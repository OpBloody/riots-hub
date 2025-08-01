import requests

def ip_lookup(ip=None):
    url = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        print(f"\n{'='*40}")
        print(f"IP Address:   {data.get('ip', 'N/A')}")
        print(f"Hostname:     {data.get('hostname', 'N/A')}")
        print(f"City:         {data.get('city', 'N/A')}")
        print(f"Region:       {data.get('region', 'N/A')}")
        print(f"Country:      {data.get('country', 'N/A')}")
        print(f"Location:     {data.get('loc', 'N/A')}")
        print(f"Org:          {data.get('org', 'N/A')}")
        print(f"Timezone:     {data.get('timezone', 'N/A')}")
        print(f"{'='*40}\n")

    except requests.exceptions.RequestException as e:
        print(f"\n[!] Request failed: {e}\n")

def main():
    print("=== IP Lookup Tool ===")
    print("1. Get info about your own IP")
    print("2. Lookup a specific IP")
    
    choice = input("Select an option (1 or 2): ").strip()

    if choice == "1":
        ip_lookup()
    elif choice == "2":
        ip = input("Enter the IP address to look up: ").strip()
        ip_lookup(ip)
    else:
        print("Invalid option. Please run the script again.")

if __name__ == "__main__":
    main()
