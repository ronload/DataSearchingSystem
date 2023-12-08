# fetchs/fetch_index.py

from flask import Blueprint, jsonify

from utils import execute_query
from queries import FETCH

fetch_index_bp = Blueprint("fetch_index", __name__)

# index
@fetch_index_bp.route("/get_month_order_data")
def get_month_order_data():
    result = execute_query(FETCH.MONTH_ORDER)
    samples = [{
        "date": date, "order_count": order_count
    } for date, order_count in result]

    return jsonify(
        xName=[sample["date"] for sample in samples],
        renderData=[sample["order_count"] for sample in samples]
    )

@fetch_index_bp.route("/get_month_sale_data")
def get_month_sale_data():
    result = execute_query(FETCH.MONTH_SALE)
    samples = [{
        "date": date, "total_sale": total_sale
    } for date, total_sale in result]

    return jsonify(
        xName=[sample["date"] for sample in samples],
        renderData = [sample["total_sale"] for sample in samples]
    )

@fetch_index_bp.route("/get_category_sale_data")
def get_category_sale_data():
    result = execute_query(FETCH.CATEGORY_SALE)
    data = [{
        "name": category_name, "value": total_sale
    } for category_name, total_sale in result]

    return jsonify(data)