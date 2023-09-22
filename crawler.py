import socket


def check_ipv6_web(host, port):
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


ipv6_address = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
port_http = 80
port_https = 443

has_http_service = check_ipv6_web(ipv6_address, port_http)
has_https_service = check_ipv6_web(ipv6_address, port_https)

if has_http_service or has_https_service:
    print("IPv6 адресът хоства уебсайт или уеб сървър.")
else:
    print("IPv6 адресът не хоства уебсайт или уеб сървър.")
