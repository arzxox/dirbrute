# 🚀 Dirbrute – Directory Bruteforce Tool

Dirbrute is a lightweight and efficient **directory brute-forcing tool** written in Python. It is designed to discover hidden directories and files on web servers using a wordlist, similar to tools like Gobuster and Dirsearch.

This project was built as part of my cybersecurity learning journey to understand **web enumeration, HTTP requests, and performance optimization techniques**.

---

## Features:

- Wordlist-based directory and file discovery  
- Multi-threading for faster enumeration  
- Supports HTTP and HTTPS targets  
- Optional file extension brute-forcing  
- Filters non-existing (404) responses  
- Timeout handling to avoid hanging requests  
- Connection reuse using `requests.Session()`  
- Command-line interface using `argparse`  

---

## Requirements:

- Python 3.x  
- requests module  

Install dependencies:
```bash
pip install requests
```

## Usage:
```bash
python dirbrute.py -u <URL> -w <WORDLIST>
```

## Example:
```bash
python dirbrute.py -u http://example.com -w wordlist.txt
```

## Optional Arguments
-x, --ext      -     Add file extension (e.g. php, html)
-t, --threads  -     Number of threads (default: 20)

## Example with extension:
```bash
python dirbrute.py -u http://example.com -w wordlist.txt -x php -t 50
```

## How it works:
- Takes a target URL and wordlist as input
- Appends each word (and optional extension) to the URL
- Sends HTTP requests concurrently using threads
- Displays valid responses (non-404 status codes)

 ## Disclaimer:
This tool is created for educational purposes only.
Do not use it on systems you do not own or have permission to test.
