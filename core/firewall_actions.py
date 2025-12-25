import os
from datetime import datetime

LOG_FILE = "logs/traffic.log"

def log_event(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

def block_ip(ip):
    os.system(f"iptables -A INPUT -s {ip} -j DROP")
    log_event(f"BLOCKED IP: {ip}")

def block_port(port):
    os.system(f"iptables -A INPUT -p tcp --dport {port} -j DROP")
    log_event(f"BLOCKED PORT: {port}")
