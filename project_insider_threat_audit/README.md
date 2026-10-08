# Employee Offboarding & Insider Threat Audit

## 🎯 Objective
To automate the monitoring of internal system activities, specifically targeting the employee offboarding phase, to rapidly detect anomalous behavior and prevent intellectual property (IP) exfiltration before an employee's departure.

## 📌 Project Overview
This project simulates a SOC Analyst's responsibility of auditing user activities during the critical employee offboarding process. I developed an end-to-end automated Python data pipeline (ETL) to parse thousands of simulated internal audit logs, pinpoint unauthorized access to confidential files, and store the aggregated findings in a database to identify high-risk employees who might be stealing data before leaving the company.

## 🛠️ Technologies Used
- **Python:** Data extraction, log parsing, and end-to-end automation (`collections.Counter`, `re`, `sqlite3`).
- **Database:** SQLite for lightweight, local data storage and structured analysis.
- **SQL:** Data aggregation queries to isolate and rank employees based on anomalous download volumes.

## 🚀 How It Works
1. Reads the `audit.log` file containing simulated internal employee actions and system events.
2. Filters for highly suspicious activities by specifically identifying `"downloaded_confidential_file"` log entries.
3. Extracts the employee's username associated with the unauthorized action utilizing Regular Expressions (Regex).
4. Automatically loads the aggregated download counts per user directly into a SQLite database (`insider_threat.db`).
5. Executes SQL queries to flag and rank users with an abnormally high volume of confidential file downloads, preparing the data for HR and Security review prior to departure.

## 💡 Business Impact & Value
- **Cross-Departmental Security:** Bridges the gap between HR and IT Security by providing actionable intelligence during the offboarding process.
- **Data Loss Prevention (DLP):** Provides rapid visibility into potential intellectual property theft or data breaches originating from within the organization.
- **Operational Efficiency:** Eliminates manual compliance checks by automating the auditing of massive log files, transforming raw text into an actionable ETL pipeline.
