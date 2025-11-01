import socket
import struct
from contextlib import contextmanager

@contextmanager
def open_socket(group_ip: str, group_port: int, rx_timeout: float):

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as sock:
        
        sock.settimeout(rx_timeout)

        # allow other process to bind to the same port
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind to any interface
        sock.bind(("", group_port))

        # create igmp membership report
        membership_report = struct.pack("4sl", socket.inet_aton(group_ip), socket.INADDR_ANY)

        sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership_report)

        yield sock

        sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, membership_report)

        sock.close()
        
