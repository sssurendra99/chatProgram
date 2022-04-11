import socket
import art

art.tprint("CLIENT")


IP = '127.0.0.1'
PORT = 5800

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    
    c.connect((IP,PORT))
    while True:
        message = input("Enter: ")
        c.send(bytes(message,'utf-8'))
        data = c.recv(1024)
        print(f"Warrior: {data.decode('utf-8')}")


  

