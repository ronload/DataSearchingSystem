# routes/search.py

import mysql.connector
from config import Config
from flask import Blueprint, render_template, request
from itertools import groupby

from config import Config

db_config = Config.DB_CONFIG

search_bp = Blueprint("search", __name__)

# Search customer information
@search_bp.route("/search_CustomerInfo", methods=["GET", "POST"])
def search_customer_info():
    result = []
    if request.method == "GET":
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM CustomerInfo")
        result = cursor.fetchall()
        return render_template(
            "search_CustomerInfo.html", 
            result=result, 
            show_no_result=False
        )

    if request.method == "POST":
        # customer attribute
        id = request.form.get("by_CustomerID")
        name = request.form.get("by_CustomerName")
        phone_number = request.form.get("by_PhoneNumber")
        address = request.form.get("by_Address")
        email = request.form.get("by_EmailAddress")

        # query
        connection = None
        try:
            # build database connection
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            conditions = []
            values = []

            # select conditions and values
            if id:
                conditions.append("CustomerID LIKE %s")
                values.append(f"{id}")
            if name:
                conditions.append("CustomerName LIKE %s")
                values.append(f"%{name}%")
            if phone_number:
                conditions.append("PhoneNumber LIKE %s")
                values.append(f"%{phone_number}%")
            if address:
                conditions.append("Address LIKE %s")
                values.append(f"%{address}%")
            if email:
                conditions.append("EmailAddress LIKE %s")
                values.append(f"%{email}%")
            
            # build SQL query
            query = "SELECT * FROM CustomerInfo"
            if conditions:
                query += " WHERE " + " AND ".join(conditions)
            cursor.execute(query, tuple(values))
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return render_template(
                "search_CustomerInfo.html", 
                result=result, 
                show_no_result=(len(result) == 0)
            )
        except mysql.connector.Error as err:
            return f"Error: {err}"
        
        finally:
            if connection is not None and connection.is_connected():
                connection.close()
                cursor.close()
            
    return render_template("search_CustomerInfo.html", result=result)

# Search product information
@search_bp.route("/search_ProductInfo", methods=["GET", "POST"])
def search_product_info():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ProductInfo")
        result = cursor.fetchall()
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            cursor.close()

    if request.method == "GET":
        return render_template(
            "search_ProductInfo.html", 
            result=result,
            show_no_result=(len(result) == 0)
        )

    if request.method == "POST":
        # product attribute
        id = request.form.get("by_ProductID")
        name = request.form.get("by_ProductName")
        category = request.form.get("by_Category")

        # query
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            conditions = []
            values = []

            # select conditions and values
            if id:
                conditions.append("ProductID LIKE %s")
                values.append(f"%{id}%")
            if name:
                conditions.append("ProductName LIKE %s")
                values.append(f"%{name}%")
            if category:
                conditions.append("Category LIKE %s")
                values.append(f"%{category}%")

            # build SQL query
            query = "SELECT * FROM ProductInfo"
            if conditions:
                query += " WHERE " + " AND ".join(conditions)
            cursor.execute(query, tuple(values))
            result = cursor.fetchall()

            cursor.close()
            connection.close()
            return render_template(
                "search_ProductInfo.html", 
                result=result, 
                show_no_result=(len(result) == 0)
            )
        except mysql.connector.Error as err:
            return f"Error: {err}"

        finally:
            if connection is not None and connection.is_connected():
                connection.close()
                cursor.close()

    return render_template("search_ProductInfo.html", result=result)

