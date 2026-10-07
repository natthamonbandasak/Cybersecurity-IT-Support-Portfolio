# Automated Log Analysis & Threat Detection Pipeline

## 🎯 Objective
To automate the manual and time-consuming process of reviewing authentication logs, enabling security teams to rapidly identify brute-force attacks and proactively block malicious IP addresses.

## 📌 Project Overview
This project simulates a Junior SOC Analyst's daily task of monitoring and triaging server traffic. I built an automated data pipeline to parse over 5,000 server log entries, extract malicious SSH login attempts, and store the aggregated data in a database for rapid risk assessment.

## 🛠️ Technologies Used
* **Python:** Data extraction, log parsing, and automation (`collections.Counter`, `re`).
* **Database:** SQLite for lightweight, local data storage.
* **SQL:** Data aggregation queries (`GROUP BY`, `SUM()`, `ORDER BY`) to isolate and rank high-risk IPs.

## 🚀 How It Works
1. Reads the `auth.log` file containing simulated server authentication traffic.
2. Filters out suspicious activities by identifying "Failed password" log entries.
3. Extracts source IP addresses utilizing Regular Expressions (Regex).
4. Loads the aggregated attempt counts into a SQLite database.
5. Executes SQL queries to sort and flag IPs based on their total volume of failed login attempts.

## 💡 Business Impact & Value
* **Operational Efficiency:** Eliminates manual log reading, transforming thousands of raw text lines into actionable threat intelligence in seconds.
* **Proactive Defense:** Generates a prioritized list of highly suspicious IPs, ready to be exported for firewall blocklisting.
* **Data-Driven Security:** Demonstrates a complete end-to-end workflow (ETL) from raw data ingestion to structured data analysis.
