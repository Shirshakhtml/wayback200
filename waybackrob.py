import requests
import re
import sys
from multiprocessing.dummy import Pool

def robots(host):
    url = f"https://web.archive.org/cdx/search/cdx?url={host}/robots.txt&output=json&fl=timestamp,original&filter=statuscode:200&collapse=digest"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for entry in data[1:]:  # Skipping the header row
                print(f"Timestamp: {entry[0]}, URL: {entry[1]}")
        else:
            print(f"Failed to fetch data for {host}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    robots(domain)
