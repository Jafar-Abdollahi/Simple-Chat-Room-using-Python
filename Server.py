import soket
PORT=150
Host=socket.gethostname()
s=spcket.socket(socket.AF_INET, socket.SOCK_STREM)
s.connect((HOST,PORT))
NICK=input("Wellcome, Please Enter your Name...")
while True:
    MSG=input(">>")
    MSG=NICCK+":"+MSG
    if MSG.strip()[4:]=="exit":
        break
    s.send(MSG.encode("UTF-8")
    data=s.rec(1024)
    print(data)

s.close()
