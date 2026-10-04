Automated Log Analysis & Threat Detection Pipeline
Overview

The Automated Log Analysis & Threat Detection Pipeline is a cybersecurity project that simulates a real-world investigation performed by an IT Support Technician / Junior SOC Analyst.

The project focuses on analysing raw server authentication logs to identify suspicious login activity, extract potentially malicious source IP addresses, and generate a structured summary of potential threats.

The investigation uses a combination of Bash, Python, SQLite, SQL, and GitHub to demonstrate an end-to-end security log analysis workflow.

The project is designed to demonstrate practical skills in:

Linux command-line investigation

Log analysis

IP address extraction

Data validation

Python scripting

SQLite database management

SQL querying

Basic threat detection

Security investigation documentation

Git/GitHub version control

Scenario

A company has reported suspicious activity against one of its servers.

The IT/Security team suspects that an external user may be attempting to gain unauthorized access to the server.

As a Junior SOC Analyst, I have been asked to investigate the available raw log data and determine whether there is evidence of suspicious authentication activity.

The investigation will focus on identifying:

Repeated failed login attempts

Suspicious source IP addresses

High-frequency authentication attempts

Potential brute-force behaviour

Successful logins following repeated failures

Unusual activity patterns

The final objective is to identify potentially suspicious IP addresses and produce an evidence-based security investigation summary.

Important: An IP address appearing frequently in a log does not automatically mean that it belongs to an attacker. Findings in this project are based on observable log evidence and should be treated as indicators requiring further investigation.

Project Objectives

The main objectives of this project are:

Obtain a suitable sample authentication/server log.

Understand the structure and format of the log.

Use Bash to extract relevant security events.

Extract source IP addresses from suspicious events.

Use Python to validate and analyse the extracted data.

Count authentication attempts associated with each IP address.

Store the results in an SQLite database.

Use SQL queries to identify high-frequency activity.

Document the investigation process.

Present the project using GitHub.

Tools & Technologies
Tool	Purpose
Bash	Initial log filtering, searching, and extraction
Python	Data processing, validation, and automation
SQLite	Storing and querying analysed log data
SQL	Investigating suspicious activity in the database
Git/GitHub	Version control and project documentation
Project Architecture

The investigation follows this workflow:

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

Investigation Process
Step 1 — Obtain the Log Data

The first stage is to obtain a suitable sample log file.

Possible sources include publicly available sample:

SSH authentication logs

Linux authentication logs

Apache access logs

Web server logs

The selected dataset should contain enough information to investigate authentication or connection activity.

The original log file will be preserved as the source evidence for the investigation.

Expected Input
raw_logs/
└── auth.log

Step 2 — Understand the Log Format

Before writing any analysis scripts, I will manually inspect the log file to understand its structure.

I will identify fields such as:

Timestamp

Host/server

Event type

Username

Source IP address

Authentication result

Service/process

For example, an authentication log may contain information similar to:

Timestamp    Host    Event              User       Source IP
----------   -----   -----------------  ---------  ------------
...          server  Failed password     user1      192.0.2.10
...          server  Failed password     admin      192.0.2.10


The exact format will depend on the dataset selected for the project.

Understanding the format is important because the Bash and Python extraction logic will depend on the structure of the log.

Step 3 — Bash Log Extraction

The next stage is to use Bash to perform the initial investigation.

The Bash script will be called:

extract.sh


The purpose of the script is to:

Read the raw log.

Identify relevant security events.

Filter suspicious authentication attempts.

Extract source IP addresses.

Save the extracted information for further analysis.

Tools that may be used include:

grep
awk
sort
uniq
cut


The script should produce an intermediate file such as:

suspicious_ips.txt


The goal is not to build a complicated script.

Instead, the purpose is to demonstrate that I understand how to use Linux command-line tools to investigate security logs efficiently.

Step 4 — Python Analysis

After Bash extracts the relevant information, Python will be used for further analysis.

The Python script will be called:

analyzer.py


The Python analysis will:

Read the extracted data.

Validate the input.

Identify IP addresses.

Count the number of attempts associated with each IP.

Identify high-frequency activity.

Store the results in SQLite.

Python will allow the analysis to become more automated and repeatable.

A dictionary can be used to maintain a count for each IP address.

Conceptually:

IP Address       Attempts
-----------      --------
192.0.2.10       25
192.0.2.20       8
192.0.2.30       3


The actual implementation will be developed as part of the project.

Step 5 — Data Validation

Before storing the results, the Python script will perform basic validation.

Examples include checking whether:

An IP address exists

The extracted value has a valid IP format

Empty lines are ignored

Unexpected log entries are handled

Duplicate events are processed correctly

This stage demonstrates an important security/data-analysis principle:

Do not blindly trust extracted data.

The analysis should identify and handle malformed or unexpected input where possible.

Step 6 — SQLite Database

The analysed data will then be stored in an SQLite database.

The database will be called:

threat_alerts.db


A table can be designed to contain information such as:

logs
--------------------------------
id
ip_address
attempt_count
event_type
analysis_timestamp


The exact database design may be adjusted depending on the dataset and the information extracted during the investigation.

SQLite is useful for this project because it allows the extracted security data to be queried using SQL without requiring a separate database server.

Step 7 — SQL Threat Investigation

Once the data has been stored in SQLite, SQL queries will be used to investigate suspicious activity.

For example, the investigation can ask:

Which IP addresses generated the most failed attempts?

Which IP addresses exceeded a defined threshold?

Which IP addresses were associated with multiple events?

