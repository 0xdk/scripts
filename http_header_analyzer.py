import requests
import sys

SECURITY_HEADERS = [
    "Strict-Transport-Security", 
    "X-Content-Type-Options",  
    "X-Frame-Options",        
    "Content-Security-Policy", 
    "X-XSS-Protection",         
    "Referrer-Policy"            
]

def get_headers(url):
    try:
        response = requests.get(url)
        return response.headers
    except:
        print("Something went wrong while fetching the headers!")
        sys.exit()

def check_https(url):
    if not url.startswith("https://"):
        print("[!] Warning: This site is using HTTP and not HTTPS!")
    else:
        print("[+] The site is using HTTPS, continuing...")

def check_missing_headers(headers):
    missing = []
    for header in SECURITY_HEADERS:
        if header not in headers:
            missing.append(header)
    
    return missing

def main():
    if len(sys.argv) != 2:
        print("Usage: python http_header_analyzer.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    # add 'http://' if not present in the URL
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
        print(f"Added http:// to the URL. Trying {url}")

    check_https(url)

    print(f"Trying to fetch headers from {url}...")
    headers = get_headers(url)

    missing_headers = check_missing_headers(headers)

    if missing_headers:
        print("\n[!] These security headers are missing:")
        for header in missing_headers:
            print(f"- {header}")
    else:
        print("\n[+] All the important security headers are there!")

if __name__ == "__main__":
    main()

