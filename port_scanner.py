import socket
import sys

if len(sys.argv) != 4:
    print("Usage: python debug_scanner.py <target> <start_port> <end_port>")
    sys.exit()

target = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

print(f"Scanning {target_ip} from port {start_port} to {end_port}")
print("-" * 30)

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target_ip, port))

    print(f"Port {port} -> return code: {result}")

    if result == 0:
        print(f"[+] Port {port} is OPEN")

    sock.close()

print("Done.")

