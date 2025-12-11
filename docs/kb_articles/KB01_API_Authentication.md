
# API Authentication Guide

API authentication ensures every request is tied to an authorized user or application. 
Most modern APIs use API keys passed through request headers.

---

## Why Authentication Fails

Common causes:
- Missing API key header
- Misspelled header name (capitalization matters)
- Expired or invalid API key
- Extra spaces or hidden characters
- Sending the key in the query string instead of headers

---

## Correct Header Example

Authorization: Bearer YOUR_API_KEY  
Content-Type: application/json

---

## Incorrect Examples

Auth: KEY  
authorization: apikey  
(no Authorization header at all)

---

## How to Fix

- Verify the header name is exactly: Authorization
- Remove extra spaces around the key
- Ensure the key is active in your dashboard
- Avoid sending API calls directly from the browser (CORS issues)
- Use backend code for secure API requests

---
