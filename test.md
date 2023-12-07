以下是我的代碼：

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/css/index.css">
    <script src="../static/javascript/echarts.min.js"></script>
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

`search_CustomerInfo.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/css/search_CustomerInfo.css">
    <title>Search Customer Info</title>
</head>
<body class="wrap">
    <section class="head">
        <div>E COMMERCE BACKEND</div>
    </section>
    <section class="content">
        <aside>
            <a href="/" class="search_button">HOME</a>
            <a href="search_CustomerInfo" class="search_button">CUSTOMER</a>
            <a href="search_ProductInfo" class="search_button">PRODUCT</a>
            <a href="search_OrderInfo" class="search_button">ORDER</a>
            <a href="search_CartInfo" class="search_button">CART</a>
        </aside> 
        <div class="main">
            <form action="/search_CustomerInfo" method="POST" class="search">
                <div class="condition">
                    <div class="input-item">
                        <label for="by_CustomerID">ID</label><br>
                        <input type="text" id="by_CustomerID" name="by_CustomerID" autocomplete="off">
                    </div>
                    <div class="input-item">
                        <label for="by_CustomerName">Name</label><br>
                        <input type="text" id="by_CustomerName" name="by_CustomerName" autocomplete="off">
                    </div>
                    <div class="input-item">
                        <label for="by_PhoneNumber">Phone Number</label><br>
                        <input type="text" id="by_PhoneNumber" name="by_PhoneNumber" autocomplete="off">
                    </div>
                    <div class="input-item">
                        <label for="by_Address">Address</label><br>
                        <input type="text" id="by_Address" name="by_Address" autocomplete="off">
                    </div>
                    <div class="input-item">
                        <label for="by_EmailAddress">Email Address</label><br>
                        <input type="text" id="by_EmailAddress" name="by_EmailAddress" autocomplete="off">
                    </div>
                </div>
                <input type="submit" value="Search" class="submit">
            </form>
            <div class="result">
                {% if show_no_result %}
                    <p>No results found.</p>
                {% endif %}
                {% if result %}
                    {% if result %}
                        <table>
                            <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Phone Number</th>
                                <th>Address</th>
                                <th>Email Address</th>
                            </tr>
                            {% for row in result %}
                                <tr>
                                    <td>{{ row[0] }}</td>
                                    <td>{{ row[1] }}</td>
                                    <td>{{ row[3] }}</td>
                                    <td>{{ row[2] }}</td>
                                    <td>{{ row[4] }}</td>
                                </tr>
                            {% endfor %}
                        </table>
                    {% endif %}
                {% endif %}
            </div>
        </div>
    </section>
</body>
</html>
```

`search_ProductInfo.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/css/search_CartInfo.css">
    <title>Search Customer Info</title>
</head>
<body class="wrap">
    <section class="head">
        <div>E COMMERCE BACKEND</div>
    </section>
    <section class="content">
        <aside>
            <a href="/" class="search_button">HOME</a>
            <a href="search_CustomerInfo" class="search_button">CUSTOMER</a>
            <a href="search_ProductInfo" class="search_button">PRODUCT</a>
            <a href="search_OrderInfo" class="search_button">ORDER</a>
            <a href="search_CartInfo" class="search_button">CART</a>
        </aside>
        <div class="main">
            <form action="/search_ProductInfo" method="POST" class="search">
                <div class="condition">
                    <div class="input-item">
                        <label for="by_ProductID">Product ID:</label><br>
                        <input type="text" id="by_ProductID" name="by_ProductID" autocomplete="off">
                    </div>
                    <div class="input-item">
                        <label for="by_ProductName">Product Name:</label><br>
                        <input type="text" id="by_ProductName" name="by_ProductName" autocomplete="off">
                    </div>
                    <div class="input-item">
                        <label for="by_Category">Category:</label><br>
                        <input type="text" id="by_Category" name="by_Category" autocomplete="off">
                    </div>
                </div>
                <input type="submit" value="Search" class="submit">
            </form>
            <div class="result">
                {% if show_no_result %}
                    <p>No results found.</p>
                {% endif %}
                {% if result %}
                    <table>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Remain Quantity</th>
                            <th>Category</th>
                            <th>Price</th>
                        </tr>
                        {% for row in result %}
                            <tr>
                                <td>{{ row[0] }}</td>
                                <td>{{ row[1] }}</td>
                                <td>{{ row[3] }}</td>
                                <td>{{ row[2] }}</td>
                                <td>${{ row[4] }}</td>
                            </tr>
                        {% endfor %}
                    </table>
                {% endif %}
            </div>
        </div>
    </section>
</body>
</html>
```

