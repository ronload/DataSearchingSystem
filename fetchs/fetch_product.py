# fetchs/fetch_product.py

from flask import Blueprint, jsonify

from utils import execute_query
from queries import FETCH


fetch_product_bp = Blueprint("fetch_product", __name__)

@fetch_product_bp.route("/get_product_rank_data")
def get_product_rank_data():
    result = execute_query(FETCH.PRODUCT_RANK)
    samples = [{
        "name": product_name, "value": product_sale
    } for product_name, product_sale in result]
    renderData = samples[:5]
    renderData.append({
        "name": "others", "value": sum(sample["value"] for sample in samples[5:])
    })

    return jsonify(renderData)

@fetch_product_bp.route("/get_category_rank_data")
def get_category_rank_data():
    result = execute_query(FETCH.CATEGORY_RANK)
    samples = [{
        "name": category_name, "value": total_sale
    } for category_name, total_sale in result]
    renderData = samples[:5]
    renderData.append({
        "name": "others", "value": sum(sample["value"] for sample in samples[5:])
    })

    return jsonify(renderData)