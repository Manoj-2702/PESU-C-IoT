import socket

HOST = "192.168.43.79"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while True:
        src_ip = conn.recv(1024).decode()
        dst_ip = conn.recv(1024).decode()
        src_port = conn.recv(1024).decode()
        dst_port = conn.recv(1024).decode()
        proto = conn.recv(1024).decode()
        flag = conn.recv(1024).decode()
        print(f"Source IP {src_ip}")
        print(f"Dst IP {dst_ip}")
        print(f"Source Port {src_port}")
        print(f"Destination Port {dst_port}")
        if proto == '6':
            print(f"Protocol: TCP")
        elif proto == '17':
            print(f"Protocol: UDP")
        elif proto == '1':
            print(f"Protocol: TCP")
        else:
            print(f"Protocol: {proto}")
        print(f"Flag: {flag}")
    # conn.sendall(data)

s.close()
