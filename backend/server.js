// server.js
const express = require("express");
const path = require("path");
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static HTML page
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

// API endpoint
app.post("/api/process", (req, res) => {
  const { text, debug } = req.body || {};

  console.log("➡️  Incoming /api/process");
  console.log("   BODY:", req.body);
  console.log("   text:", text);
  console.log("   debug:", debug);

  // 💥 NEW: 504 Gateway Timeout simulation
  if (debug === "gateway_timeout") {
    console.log("   🕒 Simulating 504 Gateway Timeout (3s delay)...");
    return setTimeout(() => {
      return res.status(504).json({
        error:
          "Gateway Timeout: upstream server did not respond in time (debug forced error)",
      });
    }, 3000); // 3 seconds delay before sending the 504
  }

  // 💥 NEW: Slow API response but still 200 OK (~5s delay)
  if (debug === "slow_200") {
    console.log("   🐢 Simulating slow 200 OK response (5s delay)...");
    return setTimeout(() => {
      const reversed = String(text || "").split("").reverse().join("");
      return res.json({
        input: text,
        result: reversed,
        info: "Slow API response simulation (5s delay before response)",
      });
    }, 5000);
  }

  // 💥 NEW: High latency but still 200 OK (~2.5s delay)
  if (debug === "high_latency") {
    console.log("   🐌 Simulating high latency (2.5s delay)...");
    return setTimeout(() => {
      const reversed = String(text || "").split("").reverse().join("");
      return res.json({
        input: text,
        result: reversed,
        latencyInfo:
          "High latency simulation (2.5s delay before response)",
      });
    }, 2500);
  }

  // Existing debug error triggers
  const errors = {
    missing_text: [
      400,
      "Missing 'text' field in body (debug forced error)",
    ],
    invalid_api_key: [
      401,
      "Invalid or missing API key (debug forced error)",
    ],
    rate_limit: [
      429,
      "Too many requests — rate limit exceeded (debug forced error)",
    ],
    server_error: [
      500,
      "Internal server error (debug forced error)",
    ],
    forbidden: [
      403,
      "Forbidden: you do not have permission to perform this action (debug forced error)",
    ],
    not_found: [
      404,
      "Endpoint or resource not found (debug forced error)",
    ],
    request_timeout: [
      408,
      "Request Timeout: The server timed out waiting for the request (debug forced error)",
    ],
    conflict_error: [
      409,
      "Conflict: The request could not be completed due to a conflict with the current state (debug forced error)",
    ],
    unprocessable_entity: [
      422,
      "Unprocessable Entity: The server understands the content type but was unable to process the contained instructions (debug forced error)",
    ],
    payload_too_large: [
      413,
      "Payload Too Large: The request is larger than the server is willing or able to process (debug forced error)",
    ],
  };

  if (debug && errors[debug]) {
    const [code, message] = errors[debug];
    console.log(`   ✅ DEBUG branch hit → ${code}`);
    return res.status(code).json({ error: message });
  }

  // Natural validation
  if (!text) {
    console.log("   ⚠️ Natural validation 400 (no text, no debug)");
    return res.status(400).json({ error: "Missing 'text' field in body" });
  }

  // Normal success response
  const reversed = String(text).split("").reverse().join("");
  console.log("   ✅ Normal success 200");
  return res.json({
    input: text,
    result: reversed,
    info: "AI Support Lab successful processing",
  });
});

// Catch-all for unknown routes
app.use((req, res) => {
  res.status(404).json({ error: "Route not found" });
});

// Start server
app.listen(PORT, () => {
  console.log(`✅ AI Support Lab backend running on http://localhost:${PORT}`);
});
