# fetchs/customer.py

from flask import Blueprint, jsonify

from utils import execute_query
from queries import FETCH

fetch_customer_bp = Blueprint("fetch_customer", __name__)

@fetch_customer_bp.route("/get_customer_number_data")
def get_customer_number_data():
    result = execute_query(FETCH.CUSTOMER_NUMBER)

    samples = [{
        "date": date, "customer_count": customer_count
    } for date, customer_count in result]

    return jsonify(
        xName=[data["date"] for data in samples],
        renderData=[data["customer_count"] for data in samples]
    )

@fetch_customer_bp.route("/get_customer_rank_data")
def get_customer_rank_data():
    result = execute_query(FETCH.CUSTOMER_RANK)
    samples = [{
        "name": customer_name, "value": total_sale
    } for customer_name, total_sale in result]
    renderData = samples[:5]
    renderData.append({
        "name": "others", "value": sum(sample["value"] for sample in samples[5:])
    })

    return jsonify(renderData)