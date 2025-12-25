from scapy.all import sniff, IP, TCP, UDP
from core.firewall_actions import block_ip, block_port, log_event

def analyze_packet(packet, rule_engine):
    if IP in packet:
        src_ip = packet[IP].src
        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
            port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            port = packet[UDP].dport
        else:
            port = None

        if rule_engine.is_ip_blocked(src_ip):
            block_ip(src_ip)
            return

        if not rule_engine.is_protocol_allowed(protocol):
            log_event(f"DROPPED PROTOCOL: {protocol} from {src_ip}")
            return

        if port and rule_engine.is_port_blocked(port):
            block_port(port)
            return

        log_event(f"ALLOWED: {src_ip} {protocol} Port:{port}")

def start_sniffing(rule_engine):
    sniff(prn=lambda packet: analyze_packet(packet, rule_engine),
          store=False)
