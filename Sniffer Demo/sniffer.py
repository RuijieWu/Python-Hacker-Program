'''
EZ Sniffer
'''
import socket
import os
import config

def main():
    '''create socket and listen'''
    #! Windows可以嗅探任何协议的所有流入数据
    #! Linux需要指定一个协议进行嗅探
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)
    sniffer.bind((config.HOST,config.PORT))
    #! 抓包时包含IP头
    sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    #! 如果是WIndows系统就发送IOCTL启用网卡混杂模式
    if os.name=="nt":
        sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

    print(sniffer.recvfrom(65565))

    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)

if __name__ == "__main__":
    main()
