# 🔥 SSRF Vulnerable API Lab (Flask)

This project is a **learning lab** for understanding and testing:

> 🔐 Server-Side Request Forgery (SSRF) — OWASP API Security Top 10 (API7)

It demonstrates how an attacker can force a server to make requests to internal systems using a user-controlled URL input.

---

# ⚠️ DISCLAIMER

⚠️ This project is intentionally vulnerable for **educational purposes only**.  
Do NOT deploy it on the internet or production systems.

---

# 📌 What You Will Learn

- How SSRF works in real-world APIs
- How attackers access internal endpoints via server requests
- Why URL validation is critical
- How internal services can be exposed
- How to test SSRF using Postman

---

# 🚀 Features

- Flask REST API
- Swagger UI documentation (`/apidocs`)
- Internal test endpoints (`/admin`, `/internal-api`)
- File saving of fetched responses
- Intentionally vulnerable SSRF endpoint

---
## Screenshots
<img width="1365" height="767" alt="A07-SSRF_test2" src="https://github.com/user-attachments/assets/d3afa599-483c-443f-aab3-e520eaf329b7" />
<img width="1365" height="767" alt="A07-SSRF_test_1" src="https://github.com/user-attachments/assets/78040bd3-aa81-4988-937b-592aa3a0fb5c" />
<img width="1365" height="767" alt="A07-SSRF_normal_request" src="https://github.com/user-attachments/assets/abe5884f-3217-4376-a906-694f38b1c0fd" />




# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/ssrf-lab.git
cd ssrf-lab
2. Install dependencies
pip install flask flasgger requests
3. Run the application
python app.py

Server will start at:

http://127.0.0.1:9878
📘 API Documentation (Swagger)

After running the app:

http://127.0.0.1:9878/apidocs
📡 API Endpoints
🏠 Home
GET /

Returns:

{
  "message": "SSRF Lab Running"
}
🔐 Internal Admin Endpoint
GET /admin

Example response:

{
  "admin_panel": true,
  "secret_key": "SUPER-SECRET-KEY"
}
🔒 Internal API Endpoint
GET /internal-api

Example response:

{
  "database_password": "root123",
  "api_token": "INTERNAL-TOKEN-123"
}
⚠️ SSRF Vulnerable Endpoint
POST /api/fetch
Request Body:
{
  "url": "http://example.com"
}
Example SSRF Payload:
{
  "url": "http://127.0.0.1:9878/admin"
}
🧪 How to Test SSRF (Postman)
Step 1

Set method:

POST
Step 2

URL:

http://127.0.0.1:9878/api/fetch
Step 3

Headers:

Content-Type: application/json
Step 4

Body:

{
  "url": "http://127.0.0.1:9878/internal-api"
}
🔥 SSRF Attack Flow
Attacker → API → Server → Internal Services

Example:

User input URL → Flask server → localhost/admin → Sensitive data exposed
📂 Saved Files

All fetched responses are stored in:

/downloads
🛡️ Security Issues Demonstrated
❌ No URL validation
❌ No IP restriction (localhost allowed)
❌ No domain allowlist
❌ No content-type enforcement
❌ No SSRF protection
🧠 OWASP Mapping

This project demonstrates:

OWASP API7: Server-Side Request Forgery (SSRF)

🛡️ How to Fix SSRF (Conceptual)
Allowlist domains only
Block private IP ranges
Validate DNS resolution
Disable redirect abuse
Use network-level restrictions
