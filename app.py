import mysql.connector
from flask import Flask, render_template

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
@app.route("/search_CustomerInfo")
def search_customer_info():
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