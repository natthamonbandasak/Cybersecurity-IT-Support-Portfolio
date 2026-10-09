import re
from collections import Counter

# define Regex pattern
ip_pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

# create list for store data
ip_list = []

# open access.log file in read mode
with open("access.log", "r") as file:

    for line in file:
        # use research for searching ip address in line
        match = re.search(ip_pattern, line)
        if match:
            # got text from group 1
            ip_address = match.group(1)
            ip_list.append(ip_address)

ip_counts = Counter(ip_list)

print("🚨 DDoS ALERT: High Frequency IP Addresses")
for ip, count in ip_counts.most_common():
    print(f"- IP {ip}: {count} requests")

import sqlite3
# create and connect database
conn = sqlite3.connect("ddos_alert.db")
cursor = conn.cursor()

# create table ip_traffic
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ip_traffic (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip_address TEXT,
        request_count INTEGER
    )

''')
# delete old data in case of execute many times
cursor.execute("DELETE FROM ip_traffic")

#loop data and execute it to db
for ip, count in ip_counts.items():
    cursor.execute("INSERT INTO ip_traffic (ip_address, request_count) VALUES (?, ?)", (ip, count))



# commit and disconnect
conn.commit()
conn.close()

print("\n DATA SAVED: Results successfully loaded into ddos_alert.db")




