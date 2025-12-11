
# Understanding CORS and Why It Happens

CORS errors occur when browser-based frontend code attempts to call an API hosted on a different domain.

---

## Why CORS Exists

- Browser security restrictions
- Backend must explicitly allow cross-origin requests
- Prevents malicious websites from calling APIs without permission

---

## Example CORS Error

Access to fetch at 'https://api.example.com' from origin 'http://localhost:3000' 
has been blocked by CORS policy.

---

## How to Fix CORS Issues

- Make API requests from your backend server, not the browser
- Enable CORS only in development (temporary)
- Double-check fetch options such as mode: 'cors'

---

## Important Note

CORS is *not* an API failure.  
It is a browser security mechanism.

---
