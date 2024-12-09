import os
import subprocess
import requests
from urllib.parse import urljoin

# Color codes for pretty output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Banner
def banner():
    print(f"{Colors.HEADER}CTF Scanner - All-in-One Tool{Colors.ENDC}")
    print(f"{Colors.OKBLUE}For educational use only.{Colors.ENDC}")
    print()

# Nmap Port Scanner
def nmap_scan(target):
    print(f"{Colors.HEADER}Running Nmap Scan on: {target}{Colors.ENDC}")
    try:
        subprocess.run(["nmap", "-A", "-T4", target], check=True)
    except Exception as e:
        print(f"{Colors.FAIL}[-] Error running Nmap: {e}{Colors.ENDC}")

# Gobuster Directory Brute-Force
def gobuster_scan(target, wordlist):
    print(f"{Colors.HEADER}Running Gobuster on: {target}{Colors.ENDC}")
    try:
        subprocess.run(["gobuster", "dir", "-u", target, "-w", wordlist], check=True)
    except Exception as e:
        print(f"{Colors.FAIL}[-] Error running Gobuster: {e}{Colors.ENDC}")

# Nikto Web Vulnerability Scanner
def nikto_scan(target):
    print(f"{Colors.HEADER}Running Nikto Scan on: {target}{Colors.ENDC}")
    try:
        subprocess.run(["nikto", "-h", target], check=True)
    except Exception as e:
        print(f"{Colors.FAIL}[-] Error running Nikto: {e}{Colors.ENDC}")

# Strings Extraction from File
def extract_strings(filename):
    print(f"{Colors.HEADER}Extracting Strings from: {filename}{Colors.ENDC}")
    try:
        result = subprocess.run(["strings", filename], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"{Colors.FAIL}[-] Error extracting strings: {e}{Colors.ENDC}")

# Steghide Analysis
def steghide_extract(filename):
    print(f"{Colors.HEADER}Running Steghide on: {filename}{Colors.ENDC}")
    try:
        subprocess.run(["steghide", "extract", "-sf", filename], check=True)
    except Exception as e:
        print(f"{Colors.FAIL}[-] Error running Steghide: {e}{Colors.ENDC}")

# Main Menu
def main():
    banner()
    print("1. Nmap Port Scan")
    print("2. Gobuster Directory Brute-Force")
    print("3. Nikto Web Vulnerability Scan")
    print("4. Strings Extraction (File Analysis)")
    print("5. Steghide (Steganography)")
    print("6. Exit")
    choice = input(f"{Colors.WARNING}Choose an option: {Colors.ENDC}")

    if choice == "1":
        target = input("Enter target IP or domain: ")
        nmap_scan(target)
    elif choice == "2":
        target = input("Enter target URL (e.g., http://example.com): ")
        wordlist = input("Enter path to wordlist: ")
        gobuster_scan(target, wordlist)
    elif choice == "3":
        target = input("Enter target URL or IP: ")
        nikto_scan(target)
    elif choice == "4":
        filename = input("Enter path to the file: ")
        extract_strings(filename)
    elif choice == "5":
        filename = input("Enter path to the file (image/audio): ")
        steghide_extract(filename)
    elif choice == "6":
        print(f"{Colors.OKBLUE}Exiting...{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}Invalid option!{Colors.ENDC}")
        main()

if __name__ == "__main__":
    main()