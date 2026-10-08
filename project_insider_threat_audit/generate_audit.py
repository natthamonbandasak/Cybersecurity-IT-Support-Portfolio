# 1. to random data
import random
from datetime import datetime, timedelta

# 2. prepare primary data (change person name as you prefer)
employees = ["jungkook", "namjoon", "jimin", "yoonki", "jin", "karina", "nicole", "jane", "james", "suspect66", "jackson", "felix", "lisa", "jennie", "jisoo", "kevin", "william", "diana", "rebecca", "thomas", "emily", "sarah", "henry", "alex", "lily", "chloe", "matilda", "willow", "margaret", "laura", "luca", "antonio", "elisabetta", "julie", "francesca"]
actions = ["logged_in", "read_email", "downloaded_confidential_file", "failed_login", "deleted_database", "logged_out", "update_profile", "password_changed", "accessed_shared_drive"]

# 3. open new file name audit.log for write
with open("audit.log", "w") as file:

    # processing data 5000 times
    for _ in range(5000):
        time_offset = timedelta(minutes=random.randint(1, 10000))
        time_str = (datetime.now() - time_offset).strftime("%Y-%m-%d %H:%M:%S")
        user = random.choice(employees)
        action = random.choice(actions)

        file.write(f"[{time_str}] User: {user} | Action: {action}\n")

print("Generated 5000 lines successfully!")


