以下是我的代碼：

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/css/index.css">
    <script src="https://cdn.jsdelivr.net/npm/echarts@5"></script>
    <script src="../static/javascript/index.js"></script>
    <title>E Commerce Backend</title>
</head>
<body class="wrap">
    <section class="head">
        <div>E COMMERCE BACKEND</div>
    </section>
    <section class="content">
        <aside>
            <a href="" class="search_button">HOME</a>
            <a href="search_CustomerInfo" class="search_button">CUSTOMER</a>
            <a href="search_ProductInfo" class="search_button">PRODUCT</a>
            <a href="search_OrderInfo" class="search_button">ORDER</a>
            <a href="search_CartInfo" class="search_button">CART</a>
        </aside> 
        <div class="main">
            <div class="banner">
                <div class="dashboard" id="month-order">
                    <div class="chart" id="month-order-chart"></div>
                </div>
                <div class="dashboard" id="category-sale">
                    <div class="chart" id="category-sale-chart"></div>
                </div>
            </div>
            <div class="banner">
                <div class="dashboard" id="month-sale">
                    <div class="chart" id="month-sale-chart"></div>
                </div>
            </div>
        </div>
    </section>
</body>
</html>
```

`index.css`

```css
/* 
background color: #fafafa 
float block color: #ffffff
*/
@charset "utf-8";
html {
    background-color: #fafafa;
    height: 100%;
}

.head {
    font-size: 1.25em;
    background-color: #ffffff;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 4em;
    border-bottom: 0.5px solid #ccc;
}

body {
	font-family: "Roboto", Helvetica, sans-serif;
	font-weight: 100;
	line-height: 1.75em;
    align-items: center;
    margin: 0%;
}

.wrap {
    height: 100%;
}

.content {
    height: 100%;
    display: flex;
}

aside {
    display: block;
    background-color: #ffffff;
    width: 10em;
    height: 100%;
    border-right: 0.5px solid #ccc;
}

.search_button {
    padding-top: 1em;
    padding-bottom: 1em;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.25em larger;
    text-decoration: none;
    color: #000000;
}

.search_button:hover {
    transform: scale(1.1);
    transition: all 0.3s ease 0s;
    background-color: #eaeaea;
}

.search_button:visited {
    color: #000000;
}

.main {
    width: 100%;
    height: 100%;
    display: block;
}

.banner {
    display: flex;
    width: 100%;
    height: 44%;
}

.dashboard {
    text-align: center;
    background-color: #ffffff;
    border: 0.5px solid #ccc;
    border-radius: 3px;
    margin: 1em;
    margin-bottom: 0%;
    padding: 1.5em;
}

#month-order {
    width: 50%;
    margin-right: 0.5em;
}

#category-sale {
    width: 50%;
    margin-left: 0.5em;
}

#month-sale {
    width: 100%;
}

.chart {
    width: 100%;
    height: 100%;
}
```

`index.js`

```javascript
document.addEventListener("DOMContentLoaded", function () {
    // 獲取最近30天每天的訂單數量數據
    fetch("/get_recent_orders_chart_data")
        .then(response => response.json())
        .then(data => {
            renderLineChart("month-order-chart", "最近30天每天訂單數量變化", data, "日期", "訂單數量");
        })
        .catch(error => console.error("Error fetching data:", error));

    // ... 其他圖表的請求和渲染 ...

    // 以下是一個簡單的渲染 ECharts 折線圖的函數
    function renderLineChart(containerId, title, data, xName, yName) {
        var chart = echarts.init(document.getElementById(containerId));

        var option = {
            title: {
                text: title
            },
            tooltip: {
                trigger: "axis"
            },
            xAxis: {
                type: "category",
                data: data.map(item => item[xName]),
            },
            yAxis: {
                type: "value"
            },
            series: [
                {
                    name: yName,
                    type: "line",
                    data: data.map(item => item[yName]),
                }
            ]
        };

        chart.setOption(option);
    }
});

```

`app.py`

```python
import json
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

