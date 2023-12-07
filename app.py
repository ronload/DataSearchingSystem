import mysql.connector
from flask import Flask, render_template, request, jsonify
from itertools import groupby
from datetime import datetime, timedelta

# Initialize Flask
app = Flask(
    __name__, 
    static_folder="static", 
    static_url_path="/static"
)

# Database setting
db_config = {
    "host": "uzb4o9e2oe257glt.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
    "user": "byg9m4pbvaijmv33",
    "password": "f5ug9tcx85x325uu",
    "database": "jw1i5zo4xwn6muaq",
    "port": 3306
}

@app.route("/get_month_order_data")
def get_month_order_data():
    # 計算最近30天的日期
    end_date = datetime.now()
    start_date = end_date - timedelta(days=29)
    date_range = [start_date + timedelta(days=i) for i in range(30)]
    
    # 將日期格式化為字符串
    xName = [date.strftime("%Y-%m-%d") for date in date_range]

    # 從數據庫查詢近30天的訂單數量
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

        # 將查詢結果轉換為字典，方便後續轉為 JSON
        date_count_dict = dict(result)

        # 根據 xName 生成 renderData
        renderData = [date_count_dict.get(date, 0) for date in xName]

        return jsonify(xName=xName, renderData=renderData)

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            cursor.close()

@app.route("/get_month_sale_data")
def get_month_sale_data():
    try:
        # 計算最近30天的日期
        end_date = datetime.now()
        start_date = end_date - timedelta(days=29)
        date_range = [start_date + timedelta(days=i) for i in range(30)]

        # 將日期格式化為字符串
        xName = [date.strftime("%Y-%m-%d") for date in date_range]

        # 從數據庫查詢近30天每天的總營業額
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

            # 將查詢結果轉換為字典，方便後續轉為 JSON
            date_sales_dict = dict(result)

            # 根據 xName 生成 renderData
            renderData = [date_sales_dict.get(date, 0) for date in xName]

            return jsonify(xName=xName, renderData=renderData)

        except Exception as e:
            return jsonify(error=str(e))

        finally:
            if connection:
                connection.close()

    except Exception as e:
        return jsonify(error=str(e))

@app.route("/get_category_sale_data")
def get_category_sale_data():
    try:
        # 从数据库查询最近30天每个类别的销售额
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

            # 记录查询结果
            app.logger.info("Query result: %s", result)

            # 将查询结果转换为字典，方便后续转为 JSON
            category_sales_data = [{"value": total_sales, "name": category_name} for category_name, total_sales in result]

            # 记录转换后的数据
            app.logger.info("Category sales data: %s", category_sales_data)

            return jsonify(category_sales_data)

        except Exception as e:
            # 记录错误信息
            app.logger.error("Error: %s", str(e))
            return jsonify(error=str(e))

        finally:
            if connection:
                connection.close()

    except Exception as e:
        # 记录错误信息
        app.logger.error("Error: %s", str(e))
        return jsonify(error=str(e))


# Home page
@app.route("/")
def index():
    # 將 xName 和 renderData 傳遞到模板中
    return render_template('index.html')

# Search customer information
@app.route("/search_CustomerInfo", methods=["GET", "POST"])
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
@app.route("/search_ProductInfo", methods=["GET", "POST"])
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
@app.route("/search_OrderInfo", methods=["GET", "POST"])
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
@app.route("/search_CartInfo", methods=["GET", "POST"])
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

if __name__ == "__main__":
    app.run(debug=True)