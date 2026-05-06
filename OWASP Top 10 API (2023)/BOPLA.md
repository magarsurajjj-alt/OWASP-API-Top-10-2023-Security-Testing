# 🔐 BOPLA (Broken Object Property Level Authorization) – Flask API

## 📌 Overview

This project demonstrates **BOPLA (Broken Object Property Level Authorization)**, a vulnerability from the **OWASP API Security Top 10**.

It is a simple Flask API built for **learning and testing how improper field-level authorization can lead to security issues**.

---

## 🎯 What is BOPLA?

**BOPLA occurs when an API does not properly restrict access to individual properties (fields) of an object**, allowing users to:

- Modify sensitive fields (e.g., `id`, `role`, `blocked`)
- Access data they should not see or change
- Perform unauthorized updates inside objects

### 🧠 Simple Explanation:
> Even if a user is allowed to access a resource, they should NOT be allowed to modify all fields inside it.

---

## ⚠️ Project Type

👉 This is an **intentionally vulnerable API lab** for educational purposes only.

❌ Do NOT use in production systems.

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Postman (for testing)

---

## 🚀 How to Run

### 1️⃣ Install Flask
```bash
pip install flask
2️⃣ Run the application
python app.py
3️⃣ Server will start at:
http://127.0.0.1:9875
📌 API Endpoints
🟢 Home
GET /
🟢 Get Video Data
GET /api/video
🔥 Update Video (Vulnerable Endpoint)
PUT /api/video/update_video
🧪 Testing BOPLA using Postman
Step 1: Normal Request
{
  "description": "updated video"
}
Step 2: BOPLA Attack Payload
{
  "title": "HACKED VIDEO",
  "blocked": false,
  "id": 999
}
🔍 Expected Vulnerable Output (if BOPLA exists)
{
  "id": 999,
  "title": "HACKED VIDEO",
  "description": "A sample video",
  "blocked": false
}
🛡️ Secure Fix (Mitigation)

To prevent BOPLA, use whitelisting approach:

allowed_properties = ["description", "blocked"]

for key in allowed_properties:
    if key in data:
        video[key] = data[key]