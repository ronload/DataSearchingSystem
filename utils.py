# utils.py

import mysql.connector
from itertools import groupby
from config import Config

db_config = Config.DB_CONFIG

def execute_query(query, params=None):
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        result = cursor.fetchall()
        return result

    except Exception as err:
        print(f"Database connection error: {err}")
        raise

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

def build_conditions(attributes):
    conditions = []
    values = []
    for key, value in attributes.items():
        if value:
            conditions.append(f"{key} LIKE %s")
            values.append(f"%{value}%")
    return conditions, values

def merge_search_results(result, key_indices, product_indices):
    merged_result = []
    for key, group in groupby(result, key=lambda x: x[key_indices[0]:key_indices[-1] + 1]):
        info = key
        products = [f"{row[product_indices[0]]} * {row[product_indices[1]]}" for row in group]
        merged_products = '<br>'.join(products)
        merged_result.append(info + (merged_products,))
    return merged_result