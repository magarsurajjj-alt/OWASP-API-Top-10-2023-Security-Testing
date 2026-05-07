# 🔴 OWASP API4 – Unrestricted Resource Consumption

## 📌 OWASP Category

**API4: Unrestricted Resource Consumption**

---

## 🧠 What is API4?

Unrestricted Resource Consumption occurs when an API does not properly limit or control how much system resources (CPU, memory, storage, bandwidth, or processing time) a user can consume.

This allows attackers to overload the system by sending excessive requests, large payloads, or expensive operations.

---

## ⚠️ Vulnerability in This Project

In this lab, the API allows image uploads without:

* Upload size limits
* Rate limiting
* Authentication
* Processing restrictions

This allows attackers to send large or repeated image uploads, leading to server overload.

---

## 📍 Affected Endpoint

### 🔹 Upload Image

```http
POST /api/v1/images
```

---

## 🧪 Attack Scenario (Example)

### Step 1: Normal Request

User uploads a small image:

```text
image_data = small_base64_image
```

---

### Step 2: Attacker Abuse

Attacker sends very large payload:

```text
image_data = AAAAAAAAAAAAAAAAAAAAA...(Huge Data)
```

OR sends repeated requests using automation tools.

---

### Step 3: Result

* Server CPU increases
* RAM usage increases
* API becomes slow or unresponsive
* Possible server crash (DoS condition)

---

## 📸 Evidence (Add Your Screenshot)
<img width="1365" height="767" alt="Configure Iterations" src="https://github.com/user-attachments/assets/539ae960-33be-4e12-b989-ff18565add58" />

<img width="1365" height="767" alt="Runner_collection_requests" src="https://github.com/user-attachments/assets/1264a36b-73a6-4fb4-890c-7e1c7744845d" />

<img width="1365" height="767" alt="Request_allowed" src="https://github.com/user-attachments/assets/2b3666ba-0293-45c4-a82f-07e56e05ea37" />

---

## 🔥 Impact of API4

* Denial of Service (DoS)
* High server resource usage
* Increased cloud cost
* Application slowdown or crash
* Service unavailability for real users

---

## 🛠️ Root Cause

* No rate limiting implemented
* No request size validation
* No authentication or abuse control
* No timeout or processing limits

---

## 🔐 How to Fix API4

### ✅ 1. Add Rate Limiting

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)
```

---

### ✅ 2. Limit Upload Size

```python
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB limit
```

---

### ✅ 3. Validate Input Size

```python
if len(image_data) > 2000000:
    return {"error": "Payload too large"}, 413
```

---

### ✅ 4. Add Authentication

Use:

* JWT authentication
* API keys
* OAuth2

---

### ✅ 5. Monitor Resource Usage

Track:

* CPU spikes
* Memory usage
* Request frequency
* API latency

---

## 🧪 Testing Tools

* `Postman Collection Runner`
* Burp Suite Intruder
* Python scripts (automation)

---

## ⚠️ Important Note

This project is for:

* Educational purposes
* OWASP API Security learning
* Ethical hacking practice labs

Do NOT test on systems you do not own or have permission to test.

---

## 📚 Reference

```text
https://owasp.org/API-Security/
```
