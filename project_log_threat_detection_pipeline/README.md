# Automated Log Analysis & Threat Detection Pipeline

## Overview
The Automated Log Analysis & Threat Detection Pipeline is a cybersecurity project that simulates a real-world investigation performed by an IT Support Technician / Junior SOC Analyst.

The project focuses on analysing raw server authentication logs to identify suspicious login activity, extract potentially malicious source IP addresses, and generate a structured summary of potential threats. The investigation uses a combination of Bash, Python, SQLite, SQL, and GitHub to demonstrate an end-to-end security log analysis workflow.

The project is designed to demonstrate practical skills in:
* Linux command-line investigation
* Log analysis
* IP address extraction
* Data validation
* Python scripting
* SQLite database management
* SQL querying
* Basic threat detection
* Security investigation documentation
* Git/GitHub version control

## Scenario
A company has reported suspicious activity against one of its servers. The IT/Security team suspects that an external user may be attempting to gain unauthorized access to the server.

As a Junior SOC Analyst, I have been asked to investigate the available raw log data and determine whether there is evidence of suspicious authentication activity. The investigation will focus on identifying:
* Repeated failed login attempts
* Suspicious source IP addresses
* High-frequency authentication attempts
* Potential brute-force behaviour
* Successful logins following repeated failures
* Unusual activity patterns

The final objective is to identify potentially suspicious IP addresses and produce an evidence-based security investigation summary.

> **Important:** An IP address appearing frequently in a log does not automatically mean that it belongs to an attacker. Findings in this project are based on observable log evidence and should be treated as indicators requiring further investigation.

## Project Objectives
The main objectives of this project are:
1. Obtain a suitable sample authentication/server log.
2. Understand the structure and format of the log.
3. Use Bash to extract relevant security events.
4. Extract source IP addresses from suspicious events.
5. Use Python to validate and analyse the extracted data.
6. Count authentication attempts associated with each IP address.
7. Store the results in an SQLite database.
8. Use SQL queries to identify high-frequency activity.
9. Document the investigation process.
10. Present the project using GitHub.

## Tools & Technologies

| Tool | Purpose |
| :--- | :--- |
| **Bash** | Initial log filtering, searching, and extraction |
| **Python** | Data processing, validation, and automation |
| **SQLite** | Storing and querying analysed log data |
| **SQL** | Investigating suspicious activity in the database |
| **Git/GitHub** | Version control and project documentation |

## Project Architecture
The investigation follows this workflow:

```text
                 Raw Log File
                      |
                      v
              +---------------+
              |     Bash      |
              |   Extraction  |
              +---------------+
                      |
                      v
            suspicious_ips.txt
                      |
                      v
              +---------------+
              |    Python     |
              |    Analysis   |
              +---------------+
                      |
                      v
              +---------------+
              |    SQLite     |
              |    Database   |
              +---------------+
                      |
                      v
              +---------------+
              |   SQL Query   |
              | Threat Search |
              +---------------+
                      |
                      v
             Suspicious Activity
                      |
                      v
             Investigation Report

