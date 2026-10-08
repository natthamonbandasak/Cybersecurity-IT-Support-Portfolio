# Insider Threat Detection & Audit Log Analysis

## 🎯 Objective
To automate the monitoring of internal system activities, enabling security teams to rapidly detect anomalous employee behavior, mitigate insider threats, and prevent potential data exfiltration.

## 📌 Project Overview
This project simulates a SOC Analyst's responsibility of auditing internal user activities for data loss prevention (DLP). I developed an end-to-end automated Python data pipeline (ETL) to parse thousands of simulated internal audit logs, pinpoint unauthorized access to confidential files, and store the aggregated findings in a database to identify high-risk users.

## 🛠️ Technologies Used
- **Python:** Data extraction, log parsing, and end-to-end automation (`collections.Counter`, `re`, `sqlite3`).
- **Database:** SQLite for lightweight, local data storage and structured analysis.
- **SQL:** Data aggregation queries to isolate and rank employees based on anomalous download volumes.

## 🚀 How It Works
1. Reads the `audit.log` file containing simulated internal employee actions and system events.
2. Filters for highly suspicious activities by specifically identifying `"downloaded_confidential_file"` log entries.
3. Extracts the employee's username associated with the unauthorized action utilizing Regular Expressions (Regex).
4. Automatically loads the aggregated download counts per user directly into a SQLite database (`insider_threat.db`).
5. Executes SQL queries to flag and rank users with an abnormally high volume of confidential file downloads for further investigation.

## 💡 Business Impact & Value
- **Data Loss Prevention (DLP):** Provides rapid visibility into potential intellectual property theft or data breaches originating from within the organization.
- **Operational Efficiency:** Eliminates manual compliance checks by automating the auditing of massive log files, transforming raw text into actionable intelligence.
- **Streamlined Security Audits:** Delivers a complete, queryable database (ETL pipeline) that allows HR and Security teams to seamlessly investigate employee misconduct.
