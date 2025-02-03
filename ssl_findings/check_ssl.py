from OpenSSL import SSL
from socket import socket
from datetime import datetime
import idna


def get_ssl_cert(hostname):
    try:
        hostname_idna = idna.encode(hostname)

        sock = socket()
        sock.connect((hostname, 443))

        ctx = SSL.Context(SSL.SSLv23_METHOD)
        ctx.check_hostname = False
        ctx.verify_mode = SSL.VERIFY_NONE

        sock_ssl = SSL.Connection(ctx, sock)
        sock_ssl.set_connect_state()
        sock_ssl.set_tlsext_host_name(hostname_idna)
        sock_ssl.do_handshake()
        cert = sock_ssl.get_peer_certificate()
        sock_ssl.close()
        sock.close()
    except Exception as e:
        cert = ""

    return cert


def check_expired(hostname, cert):
    finding_expired = None
    expired = cert.has_expired()
    expiry_date = datetime.strptime(cert.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')

    if expired:
        print('[\033[93m WARN \033[0m] The SSL certificate expired on', expiry_date, 'on', hostname)
        finding_expired = {'finding_name': 'expired_ssl', 'host': hostname, 'expired_at': expiry_date}

    return finding_expired


def check_wildcard(hostname, cert):
    finding_wildcard = None
    subject = cert.get_subject().get_components()[-1][-1].decode()

    if subject.startswith('*'):
        wildcard = True
    else:
        wildcard = False

    if wildcard:
        print('[\033[93m WARN \033[0m]', hostname, 'uses a wildcard certificate')
        finding_wildcard = {'finding_name': 'wildcard_ssl', 'host': hostname}

    return finding_wildcard
