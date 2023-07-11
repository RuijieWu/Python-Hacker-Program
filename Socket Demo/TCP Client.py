import socket

if __name__ =="__main__":
    target_host = "www.baidu.com"
    target_port = 80
    target_path = "/"
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    client.connect((target_host,target_port))

    package = f"GET {target_path} HTTP/1.1\r\nHost: {target_host}\r\n\r\n"

    client.send(package.encode())

    response = client.recv(4096)

    print(response.decode())
    client.close()