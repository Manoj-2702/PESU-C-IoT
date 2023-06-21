import socket
from scapy import all
from scapy.all import *
from scapy.layers import inet
from io import StringIO

HOST = "192.168.29.79"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
s.connect((HOST, PORT))


def custom_action(packet):
    print(f"{packet[0][1].src} ==> {packet[0][1].dst}")
    # str = "Hello World"
    # print(packet.show())
    src_ip = packet[0][1].src
    dst_ip = packet[0][1].dst

    s.send(src_ip.encode())
    s.send(dst_ip.encode())
    # data = s.recv(1024).decode()
    # print(data)


sniff(prn=custom_action)

s.close()