# 新增一個路由來提供最近30天每天的訂單數量
@app.route("/get_recent_orders_chart_data", methods=["GET"])
def get_recent_orders_chart_data():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # 查詢最近30天每天的訂單數量
        cursor.execute("""
            SELECT DATE(OrderDate) as order_date, COUNT(OrderID) as order_count
            FROM OrderInfo
            WHERE OrderDate >= CURDATE() - INTERVAL 30 DAY
            GROUP BY order_date
            ORDER BY order_date
        """)
        result = cursor.fetchall()

        # 將結果轉換為 JSON 格式
        chart_data = [{"date": str(row[0]), "count": row[1]} for row in result]

        return jsonify(chart_data)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)})

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            cursor.close()



# Home page
@app.route("/")
def index():
    return render_template("index.html")

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
```

`資料庫結構`

```mysql
desc CartInfo;
+----------------+---------------+------+-----+---------+-------+
| Field          | Type          | Null | Key | Default | Extra |
+----------------+---------------+------+-----+---------+-------+
| CartId         | varchar(255)  | NO   | PRI | NULL    |       |
| CustomerId     | varchar(255)  | YES  | MUL | NULL    |       |
| TotalCartPrice | decimal(10,2) | YES  |     | NULL    |       |
+----------------+---------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

desc CartItem;
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| CartItemId      | varchar(255) | NO   | PRI | NULL    |       |
| CartId          | varchar(255) | YES  | MUL | NULL    |       |
| ProductId       | varchar(255) | YES  | MUL | NULL    |       |
| ProductQuantity | int          | YES  |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
4 rows in set (0.00 sec)

desc Category;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| CategoryId   | varchar(255) | NO   | PRI | NULL    |       |
| CategoryName | varchar(255) | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

desc CustomerInfo;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| CustomerId   | varchar(255) | NO   | PRI | NULL    |       |
| CustomerName | varchar(255) | YES  |     | NULL    |       |
| Address      | varchar(255) | YES  |     | NULL    |       |
| PhoneNumber  | varchar(15)  | YES  |     | NULL    |       |
| EmailAddress | varchar(255) | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

desc OrderInfo;
+-----------------+---------------+------+-----+---------+-------+
| Field           | Type          | Null | Key | Default | Extra |
+-----------------+---------------+------+-----+---------+-------+
| OrderId         | varchar(255)  | NO   | PRI | NULL    |       |
| OrderDate       | date          | YES  |     | NULL    |       |
| CustomerId      | varchar(255)  | YES  | MUL | NULL    |       |
| TotalOrderPrice | decimal(10,2) | YES  |     | NULL    |       |
| PurchaseStatus  | varchar(255)  | YES  |     | NULL    |       |
+-----------------+---------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

desc OrderItem;
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| OrderItemId     | varchar(255) | NO   | PRI | NULL    |       |
| OrderId         | varchar(255) | YES  | MUL | NULL    |       |
| ProductId       | varchar(255) | YES  | MUL | NULL    |       |
| ProductQuantity | int          | YES  |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
4 rows in set (0.01 sec)

desc ProductInfo;
+-----------------------+---------------+------+-----+---------+-------+
| Field                 | Type          | Null | Key | Default | Extra |
+-----------------------+---------------+------+-----+---------+-------+
| ProductId             | varchar(255)  | NO   | PRI | NULL    |       |
| ProductName           | varchar(255)  | YES  |     | NULL    |       |
| CategoryId            | varchar(255)  | YES  | MUL | NULL    |       |
| ProductRemainQuantity | int           | YES  |     | NULL    |       |
| ProductPrice          | decimal(10,2) | YES  |     | NULL    |       |
+-----------------------+---------------+------+-----+---------+-------+
5 rows in set (0.01 sec)
```

請幫我利用echart實現以下功能：

1.   在`<div class="chart" id="month-order-chart"></div>`中利用折線圖顯示最近30日內每天的訂單數量變化。我已經提供給你了我的資料庫結構，這意味著你必須將資料庫內的查詢完成。
2.   在`<div class="chart" id="category-sale-chart"></div>`中利用圓餅圖顯示最近30日內各個分類的銷售數量。我已經提供給你了我的資料庫結構，這意味著你必須將資料庫內的查詢完成。
3.   在`<div class="chart" id="month-sale-chart"></div>`中利用折線圖顯示最近30日內每天的銷售額變化。我已經提供給你了我的資料庫結構，這意味著你必須將資料庫內的查詢完成。

請實現以上功能，並提供給我「完整的」`index.html`、`index.js`、`app.py`代碼。
