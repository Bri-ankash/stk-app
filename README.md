 🚀 STK Push Simulator API

**Simulated M-Pesa STK Push Backend** | Python + Flask | Portfolio-ready  

![Python](https://img.shields.io/badge/Python-3.12-blue) ![Flask](https://img.shields.io/badge/Flask-2.3-orange) ![Status](https://img.shields.io/badge/Status-Prototype-green)

---

Overview

Backend API that simulates **M-Pesa STK Push payments**.  
Transactions are logged in JSON and endpoints are secured with an **API key**.

---

Features

- `POST /pay` → Simulate payment (80% success)  
- `GET /transactions` → View all transactions  
- `GET /transaction/<id>` → Lookup a transaction  
- API key authentication  
- Transaction logging in `transactions.json`  

---

Quick Start

git clone https://github.com/Bri-ankash/stk-app.git
cd stk-app
`pip install flask
python app.py`

---

Send a payment:
curl -X POST http://127.0.0.1:5000/pay \
`-H "Content-Type: application/json" \
-H "x-api-key: mysecret123" \
-d '{"phone":"254712345678","amount":500}'`

---

View transactions:
curl -H "x-api-key: mysecret123" http://127.0.0.1:5000/transactions

---

Author
Brian Kash | GitHub:https://github.com/Bri-ankash/
