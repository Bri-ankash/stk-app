from flask import Flask, request, jsonify
import json
import random
import string
import time
import os

app = Flask(__name__)

DATA_FILE = "transactions.json"
API_KEY = "mysecret123"   # change this later

# Ensure transactions file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)


def generate_transaction_id():
    return "TXN" + ''.join(random.choices(string.digits, k=6))


def load_transactions():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_transactions(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=4)


def check_api_key(request):
    key = request.headers.get("x-api-key")
    return key == API_KEY


@app.route("/")
def home():
    return jsonify({"message": "STK Push Simulator API Running"})


@app.route("/pay", methods=["POST"])
def pay():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    phone = data.get("phone")
    amount = data.get("amount")

    if not phone or not amount:
        return jsonify({"error": "Phone and amount required"}), 400

    transaction_id = generate_transaction_id()

    transaction = {
        "transaction_id": transaction_id,
        "phone": phone,
        "amount": amount,
        "status": "Pending"
    }

    time.sleep(2)

    # Random success or failure (80% success rate)
    if random.randint(1, 10) <= 8:
        transaction["status"] = "Success"
    else:
        transaction["status"] = "Failed"

    transactions = load_transactions()
    transactions.append(transaction)
    save_transactions(transactions)

    return jsonify({
        "message": "STK Push Processed (Simulated)",
        "transaction_id": transaction_id,
        "status": transaction["status"]
    })


@app.route("/transactions", methods=["GET"])
def get_transactions():
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify(load_transactions())


@app.route("/transaction/<txn_id>", methods=["GET"])
def get_transaction(txn_id):
    if not check_api_key(request):
        return jsonify({"error": "Unauthorized"}), 401

    transactions = load_transactions()

    for txn in transactions:
        if txn["transaction_id"] == txn_id:
            return jsonify(txn)

    return jsonify({"error": "Transaction not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
