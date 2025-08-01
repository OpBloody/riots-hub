#
# Downloaded from: https://opbloody.github.io/riots-hub/
# Created by: BanRioT
#

import socket
import sys

try:
    import dns.resolver
except ImportError:
    print("[!] 'dnspython' is required. Run: pip install dnspython")
    sys.exit()

def resolve_domain(domain):
    print(f"\n[+] DNS Records for: {domain}\n")

    # A record (IPv4)
    try:
        ip = socket.gethostbyname(domain)
        print(f"[A]     {ip}")
    except:
        print("[A]     Not found")

    # AAAA record (IPv6)
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        for rdata in answers:
            print(f"[AAAA]  {rdata.address}")
    except:
        print("[AAAA]  Not found")

    # CNAME record
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        for rdata in answers:
            print(f"[CNAME] {rdata.target}")
    except:
        print("[CNAME] Not found")

    # MX record
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        for rdata in answers:
            print(f"[MX]    {rdata.exchange} (priority {rdata.preference})")
    except:
        print("[MX]    Not found")

    # NS record
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        for rdata in answers:
            print(f"[NS]    {rdata.target}")
    except:
        print("[NS]    Not found")

def get_own_hostname():
    return socket.gethostname()

def main():
    print("=== DNS LOOKUP TOOL ===")
    print("1. Lookup your own hostname")
    print("2. Enter custom domain")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        domain = get_own_hostname()
    elif choice == "2":
        domain = input("Enter domain (e.g. example.com): ").strip()
    else:
        print("[!] Invalid choice.")
        return

    resolve_domain(domain)

    again = input("\nDo you want to perform another lookup? (y/n): ").strip().lower()
    if again == "y":
        main()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Lookup cancelled.")