# Search order information
@search_bp.route("/search_OrderInfo", methods=["GET", "POST"])
def search_order_info():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT 
                OrderInfo.OrderID, 
                OrderInfo.OrderDate, 
                CustomerInfo.CustomerName, 
                OrderInfo.TotalOrderPrice,
                OrderInfo.PurchaseStatus,
                ProductInfo.ProductName,
                OrderItem.ProductQuantity
            FROM 
                OrderInfo
            JOIN 
                OrderItem ON OrderInfo.OrderID = OrderItem.OrderID
            JOIN 
                ProductInfo ON OrderItem.ProductID = ProductInfo.ProductID
            JOIN 
                CustomerInfo ON OrderInfo.CustomerID = CustomerInfo.CustomerID
            GROUP BY OrderInfo.OrderID, ProductInfo.ProductID
        """)
        result = cursor.fetchall()

        # Merged searching result
        merged_result = []
        for key, group in groupby(result, key=lambda x: x[:5]):
            order_info = key
            products = [f"{row[5]} * {row[6]}" for row in group]
            merged_products = '<br>'.join(products)
            merged_result.append(order_info + (merged_products,))
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            cursor.close()

    if request.method == "GET":
        return render_template(
            "search_OrderInfo.html", 
            result=merged_result,
            show_no_result=(len(merged_result) == 0)
        )

    if request.method == "POST":
        # order attribute
        order_id = request.form.get("by_OrderID")
        date = request.form.get("by_OrderDate")
        customer_id = request.form.get("by_CustomerID")
        purchase_status = request.form.get("by_PurchaseStatus")

        # query
        try:
            # build database connection
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            conditions = []
            values = []

            # select conditions and values
            if order_id:
                conditions.append("OrderInfo.OrderID LIKE %s")
                values.append(f"%{order_id}%")
            if date:
                conditions.append("OrderDate LIKE %s")
                values.append(f"%{date}%")
            if customer_id:
                conditions.append("CustomerInfo.CustomerID LIKE %s")
                values.append(f"%{customer_id}%")
            if purchase_status:
                conditions.append("PurchaseStatus LIKE %s")
                values.append(f"%{purchase_status}%")

            # build SQL query
            query = """
                SELECT 
                    OrderInfo.OrderID, 
                    OrderInfo.OrderDate, 
                    CustomerInfo.CustomerName, 
                    OrderInfo.TotalOrderPrice,
                    OrderInfo.PurchaseStatus,
                    ProductInfo.ProductName,
                    OrderItem.ProductQuantity
                FROM 
                    OrderInfo
                JOIN 
                    OrderItem ON OrderInfo.OrderID = OrderItem.OrderID
                JOIN 
                    ProductInfo ON OrderItem.ProductID = ProductInfo.ProductID
                JOIN 
                    CustomerInfo ON OrderInfo.CustomerID = CustomerInfo.CustomerID
            """

            if conditions:
                query += " WHERE " + " AND ".join(conditions)
            query += " GROUP BY OrderInfo.OrderID, ProductInfo.ProductID"
            cursor.execute(query, tuple(values))
            result = cursor.fetchall()

            # merged searching result
            merged_result = []
            for key, group in groupby(result, key=lambda x: x[:5]):
                order_info = key
                products = [f"{row[5]} * {row[6]}" for row in group]
                merged_products = '<br>'.join(products)
                merged_result.append(order_info + (merged_products,))

            cursor.close()
            connection.close()
            return render_template(
                "search_OrderInfo.html", 
                result=merged_result,
                show_no_result=(len(merged_result) == 0)
            )

        except mysql.connector.Error as err:
            return f"Error: {err}"
        
        finally:
            connection.close()
            cursor.close()

    return render_template("search_OrderInfo.html", result=merged_result)

# Search cart information
@search_bp.route("/search_CartInfo", methods=["GET", "POST"])
def search_cart_info():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT 
                CustomerInfo.CustomerName, 
                CartInfo.TotalCartPrice,
                ProductInfo.ProductName,
                CartItem.ProductQuantity
            FROM 
                CartInfo
            JOIN 
                CartItem ON CartInfo.CartID = CartItem.CartID
            JOIN 
                ProductInfo ON CartItem.ProductID = ProductInfo.ProductID
            JOIN 
                CustomerInfo ON CartInfo.CustomerID = CustomerInfo.CustomerID
            GROUP BY CartInfo.CartID, ProductInfo.ProductID
        """)
        result = cursor.fetchall()

        # Merged searching result
        merged_result = []
        for key, group in groupby(result, key=lambda x: x[:2]):
            cart_info = key
            products = [f"{row[2]} * {row[3]}" for row in group]
            merged_products = '<br>'.join(products)
            merged_result.append(cart_info + (merged_products,))
    except mysql.connector.Error as err:
        return f"Err: {err}"
    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            cursor.close()

    if request.method == "GET":
        return render_template(
            "search_CartInfo.html", 
            result=merged_result,
            show_no_result=(len(merged_result) == 0)
        )

    if request.method == "POST":
        # cart attribute
        id = request.form.get("by_CustomerID")
        
        # query
        try:
            # build connection
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            conditions = []
            values = []

            # select condition and value
            if id:
                conditions.append("CustomerInfo.CustomerID LIKE %s")
                values.append(f"%{id}%")
            
            # build sql query
            query = """
                SELECT 
                    CustomerInfo.CustomerName, 
                    CartInfo.TotalCartPrice,
                    ProductInfo.ProductName,
                    CartItem.ProductQuantity
                FROM 
                    CartInfo
                JOIN 
                    CartItem ON CartInfo.CartID = CartItem.CartID
                JOIN 
                    ProductInfo ON CartItem.ProductID = ProductInfo.ProductID
                JOIN 
                    CustomerInfo ON CartInfo.CustomerID = CustomerInfo.CustomerID
            """

            if conditions:
                query += " WHERE " + " AND ".join(conditions)
            query +=  " GROUP BY CartInfo.CartID, ProductInfo.ProductID"
            cursor.execute(query, tuple(values))
            result = cursor.fetchall()
            
            # merged searching result
            merged_result = []
            for key, group in groupby(result, key=lambda x: x[:2]):
                cart_info = key
                products = [f"{row[2]} * {row[3]}" for row in group]
                merged_products = '<br>'.join(products)
                merged_result.append(cart_info + (merged_products,))
            cursor.close()
            connection.close()

            return render_template(
                "search_CartInfo.html", 
                result=merged_result,
                show_no_result=(len(merged_result) == 0)
            )

        except mysql.connector.Error as err:
            return f"Err: {err}"
        
        finally:
            connection.close()
            cursor.close()
    return render_template("search_CartInfo.html", result=merged_result)