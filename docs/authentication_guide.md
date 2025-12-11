# Authentication Guide

This lab simulates a simple API key–based authentication system. The goal is to practice
how Support Engineers debug auth issues and explain them clearly to customers.

---

## 1. How authentication works in this lab

- Each request must include an **API key**.
- The API key is sent in a header, for example:

```http
x-api-key: test_api_key
```

- If the key is missing or invalid, the server returns:

```json
Status: 401 Unauthorized
{
  "error": "invalid_api_key"
}
```

---

## 2. Common customer mistakes

Typical problems you’ll see in tickets:

1. **Missing header**
2. **Wrong header name**
3. **Typo in the key**
4. **Frontend vs backend key confusion**

---

## 3. Correct examples

### JavaScript (fetch)

```js
const resp = await fetch("http://localhost:3000/api/process", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "x-api-key": "test_api_key"
  },
  body: JSON.stringify({ text: "Hello world" })
});
```

### Python (requests)

```python
import requests

resp = requests.post(
    "http://localhost:3000/api/process",
    headers={"x-api-key": "test_api_key"},
    json={"text": "Hello world"},
)
print(resp.status_code, resp.json())
```

---

## 4. Checklist for debugging auth issues

1. Is the header name correct?
2. Is the key present?
3. Is the key correct (no spaces, no typos)?
4. Does it work in Postman?
5. If still failing → escalate with request details.
