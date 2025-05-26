import asyncio
import socket
import struct


def create_multicast_receiver_socket(ip, port, timeout=None):

    # create ipv4 udp socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    if timeout:
        sock.settimeout(timeout)

    # allow other processes to bind to the same port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    except AttributeError:
        pass # unavailable on system

    # bind to all available interfaces
    sock.bind(("", port))

    return MulticastSubscriberSocket(sock, create_multicast_membership_report(ip))


def create_multicast_membership_report(ip: str) -> bytes:
    """Create a membership report for the given IP address."""
    return struct.pack("4sl", socket.inet_aton(ip), socket.INADDR_ANY)


class MulticastSubscriberSocket:

    def __init__(self, sock: socket.socket, membership_report: bytes):
        self._sock = sock
        self._membership_report = membership_report

    def recv(self, buffer_size: int, *args) -> bytes | None:
        """Receive data from the multicast socket."""

        return self._sock.recv(buffer_size, *args)

    async def recv_async(self, buffer_size: int) -> bytes | None:
        """Receive data from the multicast socket."""

        data = await asyncio.get_running_loop().sock_recv(self._sock, buffer_size)

        return data

    def subscribe(self):
        """Subscribe to the multicast group."""
        self._sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, self._membership_report)

    def unsubscribe(self):
        """Unsubscribe from the multicast group."""
        self._sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, self._membership_report)

    def close(self):
        """Close the multicast socket."""
        self._sock.close()
