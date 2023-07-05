import socket

if __name__ =="main":
    target_host = "www.baidu.com"
    target_port = 80

    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    package = ""

    client.sendto(package.encode(),(target_host,target_host))

    response , address = client.recvfrom(4096)

    print(response.decode())
    client.close()