'''
Sniff various protocols by scapy frame
'''
from scapy.all import sniff

def packet_callback(packet) -> None:
    '''show packet info'''
    if packet["TCP"].payload:
        #if "user" in str(packet['TCP'].payload).lower() or "pass" in str(packet["TCP"].payload).lower():
        print(f"[*] Destination: {packet['IP'].dst}")
        print(f"[*] {str(packet['IP'].payload)}")
#BPF Grammar
#  descriptor       direction       protocol
#host/net/port       src/dst     ip/ip6/tcp/udp

def main():
    '''entrance'''
    #! HTTP
    sniff(filter="tcp port 80 or tcp port 443",prn=packet_callback,store = 0)

if __name__ == "__main__":
    main()
