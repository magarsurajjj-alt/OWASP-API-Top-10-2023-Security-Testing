🔴 API8: Security Misconfiguration
📌 OWASP Category

API8: Security Misconfiguration (OWASP API Security Top 10 2023)

🧠 What is API8?

Security Misconfiguration occurs when an API is exposed or deployed with unsafe settings, such as:

Debug or internal endpoints exposed
Missing access control
Insecure default configuration
Sensitive information leakage
⚠️ Vulnerability in This Project

In this API, insecure configuration leads to exposure of internal system information and unprotected endpoints.

No Swagger or API documentation is used in this project.

📍 Affected Endpoints (Postman Tested)
🔹 Debug Information Leak
GET http://localhost:5000/api/debug
🔹 Public Data Endpoint (No Authentication)
GET http://localhost:5000/api/data
🧪 Attack Scenario (Postman Testing)
Step 1: Access Debug Endpoint
GET /api/debug
Result:
Internal configuration details are exposed
Sensitive system information is visible
Step 2: Access Public API Without Login
GET /api/data
Result:
Data is accessible without authentication
No access control is enforced
📸 Evidence (Add Your Postman Screenshots)



🔥 Impact of API8
Internal system information leakage
Unauthorized access to API endpoints
Easier attacker reconnaissance
Weak system security posture
🛠️ Root Cause
Debug endpoint exposed in production-like environment
Missing authentication on sensitive routes
No access control enforcement
Insecure configuration of API routes
🔐 How to Fix API8
✅ 1. Disable Debug Endpoints

Remove or protect debug routes in production

✅ 2. Add Authentication
from flask_httpauth import HTTPBasicAuth
✅ 3. Restrict Access to Sensitive APIs

Ensure only authorized users can access endpoints

✅ 4. Hide Internal Information

Never expose:

Environment variables
Secret keys
Database configuration
✅ 5. Secure Deployment
Do not expose development endpoints publicly
Use environment-based configuration (dev vs prod)