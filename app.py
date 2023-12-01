import mysql.connector
from flask import Flask, render_template, request

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
    "password": "u6wbqkhe1bpbzz2j",
    "database": "jw1i5zo4xwn6muaq",
    "port": 3306
}

# 路由用來顯示資料
@app.route("/show_data")
def show_data():
    try:
        # 尝试连接到 MySQL 数据库
        conn = mysql.connector.connect(**db_config)

        # 创建一个游标对象
        cursor = conn.cursor()

        # 定义一个简单的 SQL 查询
        sql_query = "SELECT * FROM CustomerInfo;"

        # 执行 SQL 查询
        cursor.execute(sql_query)

        # 获取查询结果
        result = cursor.fetchall()

        # 关闭游标和连接
        cursor.close()
        conn.close()

        return str(result)

    except mysql.connector.Error as err:
        # 处理连接错误
        return f"Error: {err}"

    finally:
        # 最后确保关闭数据库连接
        if conn.is_connected():
            cursor.close()
            conn.close()

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Search customer information
@app.route("/search_CustomerInfo", methods=["GET", "POST"])
def search_customer_info():
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
            if name:
                conditions.append("username LIKE %s")
                values.append(f"%{name}%")
            if phone_number:
                conditions.append("phonenumber LIKE %s")
                values.append(f"%{phone_number}%")
            if address:
                conditions.append("address LIKE %s")
                values.append(f"%{address}%")
            if email:
                conditions.append("email LIKE %s")
                values.append(f"%{email}%")
            
            # build SQL query
            query = "SELECT * FROM CustomerInfo"
            if conditions:
                query += " WHERE " + " AND ".join(conditions)
            cursor.execute(query, tuple(values))
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return str(result)
        except mysql.connector.Error as err:
            return f"Error: {err}"
        
        finally:
            if connection is not None and connection.is_connected():
                connection.close()
                cursor.close()
            
    return render_template("search_CustomerInfo.html")

# Search product information
@app.route("/search_ProductInfo")
def search_product_info():
    return render_template("search_ProductInfo.html")

# Search order information
@app.route("/search_OrderInfo")
def search_order_info():
    return render_template("search_OrderInfo.html")

# Search cart information
@app.route("/search_CartInfo")
def search_cart_info():
    return render_template("search_CartInfo.html")

if __name__ == "__main__":
    app.run(debug=True)