# 🕵️ Basic Network Sniffer

A simple Python network sniffer that captures and analyzes live packets using Scapy
---

## 📋 Features

- Captures live packets from the network interface
- Identifies protocol type: TCP, UDP, ICMP
- Displays source and destination IP addresses
- Shows source and destination ports (where applicable)
- Previews packet payload data (if available)
- Counts total packets captured per session

---

## 🛠️ Requirements

- Python 3.x
- Scapy library
- **Windows:** [Npcap](https://npcap.com/#download) — install with *WinPcap API-compatible Mode* checked
- **Linux:** `sudo apt-get install libpcap-dev`

---

## 📦 Installation

```bash
pip install scapy
```

---

## ▶️ Usage

**Linux / macOS:**
```bash
sudo python3 sniffer.py
```

**Windows:**
Run your terminal or IDE as **Administrator**, then:
```bash
python sniffer.py
```

---

## 📺 Example Output

```
Sniffer started... Press Ctrl+C to stop

--- Packet #1 ---
  Protocol : TCP
  Source   : 192.168.1.105  Port: 54621
  Dest     : 142.250.185.46  Port: 443

--- Packet #2 ---
  Protocol : UDP
  Source   : 192.168.1.105  Port: 51302
  Dest     : 8.8.8.8  Port: 53

--- Packet #3 ---
  Protocol : ICMP
  Source   : 192.168.1.105  Port: N/A
  Dest     : 8.8.8.8  Port: N/A

Stopped. Total packets: 3
```

---

## 🗂️ Project Structure

```
Basic-Network-Sniffer/
│
├── sniffer.py       # Main sniffer script
└── README.md        # Project documentation
```

---

## ⚙️ How It Works

1. `sniff()` opens the network interface and listens for all incoming/outgoing packets
2. Each packet is passed to `process_packet()` as a callback
3. Non-IP packets (e.g. ARP) are filtered out immediately
4. The IP layer is parsed to extract source and destination addresses
5. The transport layer (TCP/UDP/ICMP) is identified and ports are extracted
6. The Raw layer is read and decoded as UTF-8 text if a payload exists
7. All information is printed in a clean, readable format

---

## ⚠️ Legal & Ethical Notice

This tool is intended **strictly for educational purposes**.
Unauthorized packet sniffing is illegal in most jurisdictions.
Always ensure you have explicit permission before monitoring any network.

---

## 🧰 Built With

- [Python 3](https://www.python.org/)
- [Scapy](https://scapy.net/)

---

## 👨‍💻 Author

**Abdelrhman Mostafa**

