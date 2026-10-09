# Botnet & DDoS Activity Detection

## 🎯 Objective
To proactively identify and mitigate Distributed Denial of Service (DDoS) attacks and botnet activity by automating the analysis of web server access logs to detect abnormal traffic spikes targeting critical authentication endpoints.

## 📌 Project Overview
This project simulates a SOC Analyst's response to an active Layer 7 DDoS attack. I developed an automated Python ETL pipeline to ingest simulated Apache/Nginx web server logs, parse out attacking IP addresses using Regular Expressions, and load the aggregated request data into a database. This workflow allows security teams to rapidly identify malicious botnet nodes and implement immediate IP blocking strategies.

## 🛠️ Technologies Used
- **Python:** Data extraction, log parsing, and ETL pipeline automation (`collections.Counter`, `re`, `sqlite3`).
- **Database:** SQLite for rapid local data ingestion and traffic aggregation.
- **SQL:** Queries to rank IP addresses by request volume and establish thresholds for anomalous behavior.

## 🚀 How It Works
1. Ingests simulated `access.log` files containing standard web server traffic (Combined Log Format).
2. Utilizes Regular Expressions (Regex) to extract client IP addresses from thousands of log entries.
3. Aggregates request frequencies using Python's `collections.Counter` to isolate high-volume traffic sources.
4. Loads the parsed data into an SQLite database (`ddos_alert.db`) via batch insertion for optimal performance and clean execution.
5. Executes SQL queries to flag IP addresses exceeding normal traffic thresholds, specifically pinpointing botnet nodes targeting the `/api/login` endpoint.

## 💡 Business Impact & Value
- **Threat Intelligence & Mitigation:** Rapidly identifies malicious infrastructure, enabling network and firewall teams to block attacking IPs before service degradation occurs.
- **High Availability:** Protects critical business assets (such as authentication APIs) from resource exhaustion and server downtime.
- **Automated Incident Response (IR):** Transforms raw, high-volume server logs into structured, actionable security alerts, drastically reducing manual log analysis time during a live cyberattack.
