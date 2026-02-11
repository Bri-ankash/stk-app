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

```bash
git clone https://github.com/Bri-ankash/stk-app.git
cd stk-app
pip install flask
python app.py

---


