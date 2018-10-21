import socket
import socks
import time
import random
import threading
import sys

ip = str(input("Hedef/IP : "))
port = int(input("Port : "))
thread_num = int(input("Threads : "))
out_file = str(input("Proxy [proxy.txt] : "))
print ("Number Of Proxies : %s" %(len(open(out_file).readlines())))
