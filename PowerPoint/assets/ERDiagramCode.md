這是我的資料庫查詢結果：

```mysql
mysql> SELECT 
    ->     OrderInfo.OrderDate, 
    ->     OrderInfo.OrderID, 
    ->     CustomerInfo.CustomerName, 
    ->     ProductInfo.ProductName, 
    ->     OrderItem.ProductQuantity, 
    ->     OrderInfo.PurchaseStatus
    -> FROM 
    ->     OrderInfo
    -> JOIN 
    ->     OrderItem ON OrderInfo.OrderID = OrderItem.OrderID
    -> JOIN 
    ->     ProductInfo ON OrderItem.ProductID = ProductInfo.ProductID
    -> JOIN 
    ->     CustomerInfo ON OrderInfo.CustomerID = CustomerInfo.CustomerID;
+------------+---------+--------------+-------------+-----------------+----------------+
| OrderDate  | OrderID | CustomerName | ProductName | ProductQuantity | PurchaseStatus |
+------------+---------+--------------+-------------+-----------------+----------------+
| 2023-01-15 | O001    | John Doe     | Smartphone  |               2 | Completed      |
| 2023-02-20 | O002    | Jane Smith   | Laptop      |               1 | Shipped        |
| 2023-01-15 | O001    | John Doe     | T-Shirt     |               5 | Completed      |
| 2023-02-20 | O002    | Jane Smith   | Jeans       |               3 | Shipped        |
+------------+---------+--------------+-------------+-----------------+----------------+
4 rows in set (0.03 sec)
```

這是我的前端代碼`search_OrderInfo.html`：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Order Info</title>
</head>
<body>
    <h1>Search Order Info</h1>
    <form action="/search_OrderInfo" method="POST">
        <label for="by_OrderID">Order ID:</label>
        <input type="text" id="by_OrderID" name="by_OrderID">
        <label for="by_OrderDate">Order Date:</label>
        <input type="text" id="by_OrderDate" name="by_OrderDate">
        <!-- <label for="by_CustomerName">Customer Name:</label>
        <input type="text" id="by_CustomerName" name="by_CustomerName"> -->
        <label for="by_CustomerID">Customer ID:</label>
        <input type="text" id="by_CustomerID" name="by_CustomerID">
        <label for="by_PurchaseStatus">Purchase Status</label>
        <input type="text" id="by_PurchaseStatus" name="by_PurchaseStatus">
        <input type="submit" value="Search">
    </form>
    {% if result is not none %}
        {% if result %}
            <h2>Search Result:</h2>
            <table border="1">
                <tr>
                    <th>Order ID</th>
                    <th>Date</th>
                    <th>Customer ID</th>
                    <th>Total Price</th>
                    <th>Purchase Status</th>
                </tr>
                {% for row in result %}
                    <tr>
                        <td>{{ row[0] }}</td>
                        <td>{{ row[1] }}</td>
                        <td>{{ row[2] }}</td>
                        <td>${{ row[3] }}</td>
                        <td>{{ row[4] }}</td>
                    </tr>
                {% endfor %}
            </table>
        {% else %}
            <p>No results found.</p>
        {% endif %}
    {% endif %}
</body>
</html>
```

這是我的後端代碼`app.py`：

```python
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
    result = None
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
            return render_template("search_CustomerInfo.html", result=result)
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
            return render_template("search_ProductInfo.html", result=result)
        except mysql.connector.Error as err:
            return f"Error: {err}"

        finally:
            connection.close()
            cursor.close();

    return render_template("search_ProductInfo.html")

# Search order information
@app.route("/search_OrderInfo", methods=["GET", "POST"])
def search_order_info():
    result = None
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
                conditions.append("OrderID LIKE %s")
                values.append(f"%{order_id}%")
            if date:
                conditions.append("OrderDate LIKE %s")
                values.append(f"%{date}%")
            if customer_id:
                conditions.append("CustomerID LIKE %s")
                values.append(f"%{customer_id}%")
            if purchase_status:
                conditions.append("PurchaseStatus LIKE %s")
                values.append(f"%{customer_id}%")

            # build SQL query
            query = """ 
                SELECT OrderInfo.OrderID, OrderInfo.OrderDate, CustomerInfo.CustomerName,  
            """
            if conditions:
                query += " WHERE " + " AND ".join(conditions)
            cursor.execute(query, tuple(values))
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return render_template("search_OrderInfo.html", result=result)

        except mysql.connector.Error as err:
            return f"Error: {err}"
        
        finally:
            connection.close()
            cursor.close()

    return render_template("search_OrderInfo.html")

# Search cart information
@app.route("/search_CartInfo")
def search_cart_info():
    return render_template("search_CartInfo.html")

if __name__ == "__main__":
    app.run(debug=True)
```

