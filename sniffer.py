from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

packetCount = 0

def process_packet(packet):
    global packetCount

    if not packet.haslayer(IP):
        return

    packetCount += 1

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    if packet.haslayer(TCP):
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

    elif packet.haslayer(UDP):
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

    elif packet.haslayer(ICMP):
        protocol = "ICMP"
        src_port = "N/A"
        dst_port = "N/A"

    else:
        protocol = "OTHER"
        src_port = "N/A"
        dst_port = "N/A"

    payload = ""
    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode("utf-8", errors="replace")[:60]

    print(f"\n--- Packet #{packetCount} ---")
    print(f"  Protocol : {protocol}")
    print(f"  Source   : {src_ip}  Port: {src_port}")
    print(f"  Dest     : {dst_ip}  Port: {dst_port}")
    if payload:
        print(f"  Payload  : {payload}")


print("Sniffer started\n")

try:
    sniff(prn=process_packet, store=0)
except KeyboardInterrupt:
    print(f"\nStopped Total packets: {packetCount}")
