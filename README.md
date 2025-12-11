
API / SaaS Support Engineer Lab & Portfolio Project

This project is a complete end-to-end technical troubleshooting lab designed to demonstrate real-world skills required for roles such as Technical Support Engineer, API Support Engineer, Technical Customer Support (API-focused), and SaaS Support Specialist.

It simulates the daily workflows of debugging APIs, analyzing logs, investigating customer-reported issues, documenting findings, using SQL and Python for diagnostics, and delivering clear, actionable resolutions.

--------------------------------------------------------------------------
1. Project Objectives

This lab was built to demonstrate capability in:

- Troubleshooting APIs: headers, payloads, authentication, CORS, rate limits, timeouts
- Reproducing customer issues and validating expected behavior
- Analyzing structured logs in CSV, JSON, and SQL
- Writing clear internal and customer-facing technical documentation
- Automating diagnostics using Python requests, parsing, and error handling
- Understanding latency, timeouts, rate limits, authentication, and CORS
- Using Postman and browser DevTools for debugging
- Providing structured customer communication and root-cause explanations
- Knowing when and how to escalate issues
- Documenting issues in a professional ticket format (T01–T13)
- Applying escalation criteria and structured support workflows

--------------------------------------------------------------------------

2. Project Structure

api-saas-support-lab/
│
├── backend/                 # Node/Express simulated API server
├── frontend/                # Simple UI for sending test requests
├── automation/              # Python automation scripts
│   ├── load_test.py
│   ├── parse_logs.py
│   ├── analyze_logs.py
│   └── examples_try_except/
│
├── logs/
│   ├── api_logs.csv
│   ├── api_logs.json
│   └── api_lab.db          # SQLite database
│
├── queries.sql              # SQL analytics queries
│
├── kb_articles/             # Knowledge base documentation
│   ├── authentication_guide.md
│   ├── json_formatting.md
│   ├── http_errors_explained.md
│   ├── cors_troubleshooting.md
│   ├── latency_timeouts.md
│   └── escalation_criteria.md
│
├── tickets/                 # Real troubleshooting tickets T01–T13
│   ├── T01-missing-text.md
│   ├── T02-invalid-api-key.md
│   ├── ...
│   └── T13-slow-200.md
│
├── screenshots/             # All indexed screenshots per ticket
│   ├── T01/
│   ├── T02/
│   ├── ...
│   └── T13/
│
└── README.md                # This file

--------------------------------------------------------------------------

3. Python Automation Pack

The automation folder includes tools commonly used in SaaS Support roles:

• load_test.py – measures request latency and calculates min/avg/max
• parse_logs.py – reads CSV and JSON logs, extracts status, latency, and endpoint data
• analyze_logs.py – prints aggregated error rates and performance metrics
• try/except examples – demonstrates error handling for network and JSON failures

These scripts replicate internal diagnostic tooling used for log review and automated troubleshooting.

--------------------------------------------------------------------------

4. Knowledge Base Articles

Includes professionally written documentation:

• Authentication Guide
• JSON Formatting Guide
• HTTP Errors Explained
• CORS Troubleshooting Guide
• Latency & Timeout Behavior
• Escalation Criteria

Each article is structured to reflect support documentation used in SaaS engineering teams.

--------------------------------------------------------------------------

5. API Troubleshooting Tickets (T01–T13)

Every ticket includes:

• Customer problem description
• Reproduction steps
• Indexed screenshots
• Expected vs actual behavior
• Root cause analysis
• Customer-facing guidance

Scenarios covered include missing parameters, invalid API keys, CORS errors, rate limits, timeouts, backend failures, slow responses, and more.
This demonstrates structured problem investigation similar to real support workflows.

--------------------------------------------------------------------------

6. Postman Troubleshooting Practice

Demonstrates proficiency in:

• Sending structured API requests
• Triggering controlled error scenarios
• Inspecting headers, cookies, payloads, and timing
• Using Postman Console for debugging
• Validating and formatting JSON requests

--------------------------------------------------------------------------

7. Logs & Analytics Pack

The logs folder contains real example log files:

• api_logs.csv
• api_logs.json
• api_lab.db (SQLite)

The api_logs table includes 20 rows capturing endpoint, status code, latency, region, and timestamp.
Queries in queries.sql allow:

• Average latency analysis
• Status code distribution
• Endpoint-level error patterns
• Regional performance comparisons

analyze_logs.py provides automated insights using the same log dataset.

--------------------------------------------------------------------------

8. How to Run the Project

Backend:

1. Navigate to backend folder
2. Run npm install
3. Start server with node server.js
The server listens on localhost:3000.

Python tools:

Navigate to automation folder and run:
python load_test.py
python parse_logs.py
python analyze_logs.py

SQL:

Open SQLite and load queries with:
sqlite3 logs/api_lab.db
.read queries.sql

--------------------------------------------------------------------------

9. Skills Demonstrated

• API troubleshooting and debugging
• Clear customer communication
• JSON validation and formatting
• Authentication and headers analysis
• CORS investigation
• Latency and timeout diagnosis
• Python scripting for automation
• Log review (CSV, JSON, SQL)
• SQL analytics
• Postman and DevTools proficiency
• Ticket handling and structured reporting
• Knowledge base documentation writing

--------------------------------------------------------------------------

10. Purpose of This Project

The project was created to serve as a practical portfolio demonstrating readiness for API-centric SaaS Technical Support roles.
It mirrors real workflows used by engineering-support teams and shows proven capability in both technical troubleshooting and communication.

--------------------------------------------------------------------------

11. Transparency Statement / Note on Project Creation

This lab was created through a combination of my own hands-on work and AI-assisted guidance.
AI was used as a mentor-style learning aid, not as a generator of finished work.
Every script, test, ticket, log analysis, and troubleshooting step was executed, practiced, and validated by me personally.
I do not claim advanced professional experience in these areas; this project exists to demonstrate my commitment to learning, improving, and building the practical skills needed for API Support and SaaS Technical Support roles.
--------------------------------------------------------------------------

12. Contact

Michael Rojas
michaelrojas.cloudtech@gmail.com

--------------------------------------------------------------------------



--------------------------------------------------------------------------


--------------------------------------------------------------------------


--------------------------------------------------------------------------


--------------------------------------------------------------------------


--------------------------------------------------------------------------


--------------------------------------------------------------------------


--------------------------------------------------------------------------