How frequently did suspicious activity occur?

A basic investigation query could identify IP addresses with more than a selected number of attempts.

The threshold will be treated as an investigation rule, not automatic proof that an IP address is malicious.

For example:

High number of failed attempts
            +
Repeated activity
            +
Relevant authentication events
            =
Potentially suspicious activity


Further investigation would be required before declaring an IP address malicious.

Step 8 — Threat Detection Logic

The project will use simple rule-based detection rather than attempting to build a machine-learning system.

Example Detection Logic
IF failed_attempts > threshold
THEN generate investigation alert


Additional rules may be introduced as the project develops.

For example:

Multiple failed attempts
        +
Short time period
        +
Same source IP
        =
Potential brute-force activity


These rules are intended to demonstrate basic SOC detection concepts.

Step 9 — Investigation Results

The final analysis should produce a summary similar to:

IP Address       Failed Attempts       Status
-----------      ---------------       ----------------
192.0.2.10       35                    Investigate
192.0.2.20       18                    Investigate
192.0.2.30       4                     Low activity


Note: The IP addresses and numbers above are examples only. Actual results will be added after analysing the selected dataset.

These results will then be reviewed alongside the original log entries.

The purpose is to ensure that the automated output can be traced back to actual log evidence.

Step 10 — Incident Report

The final stage is to document the investigation.

The report will contain:

Executive Summary

A short explanation of the incident and the investigation outcome.

Investigation Scope

What logs and systems were analysed.

Methodology

How Bash, Python, SQLite, and SQL were used.

Evidence

Relevant log entries and analysis results.

IP Address Analysis

Details of suspicious source IP addresses and their activity.

Timeline

Important events in chronological order.

Findings

What the investigation discovered.

Risk Assessment

An assessment of the potential significance of the activity.

Recommendations

Suggested defensive actions and further investigation.

Conclusion

A final summary of the investigation.

Project Structure

The GitHub repository will be organised approximately as follows:

automated-log-analysis/
│
├── README.md
│
├── data/
│   └── auth.log
│
├── scripts/
│   ├── extract.sh
│   └── analyzer.py
│
├── database/
│   └── threat_alerts.db
│
├── sql/
│   └── queries.sql
│
├── reports/
│   └── incident-report.md
│
└── screenshots/
    └── investigation-results.png


The exact structure may change as the project develops.

Example Investigation Questions

During the investigation, I will attempt to answer questions such as:

How many authentication failures occurred?

Which IP address generated the most failures?

Which accounts were targeted?

Were multiple accounts targeted from the same IP?

Did any successful login occur after repeated failures?

Were suspicious events concentrated within a short time period?

Which IP addresses should be investigated further?

What evidence supports the conclusion?

What security controls could reduce the risk of similar activity?

Security Considerations

This project is designed for defensive security analysis and education.

The investigation focuses on analysing log data and identifying indicators of potentially malicious activity.

IP addresses found in logs will not automatically be classified as attackers.

An IP address may belong to:

A legitimate user

A corporate system

A VPN

A proxy

A security scanner

An automated service

A potentially compromised system

An actual attacker

Therefore, conclusions will be based on the available evidence.

Limitations

This project is a simplified SOC investigation and does not represent a complete enterprise security monitoring platform.

Limitations include:

Sample log data may not represent a real production environment.

IP reputation is not sufficient by itself to confirm malicious activity.

The detection rules are relatively simple.

No SIEM platform is used.

No real-time monitoring is implemented.

No machine-learning detection is implemented.

The analysis depends on the quality and completeness of the log data.

These limitations provide opportunities for future improvements.

Future Improvements

Possible future improvements include:

Add additional log sources.

Analyse authentication success and failure together.

Add timestamp-based detection rules.

Detect multiple usernames targeted by one IP.

Add configurable detection thresholds.

Generate automated reports.

Export results as CSV or JSON.

Add IP reputation enrichment.

Add visualisations.

Add automated testing.

Integrate with a SIEM platform.

Implement real-time log monitoring.

Skills Demonstrated

This project demonstrates practical experience with:

Linux / Bash

Command-line navigation

Log filtering

grep

awk

sort

uniq

Shell scripting

Python

File handling

Dictionaries

Loops

Functions

Data validation

IP address processing

SQLite integration

Basic automation

SQL / SQLite

Database creation

Table design

Data insertion

SELECT

WHERE

ORDER BY

Aggregation

Basic threat-oriented queries

Cybersecurity

Security log analysis

Authentication monitoring

Indicator identification

IP address analysis

Brute-force detection concepts

Incident investigation

Evidence-based reporting

Git/GitHub

Repository management

Version control

Documentation

Project presentation

Conclusion

The Automated Log Analysis & Threat Detection Pipeline demonstrates an end-to-end approach to investigating suspicious server activity.

Starting with raw log data, the project uses Bash for extraction, Python for analysis and automation, SQLite for structured data storage, and SQL for threat investigation.

The final results are documented and presented through GitHub, demonstrating not only technical skills but also the ability to communicate a security investigation clearly.

This project is intended to demonstrate the practical workflow of a Junior SOC Analyst:

Raw Logs
   ↓
Extract
   ↓
Validate
   ↓
Analyse
   ↓
Store
   ↓
Query
   ↓
Investigate
   ↓
Report

Disclaimer

This project is intended for educational and defensive cybersecurity purposes.

All log data used should be publicly available sample data or data that I have permission to analyse.

No unauthorized access, exploitation, or attack activity is performed as part of this project.
