import json
import sys

class RuleEngine:
    def __init__(self, rule_file):
        try:
            with open(rule_file, "r") as f:
                self.rules = json.load(f)
        except json.JSONDecodeError as e:
            print(f"[ERROR] Invalid JSON format in {rule_file}")
            print(e)
            sys.exit(1)
        except FileNotFoundError:
            print(f"[ERROR] Rule file not found: {rule_file}")
            sys.exit(1)

    def is_ip_blocked(self, ip):
        return ip in self.rules.get("blocked_ips", [])

    def is_port_blocked(self, port):
        return port in self.rules.get("blocked_ports", [])

    def is_protocol_allowed(self, protocol):
        return protocol in self.rules.get("allowed_protocols", [])