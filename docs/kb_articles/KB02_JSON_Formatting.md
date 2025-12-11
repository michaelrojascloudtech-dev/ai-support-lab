
# Proper JSON Formatting for API Requests

APIs expect valid JSON. If JSON is malformed, the server cannot parse the request.

---

## Common JSON Mistakes

- Missing quotes around keys
- Using single quotes instead of double quotes
- Forgetting commas
- Sending a JavaScript object without converting to JSON

---

## Correct JSON Example

{
  "text": "Hello world"
}

---

## Incorrect JSON Examples

{text: Hello}  
{'text': 'Hello'}

---

## Tips to Avoid JSON Errors

- Always use double quotes
- Set Content-Type: application/json
- Use JSON.stringify() in frontend JavaScript
- Validate JSON in VS Code or online formatters

---
