# 🔴 Broken Authentication

## 📌 OWASP Category
**API2: Broken Authentication**

---

## 🧠 What is Broken Authentication?

Broken Authentication occurs when an API does not properly protect login mechanisms.

This allows attackers to:
- Guess passwords
- Perform brute-force attacks
- Use automated tools to try multiple credentials
- Bypass authentication controls

---

## ⚠️ Vulnerability in This Project

This API allows unlimited login attempts without:
- Rate limiting
- Account lockout
- CAPTCHA protection
- Brute-force detection

As a result, passwords can be easily guessed using automated tools like Postman Collection Runner.

---

## 🔄 Attack Flow (Your Testing Steps)

### Step 1: User Signup
A new user is created using the signup endpoint:


POST /api/signup


User provides:
- username
- password

---

### Step 2: Authentication Test
User logs in using valid credentials:


GET /api/secure


Authentication is verified using:
- HTTP Basic Auth (username + password)

---

### Step 3: Brute Force Setup (Postman Runner)

An attacker prepares a collection of usernames and passwords:[data.txt](https://github.com/user-attachments/files/27389471/data.txt)
username,password
user1,123
user1,admin
user1,password
user1,password1
user1,wrongpass
suraj,suraj123

These credentials are added into Postman Collection Runner.

---

### Step 4: Automated Execution

Postman Runner executes multiple login attempts automatically.

- No blocking occurs
- No delay between requests
- No account lockout

---

## 📸 Evidence (Add Your Screenshot)


screenshots/brute-force.png


---

## 🔥 Security Issue Identified

This system is vulnerable because:

- ❌ Unlimited login attempts allowed
- ❌ No rate limiting
- ❌ No account lockout after failures
- ❌ Weak password policy
- ❌ Easily guessable credentials

---

## 📊 Impact

- Password guessing becomes easy
- Accounts can be compromised
- Automated brute-force attacks succeed
- Sensitive data becomes exposed

---

## 🧪 Why This is Critical (OWASP Mapping)

This maps to:

- API2: Broken Authentication
- API4: Unrestricted Resource Consumption (related due to no rate limit)

---

## 🛠️ How to Fix This Vulnerability

### ✅ 1. Add Rate Limiting
Example:
```python
from flask_limiter import Limiter
✅ 2. Account Lockout Policy
Lock account after 5 failed attempts
✅ 3. Strong Password Policy
Minimum length
Special characters
Complexity rules
✅ 4. Use JWT Authentication

Replace Basic Auth with secure token-based authentication

✅ 5. Add Monitoring & Logging

Track repeated failed login attempts
