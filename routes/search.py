# routes/search.py

from flask import Blueprint, render_template, request

from utils import execute_query, build_conditions, merge_search_results
from queries import SEARCH

search_bp = Blueprint("search", __name__)

# Search customer information
@search_bp.route("/customer", methods=["GET", "POST"])
def customer():
    result = []
    query = SEARCH.CUSTOMER

    if request.method == "GET":
        result = execute_query(query)

    if request.method == "POST":
        conditions, values = build_conditions({
            "CustomerID": request.form.get("by_CustomerID"),
            "CustomerName": request.form.get("by_CustomerName"),
            "PhoneNumber": request.form.get("by_PhoneNumber"),
            "Address": request.form.get("by_Address"),
            "Email": request.form.get("by_EmailAddress")
        })
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        result = execute_query(query, tuple(values))

    return render_template(
        "customer.html", 
        result=result, 
        show_no_result=False
    )


# Search product information
@search_bp.route("/product", methods=["GET", "POST"])
def product():
    result = []
    query = SEARCH.PRODUCT

    if request.method == "GET":
        result = execute_query(query)

    if request.method == "POST":
        conditions, values = build_conditions({
            "ProductID": request.form.get("by_ProductID"),
            "ProductName": request.form.get("by_ProductName"),
            "Category": request.form.get("by_Category")
        })
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        result = execute_query(query, tuple(values))

    return render_template(
        "product.html", 
        result=result, 
        show_no_result=(len(result) == 0)
    )

@search_bp.route("/order", methods=["GET", "POST"])
def order():
    result = []
    query = SEARCH.ORDER

    if request.method == "GET":
        result = execute_query(query)

    if request.method == "POST":
        conditions, values = build_conditions({
            "OrderID": request.form.get("by_OrderID"),
            "OrderDate": request.form.get("by_OrderDate"),
            "CustomerID": request.form.get("by_CustomerID"),
            "PurchaseStatus": request.form.get("by_PurchaseStatus")
        })
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        result = execute_query(query, tuple(values))

    merged_result = merge_search_results(result, (0, 4), (5, 6))

    return render_template(
        "order.html", 
        result=merged_result,
        show_no_result=(len(merged_result) == 0)
    )

# Search cart information
@search_bp.route("/cart", methods=["GET", "POST"])
def cart():
    result = []
    query = SEARCH.CART

    if request.method == "GET":
        result = execute_query(query)

    if request.method == "POST":
        conditions, values = build_conditions({
            "CustomerID": request.form.get("by_CustomerID")
        })
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query +=  " GROUP BY CartInfo.CartID, ProductInfo.ProductID"
        result = execute_query(query, tuple(values))
    
    merged_result = merge_search_results(result, (0, 1), (2, 3))

    return render_template(
        "cart.html", 
        result=merged_result,
        show_no_result=(len(merged_result) == 0)
    )