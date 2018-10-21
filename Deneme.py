import socket
import socks
import time
import random
import threading
import sys

print ("     ___  ___  ____  ____ ")   
print ("    / _ \/ _ \/ __ \/ __/ ")   
print (" _ / // / // / /_/ /\ \_  ")   
print ("(_)____/____/\____/___(_) ") 
print (" Instagram : @bossy.078 ")
print (" ")                             

ip = str(input("[+] IP : "))
url = str(input("[+] URL : "))
port = int(input("[+] Port : "))
thread_num = int(input("[+] Threads : "))
out_file = str(input("[+] Proxy [proxy.txt] : "))
print ("[+] Number Of Proxies : %s" %(len(open(out_file).readlines())))
time.sleep(0.2)
multiple = int(input("[+] Input the Magnification : "))
