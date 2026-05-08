# 🔴 OWASP API5 – Broken Function Level Authorization (BFLA)

This project is a **Flask-based security testing lab** designed to demonstrate and understand **OWASP API Top 10 - API5: Broken Function Level Authorization (BFLA)** using role-based access control.

---

## 📌 What This Project Demonstrates

- User authentication using Flask-Login
- Role-based users (admin / user)
- Protected admin API endpoint
- Testing unauthorized access (BFLA vulnerability concept)
- JSON-based login response for easy API testing

---

## 🧠 OWASP Concept (API5 - BFLA)

**Broken Function Level Authorization (BFLA)** occurs when:

> A user can access functions (endpoints) that they are not authorized to use.

Example:
- Normal user accessing admin-only API endpoint

---

## ⚙️ Tech Stack

- Python 3
- Flask
- Flask-Login
- Flasgger (Swagger UI)

---

## 🚀 Features

- 🔐 Login system (user-based authentication)
- 👤 Role support (admin / user)
- 📡 Admin API endpoint protection
- 📄 JSON login response (Postman-friendly)
- 🧪 Ready for Postman testing

---

## 👥 Example Users

| User ID | Role  |
|--------|-------|
| 1      | admin |
| 2      | user  |

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install flask flask-login flasgger
2. Run the application
python app.py

3. Server will start at:
http://127.0.0.1:9877
🔑 API Endpoints
🔹 Login
POST /login
Body (form-data or x-www-form-urlencoded):
user_id = 1 or 2
Response:
{
  "message": "Login successful",
  "id": 2,
  "role": "user"
}

🔹 Admin Endpoint (Protected)
GET /api/admin/v1/users/all
Access Control:
❌ user → blocked (403 Forbidden)
✅ admin → allowed
Response (admin only):
[
  {
    "id": 1,
    "role": "admin"
  },
  {
    "id": 2,
    "role": "user"
  }
]

🧪 How to Test (Postman)
Step 1: Login
POST http://127.0.0.1:9877/login

Step 2: Use session cookie automatically saved by Postman

Step 3: Call admin API
GET http://127.0.0.1:9877/api/admin/v1/users/all
🔥 Security Learning Outcome

You will understand:

Difference between Authentication vs Authorization
How BFLA occurs in real APIs
Why role checks are important
How attackers exploit admin endpoints
🛡️ Fix Concept (Important)

Proper authorization check:

if current_user.role != "admin":
    return jsonify({"error": "Admins only"}), 403
⚠️ Disclaimer

This project is for educational and cybersecurity learning purposes only.
Do not deploy intentionally vulnerable code in production systems.