import re

def check(hostname, headers, warn):

    if 'X-Powered-By' in headers:
        value = headers['X-Powered-By']
        print('[\033[93m WARN \033[0m] The X-Powered-By header contains the value "' + value + '" on:', hostname)
        warn = True

    if 'Server' in headers:
        value = headers['Server']
        if re.match(r'Apache\/[0-9].+', value) or re.match(r'nginx\/[0-9].+', value) or re.match(r'Microsoft IIS\/[0-9].+', value):
            print('[\033[93m WARN \033[0m] The Server header contains the value "' + value + '" on:', hostname)
            warn = True

    if 'X-AspNet-Version' in headers:
        value = headers['X-Aspnet-Version']
        print('[\033[93m WARN \033[0m] The X-AspNet-Version header contains the value "' + value + '" on:', hostname)
        warn = True

    if 'X-AspNetMvc-Version' in headers:
        value = headers['X-AspNetMvc-Version']
        print('[\033[93m WARN \033[0m] The X-AspNetMvc-Version header contains the value "' + value + '" on:', hostname)
        warn = True

    if 'Content-Security-Policy' in headers:
        value = headers['Content-Security-Policy']
        split_value = value.split(';')

        for line in split_value:
            match line:
                case str(x) if 'default-src' in x and 'unsafe-eval' in x and 'unsafe-inline' in x:
                    print('[\033[93m WARN \033[0m] The Content-Security-Policy default-src contains unsafe-inline and unsafe-eval on:', hostname)
                    warn = True
                case str(x) if 'default-src' in x and 'unsafe-inline' in x:
                    print('[\033[93m WARN \033[0m] The Content-Security-Policy default-src contains unsafe-inline on:', hostname)
                    warn = True
                case str(x) if 'script-src' in x and 'unsafe-eval' in x and 'unsafe-inline' in x:
                    print('[\033[93m WARN \033[0m] The Content-Security-Policy script-src contains unsafe-inline and unsafe-eval on:', hostname)
                    warn = True
                case str(x) if 'script-src' in x and 'unsafe-inline' in x:
                    print('[\033[93m WARN \033[0m] The Content-Security-Policy script-src contains unsafe-inline on:', hostname)
                    warn = True

    if 'X-XSS-Protection' in headers:
        value = headers['X-XSS-Protection']

        if value != '0':
            print('[\033[93m WARN \033[0m] The X-XSS-Protection header is set to block XSS (unsafe) on:', hostname)
            warn = True

    if 'Strict-Transport-Security' in headers:
        value = headers['Strict-Transport-Security']
        max_age = value.split(';')[0]
        max_seconds = max_age.split('=')[1]

        if int(max_seconds) < 31536000:
            print('[\033[93m WARN \033[0m] The Strict Transport Security header is set but is insufficient on:', hostname)
            warn = True

    if 'Access-Control-Allow-Origin' in headers and headers['Access-Control-Allow-Origin'] == '*':
        print('[\033[93m WARN \033[0m] The Access-Control-Allow-Origin header contains a wildcard on:', hostname)
        warn = True


    return warn