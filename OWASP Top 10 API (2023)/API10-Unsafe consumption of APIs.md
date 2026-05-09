# 🔴 OWASP API10: Unsafe Consumption of APIs

## 📌 Overview

This project demonstrates **OWASP API10:2023 – Unsafe Consumption of APIs**, where an application blindly trusts data from external APIs without proper validation or sanitization.

It shows how a malicious or compromised external API can inject unsafe data into an application and affect the final response returned to users.

---

## 🎯 Objective

- Understand how API10 vulnerability works  
- Simulate a malicious external API  
- Demonstrate unsafe API consumption behavior  
- Learn how proper validation prevents security issues  

---

## 🧠 What is API10?

> Unsafe Consumption of APIs occurs when an application **trusts external API responses without validating them**, allowing attackers or compromised services to inject malicious or unexpected data.

---

## ⚠️ Attack Scenario

- External API returns malicious or modified data  
- Main application blindly trusts the response  
- Unsafe data is directly returned to the client  
- This can lead to issues like XSS, data corruption, or logic abuse  

---
## Sreenshots
<img width="1365" height="767" alt="API10-vulnerable" src="https://github.com/user-attachments/assets/a44ee62e-02cb-44b5-bf27-08fd47e6c959" />
<img width="1365" height="767" alt="API10-third_party_fake_api" src="https://github.com/user-attachments/assets/023cab68-9af7-43aa-a8fd-58d10e3484e8" />
<img width="1365" height="767" alt="API10-main_code" src="https://github.com/user-attachments/assets/8e2561b3-a672-4bea-99c3-8d7ec36c5e5b" />

----------------
## 🧪 How to Test (Step-by-Step)

### 🔹 Step 1 — Run Fake External API
Run the malicious external API (simulating attacker-controlled service):

```bash
python fake_api.py

It will run on:

http://127.0.0.1:5001/random
🔹 Step 2 — Run Main Vulnerable API
python app.py

It will run on:

http://127.0.0.1:9882/api/quote
🔹 Step 3 — Test Using Postman

Open Postman and send:

GET http://127.0.0.1:9882/api/quote
🔥 Expected Vulnerable Response
{
  "quote": "<script>alert('API10 ATTACK')</script>",
  "source": "evil-api"
}
💣 What This Demonstrates

This confirms:

The application trusts external API blindly
No validation or sanitization is applied
Malicious data is passed directly to the user
This is a classic API10 vulnerability
❌ Security Issues
No validation of external API response
No sanitization of output
Blind trust in third-party data
Possible injection of malicious content (XSS, HTML injection)
🛡️ Secure Fix Concept

To prevent API10 issues:

Validate all external API responses
Sanitize output before returning to users
Ensure strict data type checking
Limit trust boundaries between services

Example:

import html

quote = data.get("content", "")

if not isinstance(quote, str):
    return jsonify({"error": "Invalid data"}), 500

safe_quote = html.escape(quote)
🧪 Learning Outcome

After studying this lab, you will understand:

How unsafe API consumption happens in real systems
Why trusting external APIs is risky
How attackers manipulate API responses
How to secure API integrations properly
📚 OWASP Reference
https://owasp.org/www-project-api-security/
