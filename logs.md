

## Database

###  Create Tables

1.   `Category`

     **Create**

     ```mysql
     CREATE TABLE Category (
          CategoryId VARCHAR(255) PRIMARY KEY,
          CategoryName VARCHAR(255)
      );
     ```

     **Result**

     ```sql
     desc Category;
     +--------------+--------------+------+-----+---------+-------+
     | Field        | Type         | Null | Key | Default | Extra |
     +--------------+--------------+------+-----+---------+-------+
     | CategoryId   | varchar(255) | NO   | PRI | NULL    |       |
     | CategoryName | varchar(255) | YES  |     | NULL    |       |
     +--------------+--------------+------+-----+---------+-------+
     2 rows in set (0.00 sec)
     ```

2.   

```shell
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

### Test data

```sql
-- 插入 CustomerInfo 測試資料
INSERT INTO CustomerInfo (CustomerId, CustomerName, Address, PhoneNumber, EmailAddress)
VALUES 
('C001', 'John Doe', '123 Main St, Cityville', '1234567890', 'john.doe@email.com'),
('C002', 'Jane Smith', '456 Oak St, Townsville', '9876543210', 'jane.smith@email.com');

-- 插入 Category 測試資料
INSERT INTO Category (CategoryId, CategoryName)
VALUES 
('Cat001', 'Electronics'),
('Cat002', 'Clothing');

-- 插入 ProductInfo 測試資料
INSERT INTO ProductInfo (ProductId, ProductName, CategoryId, ProductRemainQuantity, ProductPrice)
VALUES 
('P001', 'Smartphone', 'Cat001', 50, 499.99),
('P002', 'Laptop', 'Cat001', 30, 999.99),
('P003', 'T-Shirt', 'Cat002', 100, 19.99),
('P004', 'Jeans', 'Cat002', 80, 39.99);

-- 插入 OrderInfo 測試資料
INSERT INTO OrderInfo (OrderId, OrderDate, CustomerId, TotalOrderPrice, PurchaseStatus)
VALUES 
('O001', '2023-01-15', 'C001', 1499.97, 'Completed'),
('O002', '2023-02-20', 'C002', 239.97, 'Shipped');

-- 插入 OrderItem 測試資料
INSERT INTO OrderItem (OrderItemId, OrderId, ProductId, ProductQuantity)
VALUES 
('OI001', 'O001', 'P001', 2),
('OI002', 'O001', 'P003', 5),
('OI003', 'O002', 'P002', 1),
('OI004', 'O002', 'P004', 3);

-- 插入 CartInfo 測試資料
INSERT INTO CartInfo (CartId, CustomerId, TotalCartPrice)
VALUES 
('CI001', 'C001', 599.98),
('CI002', 'C002', 79.98);

-- 插入 CartItem 測試資料
INSERT INTO CartItem (CartItemId, CartId, ProductId, ProductQuantity)
VALUES 
('CII001', 'CI001', 'P001', 1),
('CII002', 'CI001', 'P003', 3),
('CII003', 'CI002', 'P002', 2),
('CII004', 'CI002', 'P004', 1);
```