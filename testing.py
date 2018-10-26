import urllib.request

# import math
# # n = int(input("Enter a number: "))
# # while n > 0:
# #     print("Hello", sep="\n", end=" ")
# #     print("n:", n, end="\n")
# #     n = n - 1
# #     if n == 3:
# #         break
# # print(n)
#
# # while True:
# #     line = input("> ")
# #     if line == "done" or line == "Done":
# #         break
# #     elif line[0] == "#":
# #         continue
# #     print(line)
# # print("Done!")
#
# for i in ["abc", "bcd", "def", "ghi", "jkl", "mno"]:
#     print("Happy New Year", i, end="!\n")
# print("Done!")
#
# max_number = 0
# min_number = None
# found = False
# for i in [1, 20, 3, 4, 5]:
#
#     if min_number is None:
#         min_number = i
#     elif min_number >= i:
#         min_number = i
#
#     if i >= max_number:
#         max_number = i
#
#     if i == 2:
#         found = True
#         break
#
# print("Max Number: ", max_number)
# print("Min. Number: ", min_number)
# print("isThere: ", found)
#
# dic = {"x": 50, "y": 3}
# key = "x"
# if key in dic:
#     print(dic[key])
#
# l = [1, 2, 3, 4]
# for i in range(len(l)):
#     print(i)
#
# str = "Hello There"
# for i in str:
#     # letter = str[i]
#     print(i, end="")
#
# print()
# print("loc: ", "helllo".find("h"))
#
# data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# atpos = data.find("@")
# print(atpos)
# sposs = data.find(" ", atpos)
# print(data[atpos:sposs])
#
# # content = dir(math)
# # print(content)
#
# inputfile = open("text.txt", "r")
#
# for i in inputfile:
#     print(i)
#
# inputfile.close()
# outputfile = open("text.txt", "a")
# outputfile.write("\nHey this is added")
# outputfile.close()
#

# num = None
# try:
#     num = input("Enter Number: ")
#     num = int(num)
#     print("number:", num * 2)
# except ValueError:
#     print("Invalid Input: %s" % num)

# list_of_lists = []
# for i in range(3):
#     L = []
#     for j in range(4):
#         L.append(i*j)
#     list_of_lists.append(L)
#
# print(list_of_lists)
#
#
# list1 = [(1, 2, 3), (2, 3, 4)]
# count = 1
# for i in list1:
#     print("count: ", count)
#     for j in i:
#         print(j, end=" ")
#     count = count + 1
#     print()

# server
# TCP Server Code

# host="127.0.0.1"                # Set the server address to variable host
# host = "127.168.2.75"  # Set the server address to variable host
# port = 4446  # Sets the variable port to 4444
# host = "localhost"
# port = 1234
#
#
# s = socket(AF_INET, SOCK_STREAM)
# #s.setsockopt(SO_REUSEADDR, SO_REUSEADDR, 1)
# s.connect((gethostname(), port))  # Binds the socket. Note that the input to
# # the bind function is a tuple
# # s.listen(1)  # Sets socket to listening state with a  queue
# # of 1 connection
# while True:
#     print(sys.stderr, "Listening for connections.. ")
#     connection, client_address = s.accept()  # Accepts incoming request from client and returns
# # # socket and address to variables q and addr
# #     print("addr:", addr, "q: ", q)
# #     data = input("Enter data to be send:  ")  # Data to be send is stored in variable data from
# # # user
# # q.send(bytes(data))  # Sends data to client
# # s.close()
#     print("hello")
#     try:
#         print(sys.stderr, 'connection from', client_address)
#
#             # Receive the data in small chunks and retransmit it
#         while True:
#             data = connection.recv(16)
#             print(sys.stderr, 'received "%s"' % data)
#             if data:
#               print(sys.stderr, 'sending data back to the client')
#               connection.sendall(data)
#             else:
#               print(sys.stderr, 'no more data from', client_address)
#               break
#
#     finally:
#             # Clean up the connection
#         client_address.close()
#         s.close()
# End of code

# Client
# TCP Client Code

# host="127.0.0.1"            # Set the server address to variable host

# host = "127.168.2.75"
# port = 4446  # Sets the variable port to 4444
#
# # from socket import *  # Imports socket module
#
# s = socket(AF_INET, SOCK_STREAM, 0)  # Creates a socket
# s.connect((host, port))  # Connect to server address
#
# msg = s.recv(1024)  # Receives data upto 1024 bytes and stores in variables msg
#
# print("Message from server : " + msg.strip().decode('ascii'))
#
# s.close()  # Closes the socket
# # End of code

#
# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Connect the socket to the port where the server is listening
# server_address = ('localhost', 10000)
# print(sys.stderr, 'connecting to %s port %s' % server_address)
# sock.connect(server_address)
# try:
#
#     # Send data
#     message = 'This is the message.  It will be repeated.'
#     print(sys.stderr, 'sending "%s"' % message)
#     sock.sendall(message)
#
#     # Look for the response
#     amount_received = 0
#     amount_expected = len(message)
#
#     while amount_received < amount_expected:
#         data = sock.recv(16)
#         amount_received += len(data)
#         print(sys.stderr, 'received "%s"' % data)
#
# finally:
#     print(sys.stderr, 'closing socket')
#     sock.close()
from urllib.parse import urlparse, urljoin
import socket

url = 'http://www.google.com'
response = urllib.request.urlopen(url)
html = response.read()
print(html)

testurl = 'http://netloc:80/path;parameters?query=argument#fragment'
tut_url = "https://www.google.com/search"
parsed = urlparse(testurl)
print(parsed)
print(parsed.port)
print(parsed.geturl())

print(urljoin('http://www.example.com/path/file.html', 'anotherfile.html'))
print (urljoin('http://www.example.com/path/file.html', '../anotherfile.html'))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 123
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("Getting connection from adress: ", addr)
    c.close()
