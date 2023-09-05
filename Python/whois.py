import argparse
import socket
import http.client
import ssl
from urllib.parse import urlparse
from datetime import datetime

def dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def http_connection(domain):
    try:
        conn = http.client.HTTPConnection(domain, timeout=10)
        conn.request("HEAD", "/")
        response = conn.getresponse()
        status_code = response.status
        return status_code
    except (http.client.HTTPException, socket.timeout, ConnectionRefusedError):
        return None

def ssl_certificate_info(domain):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=domain) as ssock:
            ssock.connect((domain, 443))
            cert = ssock.getpeercert()
            expiration_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            return expiration_date
    except ssl.CertificateError as e:
        return f"Error: SSL certificate verification failed - {str(e)}"
    except (ConnectionRefusedError, ConnectionError) as e:
        return f"Error: Connection to the server failed - {str(e)}"

def check_website(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    check_functions = {
        "DNS Lookup": dns_lookup,
        "HTTP Status Code": http_connection,
        "SSL Certificate Expiration Date": ssl_certificate_info,
    }

    results = {}
    for key, func in check_functions.items():
        result = func(domain)
        if result is not None:
            if key == "DNS Lookup":
                results[key] = f"IP Address: {result}"
            elif key == "HTTP Status Code":
                results[key] = f"HTTP Status Code: {result}"
            elif key == "SSL Certificate Expiration Date":
                if isinstance(result, str):
                    results[key] = result  # SSL certificate error message
                else:
                    formatted_date = result.strftime('%Y-%m-%d %H:%M:%S')
                    results[key] = f"SSL Certificate Expiration Date: {formatted_date}"
        else:
            results[key] = f"Error: {key} check failed."

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check a website's details.")
    parser.add_argument("url", help="The URL of the website to check.")
    args = parser.parse_args()

    # Validate URL format
    if not args.url.startswith(("http://", "https://")):
        print("Error: Please provide a valid URL starting with 'http://' or 'https://'.")
    else:
        results = check_website(args.url)
        for key, result in results.items():
            print(result)

