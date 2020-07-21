import socket
import random

print("")
print("Link Cable Manipulator for Pokemon R/B/Y/G/S/C v0.1")
print("Made by Nasina: https://github.com/Nasina7")
print("This script requires that you are using BGB.")
print("What would you like to do?")
print("1. Send Mirrored Data (Battle or Trade with yourself)")
print("2. Send Random Data (Watch the game explode)")
option = input("Type a Number and press Enter: ")
mirror = option
if mirror != "1" and mirror != "2":
    print("That is an invalid option.  Please run the script again.")
    exit()
print("On BGB, right click the screen, hover over link and click connect.")
print("Ensure that the IP entered is 127.0.0.1:8765.  If it is not, type it in.")
print("In the Dialog box, press ok and wait for the script to say Connected!")
print("When it does, you may initiate a battle or trade")
TCP_IP = '127.0.0.1'
TCP_PORT = 8765
BUFFER_SIZE = 8
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(BUFFER_SIZE)
conn.send(b'\x01\x01\x04\x00\x00\x00\x00\x00')  # Preform initial connection check
print("Connected!")
noFreeze = 0
noSlow = 0
back4 = b'\x00'
back5 = b'\x00'
back6 = b'\x00'
back7 = b'\x00'
randHex = b'\x00'
conn.send(b'l\x01\x00\x00\x00\x00\x00\x00')
while 1:
    data = conn.recv(1)
    data1 = conn.recv(1)
    data2 = conn.recv(1)
    data3 = conn.recv(1)
    data4 = conn.recv(1)
    data5 = conn.recv(1)
    data6 = conn.recv(1)
    data7 = conn.recv(1)
    noFreeze = noFreeze + 1
    if noFreeze == 10:
        conn.send(b'l\x01\x00\x00\x00\x00\x00\x00')
        noFreeze = 0
    if data == b'\x6a':
        conn.send(b'\x6a')
        conn.send(b'\x00')
        conn.send(b'\x00')
        conn.send(b'\x00')
        conn.send(data4)
        conn.send(data5)
        conn.send(data6)
        conn.send(data7)
    elif data == b'e':
        conn.send(b'j\x01\x00\x00\x00\x00\x00\x00')
    elif data == b'h':
        randHex = random.randint(0,255)
        randHex = randHex.to_bytes(1,"big")
        conn.send(b'i')
        if mirror == "1":
            conn.send(data1)
        elif mirror == "2":
            if data1 == b'\x00':
                conn.send(b'\x00')
            elif data1 == b'\x01':
                conn.send(b'\x01')
            elif data1 == b'u':
                conn.send(b'u')
            elif data1 == b'U':
                conn.send(b'U')
            elif data1 == b'`':
                conn.send(b'`')
            elif data1 == b'v':
                conn.send(b'v')
            elif data1 == b')':
                conn.send(b')')
            elif data1 == b'9':
                conn.send(b'9')
            elif data1 == b'\x85':
                conn.send(b'\x85')
            elif data1 == b'\xd0':
                conn.send(b'\xd0')
            elif data1 == b'\x86':
                conn.send(b'\x86')
            elif data1 == b'\xd1':
                conn.send(b'\xd1')
            elif data1 == b'\xd2':
                conn.send(b'\xd2')
            elif data1 == b'a':
                conn.send(b'a')
            else:
                conn.send(randHex)
        conn.send(b'\x80\x00\x00\x00\x00\x00')
    elif data == b'i':
        randHex = random.randint(0,255)
        randHex = randHex.to_bytes(1,"big")
        conn.send(b'h')
        if mirror == "1":
            conn.send(data1)
        elif mirror == "2":
            if data1 == b'\x00':
                conn.send(b'\x00')
            elif data1 == b'\x02':
                conn.send(b'\x02')
            elif data1 == b'\xd2':
                conn.send(b'\xd2')
            elif data1 == b'a':
                conn.send(b'a')
            else:
                conn.send(randHex)
        conn.send(b'\x81')
        conn.send(b'\x00')
        conn.send(back4)
        conn.send(back5)
        conn.send(back6)
        conn.send(back7)
    #else:
        # print("Unneeded BGB command: ",data)
        