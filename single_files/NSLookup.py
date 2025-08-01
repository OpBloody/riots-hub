#
# Downloaded from: https://opbloody.github.io/riots-hub/
# Created by: BanRioT
#

import socket
import sys

def nslookup(query):
    try:
        # Check if query is an IP address
        try:
            socket.inet_aton(query)
            # If valid IP, do reverse lookup
            hostname = socket.gethostbyaddr(query)[0]
            print(f"\n[+] Reverse lookup result for IP {query}:")
            print(f"    Hostname: {hostname}")
        except socket.error:
            # Otherwise, resolve hostname to IP
            ip = socket.gethostbyname(query)
            print(f"\n[+] Lookup result for hostname {query}:")
            print(f"    IP Address: {ip}")
    except socket.gaierror:
        print(f"\n[!] Could not resolve '{query}'. Please check the input.")

def main():
    print("=== NSLOOKUP TOOL ===")
    while True:
        query = input("\nEnter a hostname or IP address (or 'exit' to quit): ").strip()
        if query.lower() in ('exit', 'quit'):
            print("Goodbye!")
            break
        if query:
            nslookup(query)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Lookup cancelled.")
        sys.exit()
