import socket

HOST = "192.168.29.79"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while True:
        src_ip = conn.recv(1024).decode()
        dst_ip = conn.recv(1024).decode()
        print(f"Source IP {src_ip}")
        print(f"Dst IP {dst_ip}")
    # conn.sendall(data)

s.close()
