import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = socket.gethostname()  # To get the name of host
port_number = 1234
print("The name of local machine", host_name)  # The name of local machine admins-MacBook-Pro-3.local

host_port_pair = (host_name, port_number)  # A tuple

sock.connect(host_port_pair)  # To actively intiate the TCP Server connection

while True:
    print("TYPE A MESSAGE FOR SERVER ==> ")
    msg_for_server = input()
    if not msg_for_server:
        break
    arr = bytes(msg_for_server, "utf-8")
    print("flag")
    sock.send(arr)

    msg_from_server = sock.recv(2048)
    if not msg_from_server:
        print("<...No Reply from Server...>")
    else:
        print("From Server ==> ", msg_from_server)

sock.close()