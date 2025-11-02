from . import open_socket, decode_telegram


SPEEDWIRE_MULTICAST_IP = "239.12.255.254"
SPEEDWIRE_MULTICAST_PORT = 9522
RX_TIMEOUT = 4.0 #s


def main():

    # open the igmp multicast socket
    with open_socket(SPEEDWIRE_MULTICAST_IP, SPEEDWIRE_MULTICAST_PORT, RX_TIMEOUT) as s:

        # receive 609 byte frames as long as possible
        while frame:= s.recv(608):

            # ensure we got 608 bytes, otherwise decoding will fail
            if len(frame) != 608:
                continue
            
            print(decode_telegram(frame))
        
