# import tool (Regex for cut word, Counter for counting data)
import re
from collections import Counter

# create list for store suspicious user
suspicious_users = []

# open audit.log file in read mode
with open("audit.log", "r") as file:

    # to read line in line
    for line in file:
        # check the condition
        if "downloaded_confidential_file" in line:
            # use Regex to get a name after user:
            match = re.search(r"User:\s+(\w+)", line)
            if match:
                user = match.group(1)
                suspicious_users.append(user)

# count
user_counts = Counter(suspicious_users)

# print the result
print("\n INSIDER THREAT REPORT: Confidential File Downloads")
for user, count in user_counts.most_common():
    print(f"- User '{user}' downloaded the file {count} time(s)")

import sqlite3
# create and connect database
conn = sqlite3.connect("insider_threat.db")
cursor = conn.cursor()

# create table "audit_results" (username column is TEXT and download_count is INTEGER)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS audit_results (
        username TEXT,
        download_count INTEGER
    )
''')

# delete old data in case of execute many times
cursor.execute("DELETE FROM audit_results")

# Loop data and add it into database
for user, count in user_counts.items():
    cursor.execute("INSERT INTO audit_results (username, download_count) VALUES (?, ?)", (user, count))

# commit and disconnect
conn.commit()
conn.close()

print("\n DATA SAVED: Results successfully loaded into insider_threat.db")

