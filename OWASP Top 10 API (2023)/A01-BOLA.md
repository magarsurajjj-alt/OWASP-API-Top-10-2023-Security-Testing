# 🔴 Broken Object Level Authorization (BOLA)

## 📌 OWASP Category
**API1: Broken Object Level Authorization (BOLA)**

---

## 🧠 What is BOLA?

Broken Object Level Authorization (BOLA) occurs when an API does not properly check whether a user is allowed to access or modify a specific object (data resource).

This allows attackers to access or manipulate data that does not belong to them by changing object IDs in API requests.

---

## ⚠️ Vulnerability in This Project

In this lab, the API does not validate whether the logged-in user has permission to access or modify the requested user’s data or documents.

This leads to unauthorized data access and modification.

---

## 📍 Affected Endpoints

### 🔹 Get User Documents

GET /api/users/{user_id}/documents


### 🔹 Delete Document

DELETE /api/documents/{document_id}


### 🔹 Update Document

PUT /api/documents/{document_id}


---

## 🧪 Attack Scenario (Example)

### Step 1: Normal Request
User accesses their own data:

GET /api/users/1/documents


### Step 2: Attacker Modifies ID

GET /api/users/2/documents


👉 Result: Attacker can access another user's documents

---

## 📸 Evidence (Add Your Screenshot)


screenshots/bola-attack.png


---

## 🔥 Impact of BOLA

- Unauthorized access to sensitive data
- Data leakage between users
- Privacy violation
- Possible data manipulation or deletion

---

## 🛠️ Root Cause

- No ownership check on object access
- No authorization validation at object level
- Only authentication is implemented, not authorization

---

## 🔐 How to Fix BOLA

### ✅ 1. Validate Ownership
Ensure user can only access their own data:
```python
if document["owner_id"] != current_user:
    return {"error": "Forbidden"}, 403
✅ 2. Use Role-Based Access Control (RBAC)
Admin vs User permissions
✅ 3. Use JWT with user identity
Avoid trusting URL parameters alone
✅ 4. Centralized authorization middleware