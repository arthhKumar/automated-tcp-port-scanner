import socket
import sys
from datetime import datetime

# 1. Get the Target from the user
target_input = input("Enter the target IP address or Domain Name (e.g., 127.0.0.1): ")

try:
    # This translates a name like 'google.com' into an IP address like '142.250.190.46'
    target_ip = socket.gethostbyname(target_input)
except socket.gaierror:
    print("\n[!] Error: Could not resolve hostname. Exiting.")
    sys.exit()

# 2. Get the Port Range from the user
print(f"\n[*] Target Resolved to: {target_ip}")
try:
    start_port = int(input("Enter the STARTING port number (e.g., 1): "))
    end_port = int(input("Enter the ENDING port number (e.g., 100): "))
except ValueError:
    print("\n[!] Error: Please enter valid numbers for ports. Exiting.")
    sys.exit()

print("-" * 50)
print(f"Scanning Target: {target_ip}")
print(f"Time Started: {str(datetime.now())}")
print("-" * 50)

# 3. The Scanning Loop
try:
    for port in range(start_port, end_port + 1):
        # Create a digital socket (communication tool)
        # AF_INET means IPv4, SOCK_STREAM means TCP protocol
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Give up if the port doesn't answer in 1 second
        s.settimeout(1.0)
        
        # Try to connect to the IP and Port
        result = s.connect_ex((target_ip, port))
        
        # If result is 0, the connection was successful!
        if result == 0:
            print(f"[+] Port {port}: OPEN")
            
        # Close the connection when done
        s.close()

except KeyboardInterrupt:
    print("\n[!] Scan halted by user. Exiting.")
    sys.exit()

print("\n[*] Scan completed successfully!")