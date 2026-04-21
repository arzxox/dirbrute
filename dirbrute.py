#!/bin/python3

import requests
import argparse
import sys
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser()

parser.add_argument('-w', '--wordlist', required=True, help="Wordlist file")
parser.add_argument('-u', '--url', required=True, help="Target URL")
parser.add_argument('-x', '--ext', help="File extension (php, html, txt)")
parser.add_argument('-t', '--threads', type=int, default=20, help="Number of threads")
args = parser.parse_args()

if not args.url.startswith(('http://', 'https://')):
    print("[-] Please enter a valid URL with http:// or https://")
    sys.exit()

base_url = args.url.rstrip('/')

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0'
})

def scan_path(line):
    line = line.strip()
    if not line:
        return

    if args.ext:
        line = f"{line}.{args.ext}"

    url = f"{base_url}/{line}"

    try:
        r = session.get(url, timeout=3, allow_redirects=False)
        if r.status_code != 404:
            print(f"[+] Found: {url} [{r.status_code}]")
    except requests.exceptions.RequestException:
        pass

try:
    with open(args.wordlist, 'r') as file:
        words = file.readlines()

    print(f"[+] Starting scan with {args.threads} threads...\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(scan_path, words)

except FileNotFoundError:
    print("[-] Wordlist file not found")
except KeyboardInterrupt:
    print("\n[-] Scan stopped by user")