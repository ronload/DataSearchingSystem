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
    "host": "localhost",
    "user": "ECommerceBackendUser",
    "password": "ECommerceBackendUser",
    "database": "ECommerceBackend"
}

# 路由用來顯示資料
@app.route("/show_data")
def show_data():
    # 連接到 MySQL 資料庫
    conn = mysql.connector.connect(**db_config)

    # 創建一個游標物件
    cursor = conn.cursor()

    # 定義一個簡單的 SQL 查詢
    sql_query = "SELECT * FROM CustomerInfo;"

    # 執行 SQL 查詢
    cursor.execute(sql_query)

    # 獲取查詢結果
    result = cursor.fetchall()

    # 關閉游標和連接
    cursor.close()
    conn.close()

    return str(result)

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