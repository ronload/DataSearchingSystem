# queries.py

class SEARCH:
    CUSTOMER = """
        SELECT * FROM CustomerInfo
    """
    PRODUCT = """
        SELECT * FROM ProductInfo
    """
    ORDER = """
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
    """
    CART = """
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
    """

class FETCH:
    MONTH_ORDER = """
        SELECT 
            DATE_FORMAT(OrderDate, '%Y-%m-%d') AS OrderDate,
            COUNT(OrderId) AS OrderCount
        FROM 
            OrderInfo
        WHERE 
            OrderDate >= CURDATE() - INTERVAL 29 DAY AND OrderDate <= CURDATE()
        GROUP BY
            DATE_FORMAT(OrderDate, '%Y-%m-%d')
        ORDER BY
            DATE_FORMAT(OrderDate, '%Y-%m-%d');
    """
    MONTH_SALE = """
        SELECT 
            DATE_FORMAT(OrderDate, '%Y-%m-%d') AS OrderDate, 
            SUM(TotalOrderPrice) AS TotalSales 
        FROM 
            OrderInfo 
        WHERE 
            OrderDate >= CURDATE() - INTERVAL 29 DAY AND OrderDate <= CURDATE()
        GROUP BY 
            OrderDate 
        ORDER BY 
            OrderDate;
    """
    CATEGORY_SALE = """
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
            o.OrderDate >= CURDATE() - INTERVAL 29 DAY AND o.OrderDate <= CURDATE()
        GROUP BY 
            c.CategoryName
        ORDER BY 
            TotalSales DESC;
    """
    CUSTOMER_NUMBER = """
        SELECT
            DATE_FORMAT(o.OrderDate, '%Y-%m-%d') AS OrderDate,
            COUNT(DISTINCT o.CustomerId) AS CustomerCount
        FROM
            OrderInfo o
        JOIN
            CustomerInfo c ON o.CustomerId = c.CustomerId
        WHERE 
            o.OrderDate >= CURDATE() - INTERVAL 29 DAY AND o.OrderDate <= CURDATE()
        GROUP BY
            DATE_FORMAT(o.OrderDate, '%Y-%m-%d')
        ORDER BY
            DATE_FORMAT(OrderDate, '%Y-%m-%d');
    """
    CUSTOMER_RANK = """
        SELECT 
            c.CustomerName, 
            SUM(p.ProductPrice * oi.ProductQuantity) AS TotalSales 
        FROM 
            CustomerInfo c
        JOIN 
            OrderInfo o ON c.CustomerId = o.CustomerId
        JOIN 
            OrderItem oi ON o.OrderId = oi.OrderId
        JOIN 
            ProductInfo p ON oi.ProductId = p.ProductId
        WHERE 
            o.OrderDate >= CURDATE() - INTERVAL 29 DAY AND o.OrderDate <= CURDATE()
        GROUP BY 
            c.CustomerName
        ORDER BY 
            TotalSales DESC;
    """
    PRODUCT_RANK = """
        SELECT
            ProductInfo.ProductName,
            SUM(ProductInfo.ProductPrice * OrderItem.ProductQuantity) AS TotalSale
        FROM 
            OrderInfo
        JOIN
            OrderItem ON OrderInfo.OrderID = OrderItem.OrderID
        JOIN
            ProductInfo ON ProductInfo.ProductID = OrderItem.ProductID
        WHERE
            OrderInfo.OrderDate >= CURDATE() - INTERVAL 29 DAY AND OrderInfo.OrderDate <= CURDATE()
        GROUP BY
            ProductInfo.ProductID
        ORDER BY
            TotalSale DESC
        LIMIT 10;
    """
    CATEGORY_RANK = """
        SELECT
            Category.CategoryName,
            SUM(ProductInfo.ProductPrice * OrderItem.ProductQuantity) AS TotalSale
        FROM 
            OrderInfo
        JOIN
            OrderItem ON OrderInfo.OrderID = OrderItem.OrderID
        JOIN
            ProductInfo ON ProductInfo.ProductID = OrderItem.ProductID
        JOIN
            Category ON ProductInfo.CategoryID = Category.CategoryID
        WHERE
            OrderInfo.OrderDate >= CURDATE() - INTERVAL 29 DAY AND OrderInfo.OrderDate <= CURDATE()
        GROUP BY
            Category.CategoryID
        ORDER BY
            TotalSale DESC
        LIMIT 10;
    """