`search_OrderInfo.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/css/search_OrderInfo.css">
    <title>Search Order Info</title>
</head>
<body class="wrap">
    <section class="head">
        <div>E COMMERCE BACKEND</div>
    </section>
    <section class="content">
        <aside>
            <a href="/" class="search_button">HOME</a>
            <a href="search_CustomerInfo" class="search_button">CUSTOMER</a>
            <a href="search_ProductInfo" class="search_button">PRODUCT</a>
            <a href="search_OrderInfo" class="search_button">ORDER</a>
            <a href="search_CartInfo" class="search_button">CART</a>
        </aside>
        <div class="main">
            <form action="/search_OrderInfo" method="POST" class="search">
                <div class="condition">
                    <div class="input-item">
                        <label for="by_OrderID">Order ID:</label>
                        <input type="text" id="by_OrderID" name="by_OrderID" autocomplete="off">
                    </div>
                    <div class="input-item">
                        <label for="by_OrderDate">Order Date:</label>
                        <input type="text" id="by_OrderDate" name="by_OrderDate" autocomplete="off">
                    </div>
                    <div class="input-item">
                        <label for="by_CustomerID">Customer ID:</label>
                        <input type="text" id="by_CustomerID" name="by_CustomerID" autocomplete="off">
                    </div>
                    <div class="input-item">
                        <label for="by_PurchaseStatus">Purchase Status</label>
                        <input type="text" id="by_PurchaseStatus" name="by_PurchaseStatus" autocomplete="off">
                    </div>
                </div>
                <input type="submit" value="Search" class="submit">
            </form>
            <div class="result">
                {% if show_no_result %}
                    <p>No results found.</p>
                {% endif %}
                {% if result %}
                    <table>
                        <tr>
                            <th>Order ID</th>
                            <th>Date</th>
                            <th>Customer Name</th>
                            <th>Total Price</th>
                            <th>Purchase Status</th>
                            <th>Products</th>
                        </tr>
                        {% for row in result %}
                            <tr>
                                <td>{{ row[0] }}</td>
                                <td>{{ row[1] }}</td>
                                <td>{{ row[2] }}</td>
                                <td>${{ row[3] }}</td>
                                <td>{{ row[4] }}</td>
                                <td>{{ row[5] | safe}}</td>
                            </tr>
                        {% endfor %}
                    </table>
                {% endif %}
            </div>
        </div>
    </section>
</body>
</html>
```

`search_CartInfo.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/css/search_CartInfo.css">
    <title>Search Cart Info</title>
</head>
<body class="wrap">
    <section class="head">
        <div>E COMMERCE BACKEND</div>
    </section>
    <section class="content">
        <aside>
            <a href="/" class="search_button">HOME</a>
            <a href="search_CustomerInfo" class="search_button">CUSTOMER</a>
            <a href="search_ProductInfo" class="search_button">PRODUCT</a>
            <a href="search_OrderInfo" class="search_button">ORDER</a>
            <a href="search_CartInfo" class="search_button">CART</a>
        </aside> 
        <div class="main">
            <form action="/search_CartInfo" method="POST" class="search">
                <div class="condition">
                    <div class="input-item">
                        <label for="by_CustomerID">Customer ID:</label><br>
                        <input type="text" id="by_CustomerID" name="by_CustomerID" autocomplete="off">
                    </div>
                </div>
                <input type="submit" value="Search" class="submit">
            </form>
            <div class="result">
                {% if show_no_result %}
                    <p>No results found.</p>
                {% endif %}
                {% if result %}
                    <table>
                        <tr>
                            <th>Customer Name</th>
                            <th>Total Price</th>
                            <th>Products</th>
                        </tr>
                        {% for row in result %}
                            <tr>
                                <td>{{ row[0] }}</td>
                                <td>${{ row[1] }}</td>
                                <td>{{ row[2] | safe }}</td>
                            </tr>
                        {% endfor %}
                    </table>
                {% endif %}
            </div>
        </div>
    </section>
</body>
</html>
```

`index.js`

```javascript
document.addEventListener("DOMContentLoaded", function () {
    fetch("/get_month_order_data")
        .then(response => response.json())
        .then(data => { renderLineChart(
            containerID="month-order-chart",
            title="ORDERS IN THE PAST 30 DAYS", 
            xName=data.xName,
            renderData=data.renderData
        );
    })
    .catch(error => console.error("Error fetching data:", error));
    fetch("/get_category_sale_data")
        .then(response => response.json())
        .then(data => { renderPieChart(
            containerID="category-sale-chart",
            title="CATEGORY", 
            renderData=data
        );
    })
    .catch(error => console.error("Error fetching data:", error));

    fetch("/get_month_sale_data")
        .then(response => response.json())
        .then(data => { renderLineChart(
            containerID="month-sale-chart",
            title="SALES IN THE PAST 30 DAYS", 
            xName=data.xName,
            renderData=data.renderData
        );
    })
    .catch(error => console.error("Error fetching data:", error));
});

function renderLineChart(containerID, title, xName, renderData) {
    var chart = echarts.init(document.getElementById(containerID));
    option = {
        title: {
            text: title,
            left: 'center'
        },
        xAxis: {
            type: 'category',
            data: xName
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                data: renderData,
                type: 'line'
            }
        ]
    };
    chart.setOption(option)
}

function renderPieChart(containerID, title, renderData) {
    var chart = echarts.init(document.getElementById(containerID))
    option = {
        title: {
            text: title,
            left: 'center'
        },
        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            left: 'left'
        },
        series: [{
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: renderData,
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }]
    };
    chart.setOption(option)
}
```

`app.py`

```python
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

# fetch api - "ORDERS IN THE PAST 30 DAYS"
@app.route("/get_month_order_data")
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
@app.route("/get_month_sale_data")
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

@app.route("/get_category_sale_data")
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


# Home page
@app.route("/")
def index():
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

請告訴我，在我的程式碼中有沒有可以進行改進的地方。
