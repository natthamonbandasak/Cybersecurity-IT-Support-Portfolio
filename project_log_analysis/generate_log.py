import random
from datetime import datetime, timedelta

# insert data num
num_lines = 5000
output_file = "auth.log"

# generate User และ IP Address
users = ["root", "admin", "pi", "ubuntu", "test", "user_bob"]
normal_ips = ["192.168.1.50", "10.0.0.15", "172.16.0.5"]
attacker_ips = ["203.0.113.45", "198.51.100.22", "45.33.32.156", "185.199.108.153"]

start_time = datetime(2026, 10, 6, 8, 0, 0)

with open(output_file, "w") as f:
    current_time = start_time
    for _ in range(num_lines):
        # set timer 1-15 sec
        current_time += timedelta(seconds=random.randint(1, 15))
        timestamp = current_time.strftime("%b %d %H:%M:%S")
        pid = random.randint(10000, 20000)
        port = random.randint(30000, 60000)

        # random login 80% (Failed) and 20% (Accepted)
        if random.random() < 0.8:
            ip = random.choice(attacker_ips)
            user = random.choice(users)
            msg = f"Failed password for {user} from {ip} port {port} ssh2"
        else:
            ip = random.choice(normal_ips)
            user = "admin" if ip == "192.168.1.50" else "user_bob"
            msg = f"Accepted publickey for {user} from {ip} port {port} ssh2"

        f.write(f"{timestamp} server-01 sshd[{pid}]: {msg}\n")

print(f"✅ Generated {output_file} with {num_lines} lines successfully!")