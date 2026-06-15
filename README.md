# Automated TCP Port Scanner

## 📌 Project Overview
This is a lightweight network reconnaissance tool built from scratch in Python using the core `socket` library. The application allows a user to input a target domain name or IPv4 address alongside a custom port scope, automatically mapping out which network gateways are actively listening for connections.

I built this project to master the low-level fundamentals of network communication, socket logic, and error handling before moving on to advanced cybersecurity frameworks.

## 🛡️ Cybersecurity Context: The Reconnaissance Phase
In professional security operations, a port scanner is a fundamental utility used during the **Information Gathering (Reconnaissance) Phase**. Before an analyst can patch a network—or before an audit can begin—they must map the target system. 

Finding an **open port** tells a security professional exactly what software services are running on a machine. By mapping these gateways, we can discover unauthorized entry points or outdated, vulnerable services that require immediate mitigation.

## ⚙️ How the Engine Works (The TCP 3-Way Handshake)
The core architecture relies on a sequential execution loop utilizing standard **TCP Connect Scanning**. When checking a port, the script initiates a standard network handshake:

1. **SYN (Synchronize):** The script sends a connection request packet to the target IP and port via `socket.connect_ex()`.
2. **SYN-ACK (Acknowledgment):** If the gateway is **OPEN**, the target machine replies positively. The internal function intercepts this, registers a success code (`0`), and outputs the port status to the console.
3. **RST (Reset):** If the gateway is **CLOSED**, the target replies with a reset packet. The function registers an error code and skips the port cleanly.

## 🛠️ Core Features & Logic
* **Dynamic Hostname Resolution:** Utilizes `socket.gethostbyname()` to seamlessly map standard alphanumeric web domains (e.g., `google.com`) into raw numerical IPv4 addresses.
* **Range Optimization Feature:** Implements a user-defined scope input mechanism, allowing targeted scanning of specific subsets (e.g., standard web ports 80 to 443) rather than forcing a slow scan of all 65,535 channels.
* **Fault-Tolerant Exception Handling:** * Implements a strict `s.settimeout(1.0)` threshold to bypass firewalls that drop packets silently, preventing application hanging.
  * Captures invalid domains (`socket.gaierror`) and non-integer inputs (`ValueError`) to exit gracefully without system crashes.
  * Features `KeyboardInterrupt` interception to allow clean manual termination (`Ctrl + C`).

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on the host machine.

### Execution
1. Clone this repository or download the source script.
2. Open your terminal/command prompt inside the project folder and execute:
   ```bash
   python port_scanner.py
