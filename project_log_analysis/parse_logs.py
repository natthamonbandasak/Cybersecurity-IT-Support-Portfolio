import sqlite3
import re
from collections import Counter

def process_logs_and_store() :
    print("--- 1. Reading Log File ---")
    #log file that generated name auth.txt
    with open("auth.log", "r") as file:
        log = file.readlines()
    print(f"...Successfully read the file! Total lines: {len(log)}")

    print("--- 2. Parsing Data with Python ---")
    #filter the data only IP address that login but got Error (ex. 403 or 404 or failed)
    suspicious_ips = []
    for line in log:
        if "Failed password" in line:
            #use Regex to get IP address
            match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if match:
                suspicious_ips.append(match.group())
    print(f"!!!Found {len(suspicious_ips)} failed login attempts.")
    if len(suspicious_ips) == 0:
        print("!!! No suspicious IPs found. (Please check if the correct file is loaded)!!!")
        return

    #count the login
    ip_counts = Counter(suspicious_ips)

    print("--- 3. Storing into SQLite Database ---")
    conn = sqlite3.connect("threat_intel.db")
    cursor = conn.cursor()

    #create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS failed_access (
        ip_address TEXT,
        attempts INTEGER
        )
    ''')
    cursor.execute("DELETE FROM failed_access") #delete old data before new execute

    # store counts num into database
    for ip, count in ip_counts.items() :
        cursor.execute("INSERT INTO failed_access (ip_address, attempts) VALUES (?, ?)", (ip, count))

    conn.commit()

    print("--- 4. SQL Data Aggregation & Grouping ---")
    # querires for searching attack more than 20 times (the number could change)
    cursor.execute('''
        SELECT ip_address, SUM(attempts)
        FROM failed_access
        GROUP BY ip_address
        ORDER BY SUM(attempts) DESC
    ''')

    print("!!! High-Risk IPs Detected:")
    for row in cursor.fetchall():
        print(f"IP: {row[0]} | Blocked Attempts: {row[1]}")

    conn.close()
if __name__ == "__main__":   
    process_logs_and_store()

