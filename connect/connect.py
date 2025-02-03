import requests

def send_request(url, cookie):
    try:
        print('[\033[92m INFO \033[0m] Sending HTTP-request to', url)
        headers = {'Origin': 'https://example.local/'}

        if cookie:
            split_cookie = cookie.split(':')
            cookies = {split_cookie[0]: split_cookie[1]}
        else:
            cookies = {}

        response = requests.get(url, headers=headers, cookies=cookies, allow_redirects=True, timeout=20)
        headers = response.headers

        return headers
    except Exception as e:
        print('[\033[91m ERROR \033[0m] Could not connect to server via HTTP', e)
        return []
