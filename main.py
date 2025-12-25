from core.rule_engine import RuleEngine
from core.packet_sniffer import start_sniffing

def main():
    print("🔐 Personal Firewall Started...")
    rule_engine = RuleEngine("rules/firewall_rules.json")
    start_sniffing(rule_engine)

if __name__ == "__main__":
    main()
