from smasniff.multicast_client import open_socket

def test_creation():

    with open_socket("239.12.255.254", 9522, rx_timeout=5.0) as s:

        s.recv(608)

