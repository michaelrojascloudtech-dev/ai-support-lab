
# HTTP Errors Explained

This guide explains the meaning of common HTTP errors and how they are reproduced in this lab. Support Engineers must understand which errors come from the client, which come from the server, and how to explain each one clearly to customers.

---

## 1. 4xx vs 5xx — who is responsible?

### 4xx errors  
The **client** sent something incorrect.  
Examples:
- Missing header
- Bad JSON
- Wrong endpoint
- Rate limits
- Validation issues

### 5xx errors  
The **server** failed unexpectedly.  
Examples:
- Internal bugs
- Infrastructure issues
- Upstream failures

---

## 2. Errors used in this lab

### 400 – Bad Request (`missing_text`)
The request body is missing required fields or improperly formatted JSON.

---

### 401 – Unauthorized (`invalid_api_key`)
Authentication failed. The API key is missing, wrong, or malformed.

---

### 403 – Forbidden (`forbidden`)
The request is authenticated but not allowed due to permissions.

---

### 404 – Not Found (`not_found`)
The requested route or resource does not exist.

---

### 408 – Request Timeout (`timeout`)
The server took too long to respond. The client gave up waiting.

---

### 409 – Conflict (`conflict`)
The request conflicts with the current resource state.  
Examples:
- Duplicate resource creation
- Version conflicts

---

### 413 – Payload Too Large (`payload_too_large`)
The body is larger than the server’s allowed size.

---

### 422 – Unprocessable Entity (`unprocessable_entity`)
The request is formatted correctly but semantically invalid.  
Examples:
- Wrong data type
- Missing required semantic values

---

### 429 – Too Many Requests (`rate_limit`)
The client sent too many requests in a short period.

---

### 500 – Internal Server Error (`server_error`)
The server experienced an unexpected failure.

---

## 3. How to explain errors to customers

### Short, clear, and actionable advice:

**400 – Bad Request**  
“Your request body is missing the required field or contains invalid JSON.”

**401 – Unauthorized**  
“The API key is incorrect or missing.”

**403 – Forbidden**  
“Your key is valid, but this action is not permitted.”

**404 – Not Found**  
“The endpoint or resource does not exist.”

**408 – Timeout**  
“The server took too long to respond.”

**409 – Conflict**  
“There is a conflicting existing resource.”

**413 – Payload Too Large**  
“The request body exceeds the allowed limit.”

**422 – Unprocessable Entity**  
“Your request is valid JSON but fails validation.”

**429 – Rate Limit**  
“You sent too many requests too quickly.”

**500 – Internal Server Error**  
“This failure is on our side — I’ve escalated it.”

---

## 4. Support Engineer checklist

1. Reproduce the error using Postman.  
2. Verify request headers and body format.  
3. Check server logs or simulated logs.  
4. Identify client vs server side issue.  
5. Provide clear explanation and next steps.  
6. Escalate if multiple users or internal failures occur.
```
