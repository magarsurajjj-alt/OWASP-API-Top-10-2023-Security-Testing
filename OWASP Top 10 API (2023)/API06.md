# 🔴 OWASP API6 – Unrestricted Access to Sensitive Business Flows

This project is a **Flask-based security lab** demonstrating **OWASP API6: Unrestricted Access to Sensitive Business Flows**, where business logic (buying, redeeming coupons, resetting stock) can be abused due to missing protections like rate limiting, validation, and workflow controls.

---

## 📌 What This Project Demonstrates

This lab shows how attackers can abuse API business flows such as:

- 🛒 Repeated purchasing without limits
- 💰 Coupon/reward abuse (infinite wallet increase)
- 📦 Unauthorized stock reset
- 🔁 Automation of business actions (API spam)

---

## 🧠 OWASP Concept (API6)

> API6 occurs when APIs allow users to abuse legitimate business workflows due to missing controls, validation, or rate limiting.

### Example abuse:
- Redeeming coupons multiple times
- Repeating purchases without restrictions
- Resetting stock without authorization

---

## ⚙️ Tech Stack

- Python 3
- Flask

---

## 📂 Project Structure


app.py


---

## 🚀 Features

- 🛒 Product purchase API (`/buy`)
- 💰 Coupon redeem API (`/redeem`)
- 📦 Stock reset API (`/reset-stock`)
- 🧪 Wallet tracking (in-memory simulation)
- ❌ Intentionally vulnerable business logic (for learning)

---

## 👥 Sample Data

### Wallet

| User ID | Balance |
|--------|--------|
| 1      | 1000   |

### Stock

| Product | Quantity |
|--------|----------|
| laptop | 5        |

---

## ▶️ How to Run

### 1. Install Flask

```bash
pip install flask
2. Run the application
python app.py
3. Server will start at
http://127.0.0.1:5001
📡 API Endpoints
🛒 1. Buy Product
POST /buy
Body (x-www-form-urlencoded):
KEY	VALUE
user_id	1
product	laptop
quantity	1
Response:
{
  "message": "Order placed successfully",
  "remaining_wallet": 800,
  "remaining_stock": 4
}
💰 2. Redeem Coupon
POST /redeem
Body:
KEY	VALUE
user_id	1
value	100
Response:
{
  "message": "Coupon redeemed",
  "wallet": 1100
}

⚠️ Can be abused repeatedly (API6 vulnerability)

📦 3. Reset Stock
POST /reset-stock
Body:
KEY	VALUE
product	laptop
Response:
{
  "message": "Stock reset done",
  "stock": {
    "laptop": 100
  }
}

⚠️ No authentication or restriction

🧪 How to Test (Postman)
Open Postman
Send requests to:
/buy
/redeem
/reset-stock
Repeat requests multiple times
Observe:
wallet manipulation
stock manipulation
lack of limits
🔥 Security Issue Demonstrated
Issue	Description
No rate limiting	APIs can be spammed
No workflow control	Steps can be repeated freely
No business validation	Rules can be bypassed
No authorization	Sensitive actions exposed
🛡️ How to Fix API6

In real applications, you should implement:

✅ Rate limiting (requests per minute)
✅ One-time coupon usage
✅ Transaction validation
✅ Authentication + authorization
✅ Workflow/state validation
✅ Anti-bot protection
⚠️ Disclaimer

This project is for educational purposes only.
It demonstrates intentionally vulnerable logic for learning OWASP API security concepts.

Do NOT deploy this in production.