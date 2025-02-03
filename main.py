from connect import connect
from headers import check_missing
from headers import check_contents
from ssl_findings import check_ssl
from urllib.parse import urlparse
import argparse
import sys

print('''
 ______  _               _             
(_____ \| |             | |            
 _____) ) |__  _   _  __| | ___  ____  
|  __  /|  _ \| | | |/ _  |/ _ \|  _ \ 
| |  \ \| | | | |_| ( (_| | |_| | | | |
|_|   |_|_| |_|\__  |\____|\___/|_| |_|   
              (____/                                  
''')

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-u', '--url', help='Specify a URL to scan')
group.add_argument('-l', '--list', help='Specify a file with URL\'s')
parser.add_argument('-c', '--cookies', help='Specify a cookie value to send to webserver')
args = parser.parse_args()


def main():
    hosts = []
    warn = False
    ssl_warn = False

    # Handle user input
    if args.url:
        hosts.append(args.url)

    if args.list:
        try:
            with open(args.list, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    hosts.append(line.strip('\n'))
        except FileNotFoundError:
            print('[\033[91m ERROR \033[0m] File does not exist... exiting')
            sys.exit()

    # Check securiy headers
    for url in hosts:
        parsed = urlparse(url)

        if parsed.scheme:
            hostname = parsed[1]

            headers = connect.send_request(url, args.cookies)

            if headers:
                warn = check_missing.check(hostname, headers, warn)
                warn = check_contents.check(hostname, headers, warn)
            else:
                print('[\033[91m ERROR \033[0m] Failed to fetch headers, proceeding to next host...')
        else:
            print('[\033[91m ERROR \033[0m]', url, 'isn\'t a URL. Skipping...')
            continue

    if not warn:
        print('[\033[92m INFO \033[0m] Rhydon did not find any security header findings')

    # Check SSL 
    cert = check_ssl.get_ssl_cert(hostname)

    if cert != "":
        print('[\033[92m INFO \033[0m] Received an SSL certificate from', hostname)
        expired = check_ssl.check_expired(hostname, cert)
        wildcard = check_ssl.check_wildcard(hostname, cert)

        if expired is not None or wildcard is not None:
            ssl_warn = True

    if not ssl_warn:
        print('[\033[92m INFO \033[0m] Rhydon did not find any SSL findings')


if __name__ == "__main__":
    main()    