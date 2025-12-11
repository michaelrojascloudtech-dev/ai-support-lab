
# JSON Formatting

Incorrect JSON is one of the most common causes of API issues. This guide explains how JSON works, how it breaks, and how it produces the `400 missing_text` error in this lab.

---

## 1. What JSON is

JSON is a **string-based** structured format. It must follow very strict rules:

- Keys must use **double quotes**
- String values must use **double quotes**
- No trailing commas
- Must represent one complete object

Correct example:

```json
{
  "text": "Hello world",
  "debug": "slow_api_response"
}
```

---

## 2. Common invalid JSON examples

Missing quotes around key:

```json
{
  text: "Hello world"
}
```

Trailing comma:

```json
{
  "text": "Hello world",
}
```

Unquoted value:

```json
{
  "text": Hello
}
```

---

## 3. JavaScript: object vs JSON string

A mistake many customers make is sending a JS object instead of JSON.

❌ Incorrect:

```js
body: { text: "Hello" }
```

✔ Correct:

```js
body: JSON.stringify({ text: "Hello" })
```

If you forget `JSON.stringify()`, the API often receives an empty or invalid body.

---

## 4. Why the lab returns 400 missing_text

You will see:

```json
{
  "error": "missing_text"
}
```

when:

- The JSON cannot be parsed  
- The body is `{}`  
- The `"text"` field is missing  
- The wrong key is used  
- The `Content-Type` header is incorrect  

---

## 5. Debugging JSON issues

1. Check **DevTools → Network → Request Payload**  
2. Verify the header:  
   `Content-Type: application/json`  
3. If using fetch, ensure `JSON.stringify()` is applied  
4. If using Python, use `json={}` instead of `data={}`  
5. Test the same payload in Postman  

If Postman succeeds but the frontend fails → the issue is JSON formatting in the frontend.

---

## 6. How to explain JSON issues to customers

> “Your request body contains invalid JSON or is missing the required ‘text’ field. Please ensure the payload is valid JSON and includes the ‘text’ key.”
```
