
# CORS Troubleshooting

CORS (Cross-Origin Resource Sharing) is a browser security feature that blocks requests coming from a different origin unless the server explicitly allows them. This guide explains how to identify CORS issues and how to separate them from real API errors.

---

## 1. What CORS actually is

CORS protects users by preventing a website on one domain from freely calling APIs on another domain.  
Example:

- Frontend: `http://localhost:5173`
- Backend: `http://localhost:3000`

These are **different origins**, so the browser checks if the backend allows the call.

If not, the browser blocks the response and shows a CORS error.

---

## 2. How CORS errors appear

CORS errors DO NOT come from the server — they come from the **browser**.

### In DevTools → Console:
- *“Access to fetch at 'http://localhost:3000' from origin 'http://localhost:5173' has been blocked by CORS policy…”*

### In DevTools → Network:
- Request may show `(blocked: CORS)`
- Status might show 200 but the response is hidden

### Important:
Postman, curl, and Python **never show CORS errors** because they are not browsers.

---

## 3. Why Postman works but the browser fails

If the request works in Postman but the browser blocks it, the backend is fine.

The issue is:

- Missing `Access-Control-Allow-Origin`
- Missing `Access-Control-Allow-Headers`
- Missing `Access-Control-Allow-Methods`

This is a **browser-only safety restriction**.

---

## 4. Preflight requests (OPTIONS)

Browsers often send a preflight request:

```http
OPTIONS /api/process
```

If this request fails or the required CORS headers are missing, the main request is blocked.

---

## 5. How to debug CORS issues

1. Open DevTools → **Console**  
   - Look for a CORS error message.

2. Open DevTools → **Network**  
   - Click the request  
   - Look at “Response Headers”  
   - Check if `Access-Control-Allow-Origin` is present

3. Test the same request using Postman  
   - If Postman works, it’s definitely CORS.

4. Make sure the frontend is not served from `file://`  
   - Always use a dev server:
     - `npm run dev`
     - `live-server`
     - `npx serve .`

---

## 6. How to fix CORS in development

Typical Express.js fix:

```js
const cors = require("cors");
app.use(cors({ origin: "*" }));
```

Or allow only a specific frontend:

```js
app.use(cors({
  origin: "http://localhost:5173",
  methods: ["GET", "POST", "OPTIONS"],
  allowedHeaders: ["Content-Type", "x-api-key"]
}));
```

---

## 7. How to explain CORS to a customer

A simple Support Engineer explanation:

> “Your API calls work in Postman but fail in your browser because the backend does not allow requests from your frontend’s domain. This is a browser security feature called CORS. Once the server adds `Access-Control-Allow-Origin` for your domain, the requests will succeed.”

---

## 8. Key point to remember

A CORS error is **NOT**:
- a server error  
- an API bug  
- a backend issue  

It is the **browser blocking the response**, not the server failing.
```
