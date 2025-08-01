#
# Downloaded from: https://opbloody.github.io/riots-hub/
# Created by: BanRioT
#

import socket
import sys
import threading
from queue import Queue

print_lock = threading.Lock()

def scan_port(ip, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        with print_lock:
            if result == 0:
                print(f"[OPEN]   Port {port}")
                open_ports.append(port)
            else:
                print(f"[CLOSED] Port {port}")
        sock.close()
    except:
        pass

def threader(ip, port_range, max_threads=100):
    q = Queue()
    open_ports = []

    def worker():
        while True:
            port = q.get()
            scan_port(ip, port, open_ports)
            q.task_done()

    for _ in range(max_threads):
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    for port in range(port_range[0], port_range[1] + 1):
        q.put(port)

    q.join()

    if not open_ports:
        print("\n[-] No open ports found.")
    else:
        print("\n[+] Open ports found:")
        for port in sorted(open_ports):
            print(f"  - Port {port}")

def get_own_ip():
    return socket.gethostbyname(socket.gethostname())

def run_scan():
    print("=== PORT SCANNER ===")
    print("1. Scan your own IP")
    print("2. Enter custom IP or domain")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        target = get_own_ip()
    elif choice == "2":
        target = input("Enter IP address or domain: ").strip()
    else:
        print("[!] Invalid choice.")
        return

    start_port = input("Start port (default 1): ").strip()
    end_port = input("End port (default 1024): ").strip()

    try:
        start_port = int(start_port) if start_port else 1
        end_port = int(end_port) if end_port else 1024
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("[!] Invalid port range.")
        return

    print(f"\n[+] Scanning {target} from port {start_port} to {end_port}...\n")
    threader(target, (start_port, end_port))

def main():
    try:
        while True:
            run_scan()
            again = input("\nDo you want to run another scan? (y/n): ").strip().lower()
            if again != "y":
                print("Goodbye!")
                break
    except KeyboardInterrupt:
        print("\n[!] Scan cancelled.")
        sys.exit()

if __name__ == "__main__":
    main()
