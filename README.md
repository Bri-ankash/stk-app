  **🚀 STK Push Simulator API**
Simulated M-Pesa STK Push Backend | Python + Flask | Portfolio-ready
---
**Overview**
A lightweight backend API that simulates STK Push payments, stores transactions in JSON, and secures endpoints with an API key. Perfect for fintech portfolio projects.
---
**Features**
POST /pay → Send a simulated payment
GET /transactions → View all transactions
GET /transaction/<id> → Lookup a transaction by ID
Random success/failure simulation (80% success)
API key authentication
Transaction logging in transactions.json
---
**Quick Start**
git clone https://github.com/Bri-ankash/stk-app.git
cd stk-app
pip install flask
python app.py
Send a payment:
curl -X POST http://127.0.0.1:5000/pay \
-H "Content-Type: application/json" \
-H "x-api-key: mysecret123" \
-d '{"phone":"254712345678","amount":500}'
View transactions:
curl -H "x-api-key: mysecret123" http://127.0.0.1:5000/transactions
---
**Next Steps / Upgrades**
Integrate real M-Pesa Daraja API
Add user authentication
Store transactions in database
Deploy to cloud (Render/Heroku/Railway)
