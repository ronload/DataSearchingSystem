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
            return str(result)
        except mysql.connector.Error as err:
            return f"Error: {err}"
        
        finally:
            if connection is not None and connection.is_connected():
                connection.close()
                cursor.close()
            
    return render_template("search_CustomerInfo.html")

# Search product information
@app.route("/search_ProductInfo", methods=["GET", "POST"])
def search_product_info():
    if request.method == "POST":
        # product attribute
        id = request.form.get("by_ProductID")
        name = request.form.get("by_ProductName")
        category = request.form.get("by_Category")

        # query
        connection = None
        try:
            # connect database
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
            return str(result)
        except mysql.connector.Error as err:
            return f"Error: {err}"
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