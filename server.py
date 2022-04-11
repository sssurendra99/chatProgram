import socket
import art

art.tprint("SERVER")

HOST = '127.0.0.1'
PORT = 5800

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print('Connected by',addr)
        while True:
            data = conn.recv(1024)
            if not data:break
            print(f"Adonis: {data.decode('utf-8')}")
            message = input("Enter:")
            conn.sendall(bytes(message,'utf-8')) 

