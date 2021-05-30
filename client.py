import socket, threading
HOST=socket.gethostname()
PORT=150
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT)
while True:
    s.listen(1)
    conn,addr=s.accept()
    print("Connection By...",addr)
    while 1:
        data=conn.recv(1024)
        if data.strip()[4:]=="exit":
            print("Closed By", addr)
        else:
            conn.send(data)
        if not data:
            break
        print(data)
conn.close()
