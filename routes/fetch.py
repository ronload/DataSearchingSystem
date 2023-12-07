# routes/fetch.py

import mysql.connector
from flask import Blueprint, jsonify
from datetime import datetime, timedelta

from config import Config

fetch_bp = Blueprint("fetch", __name__)

db_config = Config.DB_CONFIG

def execute_query(query, params=None):
    connection = None
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
        # Handle the error appropriately, you might want to log it.
        raise

    finally:
        if connection and connection.is_connected():
            connection.close()
            cursor.close()

@fetch_bp.route("/get_month_order_data")
def get_month_order_data():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=29)
    date_range = [start_date + timedelta(days=i) for i in range(30)]
    
    xName = [date.strftime("%Y-%m-%d") for date in date_range]

    query = """
        SELECT 
            DATE_FORMAT(OrderDate, '%Y-%m-%d') AS OrderDate,
            COUNT(OrderId) AS OrderCount
        FROM 
            OrderInfo
        WHERE 
            OrderDate >= %s
        GROUP BY
            DATE_FORMAT(OrderDate, '%Y-%m-%d')
        ORDER BY
            DATE_FORMAT(OrderDate, '%Y-%m-%d');
    """

    params = (start_date,)

    result = execute_query(query, params)

    date_count_dict = dict(result)
    renderData = [date_count_dict.get(date, 0) for date in xName]

    return jsonify(xName=xName, renderData=renderData)

@fetch_bp.route("/get_month_sale_data")
def get_month_sale_data():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=29)
    date_range = [start_date + timedelta(days=i) for i in range(30)]

    xName = [date.strftime("%Y-%m-%d") for date in date_range]

    query = """
        SELECT 
            DATE_FORMAT(OrderDate, '%Y-%m-%d') AS OrderDate, 
            SUM(TotalOrderPrice) AS TotalSales 
        FROM 
            OrderInfo 
        WHERE 
            OrderDate >= %s 
        GROUP BY 
            OrderDate 
        ORDER BY 
            OrderDate;
    """

    params = (start_date,)

    result = execute_query(query, params)

    date_sales_dict = dict(result)
    renderData = [date_sales_dict.get(date, 0) for date in xName]

    return jsonify(xName=xName, renderData=renderData)

@fetch_bp.route("/get_category_sale_data")
def get_category_sale_data():
    query = """
        SELECT 
            c.CategoryName, 
            SUM(p.ProductPrice * oi.ProductQuantity) AS TotalSales 
        FROM 
            Category c
        JOIN 
            ProductInfo p ON c.CategoryId = p.CategoryId
        JOIN 
            OrderItem oi ON p.ProductId = oi.ProductId
        JOIN 
            OrderInfo o ON oi.OrderId = o.OrderId
        WHERE 
            o.OrderDate >= CURDATE() - INTERVAL 29 DAY 
        GROUP BY 
            c.CategoryName
        ORDER BY 
            TotalSales DESC;
    """

    result = execute_query(query)

    category_sales_data = [{"value": total_sales, "name": category_name} for category_name, total_sales in result]

    return jsonify(category_sales_data)
