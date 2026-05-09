# 🔴 OWASP API9 - Improper Inventory Management

A vulnerable Flask API intentionally designed to demonstrate:

- OWASP API9: Improper Inventory Management
- Deprecated APIs
- Shadow APIs
- Forgotten endpoints
- Exposed debug routes
- Internal API exposure
- Sensitive data exposure

This project is for **educational and security testing purposes only**.

---

# 📌 OWASP Category

## API9: Improper Inventory Management

Improper Inventory Management occurs when organizations fail to properly manage:

- old API versions
- deprecated endpoints
- test APIs
- internal APIs
- debug endpoints
- undocumented APIs

Attackers often discover and exploit these forgotten APIs.

---

# 🚀 Features

This vulnerable lab includes:

| Vulnerability | Endpoint |
|---|---|
| Old API Version | `/api/v1/login` |
| Hidden API | `/api/v1/admin/users` |
| Debug Endpoint | `/debug/config` |
| Internal API Exposure | `/internal/test` |
| Sensitive Data Exposure | `/api/v1/login` |
| Missing Authentication | `/api/v1/admin/users` |
| Shadow APIs | Undocumented v1 APIs |

---

# 🛠️ Technologies Used

- Python
- Flask
- Flasgger (Swagger UI)
- Postman
- FFUF

---
# Screenshots
<img width="1365" height="767" alt="API09-old_api" src="https://github.com/user-attachments/assets/0ca1d6c0-2263-4cb9-af3a-1ea0d557291a" />
<img width="1365" height="767" alt="API09-Secure_request" src="https://github.com/user-attachments/assets/e86430b1-afdb-4310-a26e-99e604870569" />
<img width="1365" height="767" alt="API09-vulne_request" src="https://github.com/user-attachments/assets/f0e99695-8bb1-4142-9a51-1f1186a5f851" />




----------------------
# 🧪 API Endpoints

---

## ✅ Secure API (Documented)

### POST `/api/v2/login`

Secure login endpoint.

### Request

```json
{
  "email": "admin@test.com",
  "password": "admin123"
}
```

---

# 🔥 Vulnerable APIs

---

## 🔴 POST `/api/v1/login`

Deprecated API version.

### Vulnerabilities

- Password logging
- Sensitive data exposure
- Old unmanaged API

### Request

```json
{
  "email": "admin@test.com",
  "password": "admin123"
}
```

### Vulnerable Response

```json
{
  "message": "Login successful (v1)",
  "user": {
    "email": "admin@test.com",
    "password": "admin123",
    "role": "admin",
    "token": "admin-token"
  }
}
```

---

## 🔴 GET `/api/v1/admin/users`

Forgotten admin API.

### Vulnerabilities

- No authentication
- Exposes all users
- Sensitive data leak

### Example

```text
GET /api/v1/admin/users
```

---

## 🔴 GET `/debug/config`

Exposed debug endpoint.

### Vulnerabilities

- Secret key exposure
- Database credentials leak
- Internal configuration disclosure

---

## 🔴 GET `/internal/test`

Internal API exposed publicly.

---

## 🔴 GET `/api/v1/slow-data`

Legacy slow endpoint.

---

# 🧪 Testing with Postman

---

## Test Secure API

### POST

```text
http://127.0.0.1:9881/api/v2/login
```

Body:

```json
{
  "email": "admin@test.com",
  "password": "admin123"
}
```

---

## Test Vulnerable API

### POST

```text
http://127.0.0.1:9881/api/v1/login
```

Body:

```json
{
  "email": "admin@test.com",
  "password": "admin123"
}
```

---

## Test Hidden Admin API

### GET

```text
http://127.0.0.1:9881/api/v1/admin/users
```

---

## Test Debug Endpoint

### GET

```text
http://127.0.0.1:9881/debug/config
```

---

# 🔍 Discover Hidden APIs Using FFUF

---

## Install FFUF

```bash
go install github.com/ffuf/ffuf/v2@latest
```

---

## Create Wordlist

```text
v1
v2
admin
debug
internal
test
```

Save as:

```text
wordlist.txt
```

---

## Run FFUF

```bash
ffuf -u http://127.0.0.1:9881/FUZZ -w wordlist.txt
```

---

# 📌 Educational Objectives

This lab helps understand:

- OWASP API9
- API inventory management
- deprecated APIs
- hidden/shadow APIs
- debug endpoint exposure
- internal API exposure
- sensitive data leakage
- API discovery techniques

---

# 🔐 Prevention

To prevent API9 vulnerabilities:

- Maintain complete API inventory
- Remove deprecated APIs
- Disable debug endpoints
- Document all APIs
- Restrict internal APIs
- Use API gateways
- Continuously scan environments

---

# ⚠️ Disclaimer

This project is intentionally vulnerable.

Use only for:

- security research
- lab environments
- educational purposes
- ethical testing

Do NOT deploy in production.

---
