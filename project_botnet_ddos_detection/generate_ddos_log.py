# 1. random data
import random

# 2. prepare data DDoS Attack Node
normal_ips = ["192.168.1.15", "192.168.1.42", "192.168.1.88", "192.168.1.105", "10.10.4.12", "10.10.4.55", "10.20.1.101", "10.50.3.77",
    "172.16.12.4", "172.16.15.89", "172.16.20.140", "203.0.113.10", "203.0.113.44", "203.0.113.88"]
attacker_ips = ["185.220.101.5", "185.220.101.7", "194.26.29.112", "45.154.255.89"]

endpoints = ["/home", "/about", "/contact", "/products", "/images/banner.png", "/css/style.css"]
ddos_target = "/api/login" #spam request...

# 3. open new file name access.log for write
with open ("access.log", "w") as file:

    # mock data 5000 items
    for i in range(5000):
    # DDoS traffic 75% and normal ips 25%
        is_attacker = random.choices([True, False], weights =[75, 25])[0]
        if is_attacker:
            # random DDoS botnet
            ip = random.choice(attacker_ips)
            endpoint = ddos_target
        else:
            # random normal ips
            ip = random.choice(normal_ips)
            endpoint = random.choice(endpoints)

        timestamp = "08/Oct/2026:08:08:08 +200"
        status_code = 200
        bytes_sent = 4520
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"    
        # log line format

        log_line = f'{ip} - - [{timestamp}] "GET {endpoint} HTTP/1.1" {status_code} {bytes_sent} "https://example.com" "{user_agent}"\n'            
        
        # record data into file
        
        file.write(log_line)

print("Generated Full Apache&/Nginx DDoS Traffic 5,000 lines successfully!")








