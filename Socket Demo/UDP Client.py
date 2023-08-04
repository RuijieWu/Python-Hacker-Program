'''
UDP Socket Program Demo
'''
import socket

if __name__ =="__main__":
    TARGET_HOST = "www.baidu.com"
    TARGET_PORT = 80

    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    package = ""

    client.sendto(package.encode(),(target_host,target_host))

    response , address = client.recvfrom(4096)

    print(response.decode())
    client.close()
