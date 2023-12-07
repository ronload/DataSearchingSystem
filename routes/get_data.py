# routes/get_data.py

import mysql.connector
from flask import Blueprint, jsonify
from datetime import datetime, timedelta

from config import Config

get_data_bp = Blueprint("get_data", __name__)

db_config = Config.DB_CONFIG

# fetch api - "ORDERS IN THE PAST 30 DAYS"
@get_data_bp.route("/get_month_order_data")
def get_month_order_data():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=29)
    date_range = [start_date + timedelta(days=i) for i in range(30)]
    
    xName = [date.strftime("%Y-%m-%d") for date in date_range]

    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
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

        cursor.execute(query, (start_date,))
        result = cursor.fetchall()

        date_count_dict = dict(result)
        renderData = [date_count_dict.get(date, 0) for date in xName]

        return jsonify(xName=xName, renderData=renderData)

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            cursor.close()

# fetch api - "ORDERS IN THE PAST 30 DAYS"
@get_data_bp.route("/get_month_sale_data")
def get_month_sale_data():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=29)
    date_range = [start_date + timedelta(days=i) for i in range(30)]

    xName = [date.strftime("%Y-%m-%d") for date in date_range]

    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

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

        cursor.execute(query, (start_date,))
        result = cursor.fetchall()

        date_sales_dict = dict(result)
        renderData = [date_sales_dict.get(date, 0) for date in xName]

        return jsonify(xName=xName, renderData=renderData)

    except Exception as err:
        return jsonify(error=str(err))

    finally:
        if connection:
            connection.close()

@get_data_bp.route("/get_category_sale_data")
def get_category_sale_data():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

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

        cursor.execute(query)
        result = cursor.fetchall()
        category_sales_data = [{"value": total_sales, "name": category_name} for category_name, total_sales in result]

        return jsonify(category_sales_data)

    except Exception as err:
        return jsonify(error=str(err))

    finally:
        if connection:
            connection.close()