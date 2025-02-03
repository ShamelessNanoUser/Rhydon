# Rhydon

Rhydon is a Python-based tool designed to identify missing or misconfigured HTTP security headers in web applications. It sends HTTP requests to a target URL and analyzes the response headers to determine if any security headers are missing or improperly configured. Currently the following security headers are checked by Rhydon:

- `Content-Security-Policy` 
- `Strict-Transport-Security` 
- `X-Content-Type-Options`
- `X-Frame-Options`
- `X-XSS-Protection`
- `Referrer-Policy`
- `Permissions-Policy`
- `Cross-Origin-Opener-Policy`
- `Cross-Origin-Embedder-Policy`
- `Cross-Origin-Resource-Policy`
- `X-Powered-By`
- `Server`
- `X-AspNet-Version`
- `X-AspNetMvc-Version`
- `Access-Control-Allow-Origin`

## Installation

```
git clone https://github.com/ShamelessNanoUser/Rhydon
pip3 install -r requirements.txt
```

## Usage

```
 ______  _               _
(_____ \| |             | |
 _____) ) |__  _   _  __| | ___  ____
|  __  /|  _ \| | | |/ _  |/ _ \|  _ \
| |  \ \| | | | |_| ( (_| | |_| | | | |
|_|   |_|_| |_|\__  |\____|\___/|_| |_|
              (____/

usage: main.py [-h] (-u URL | -l LIST) [-c COOKIES]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Specify a URL to scan
  -l LIST, --list LIST  Specify a file with URL's
  -c COOKIES, --cookies COOKIES
                        Specify a cookie value to send to webserver
```