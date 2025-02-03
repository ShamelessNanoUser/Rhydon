def check(hostname, headers, warn):
    if 'Strict-Transport-Security' not in headers:
        print('[\033[93m WARN \033[0m] The Strict-Transport-Security header is missing on:', hostname)
        warn = True

    if 'Content-Security-Policy' not in headers:
        print('[\033[93m WARN \033[0m] The Content-Security-Policy header is missing on:', hostname)
        warn = True

    if 'X-Frame-Options' not in headers:
        print('[\033[93m WARN \033[0m] The X-Frame-Options header is missing on:', hostname)
        warn = True

    if 'X-Content-Type-Options' not in headers:
        print('[\033[93m WARN \033[0m] The X-Content-Type-Options header is missing on:', hostname)
        warn = True

    if 'Referrer-Policy' not in headers:
        print('[\033[93m WARN \033[0m] The Referrer-Policy header is missing on:', hostname)
        warn = True

    if 'Permissions-Policy' not in headers:
        print('[\033[93m WARN \033[0m] The Permissions-Policy header is missing on:', hostname)
        warn = True

    if 'Cross-Origin-Opener-Policy' not in headers:
        print('[\033[93m WARN \033[0m] The Cross-Origin-Opener-Policy header is missing on:', hostname)
        warn = True

    if 'Cross-Origin-Embedder-Policy' not in headers:
        print('[\033[93m WARN \033[0m] The Cross-Origin-Embedder-Policy header is missing on:', hostname)
        warn = True

    if 'Cross-Origin-Resource-Policy' not in headers:
        print('[\033[93m WARN \033[0m] The Cross-Origin-Resource-Policy header is missing on:', hostname)
        warn = True

    return warn
