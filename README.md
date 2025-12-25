# 🔐 Personal Firewall using Python (Kali Linux)

A lightweight **custom personal firewall** built using **Python, Scapy, and iptables** that monitors, analyzes, and filters incoming network traffic based on user-defined security rules.

This project is designed for **learning firewall internals, packet inspection, and SOC-level network security concepts**.

---

## 🎯 Project Objectives

- Monitor real-time network traffic
- Analyze packets (IP, Port, Protocol)
- Apply rule-based filtering
- Block malicious or unwanted traffic
- Log allowed and blocked packets
- Understand how firewalls work internally

---

## 🚀 Features

- ✅ Real-time packet sniffing
- ✅ IP-based traffic blocking
- ✅ Port-based filtering (e.g., Telnet, SMB)
- ✅ Protocol-level validation (TCP / UDP)
- ✅ iptables-based enforcement (real firewall rules)
- ✅ Traffic logging for auditing
- ✅ Simple JSON-based rule management
- ✅ Kali Linux compatible
- ✅ SOC / Cybersecurity interview ready

---

## 🛠️ Technologies Used

| Category | Tool |
|--------|------|
| Language | Python 3 |
| Packet Capture | Scapy |
| Firewall Engine | iptables |
| OS | Kali Linux |
| Rule Format | JSON |
| Logging | Text logs |

---

## 📁 Project Folder Structure

│
├── core/
│ ├── packet_sniffer.py # Captures and analyzes packets
│ ├── rule_engine.py # Loads and validates firewall rules
│ ├── firewall_actions.py # iptables actions + logging
│
├── rules/
│ └── firewall_rules.json # Firewall rules (IPs, ports, protocols)
│
├── logs/
│ └── traffic.log # Traffic activity logs
│
├── main.py
├── requirements.txt 
└── README.md 
### 1 Create Virtual Environment (MANDATORY)
```bash
python3 -m venv venv
source venv/bin/activate
### 2 Installation
pip install --upgrade pip
pip install -r requirements.txt
### 3 How to run
sudo su
source venv/bin/activate
python3 main.py
