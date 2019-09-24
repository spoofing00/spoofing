import requests

print("""
   ___                    ____                   _          
  / _ \_______ __ ____ __/ __/______ ____  ___  (_)__  ___ _
 / ___/ __/ _ \\ \ / // /\ \/ __/ _ `/ _ \/ _ \/ / _ \/ _ `/
/_/  /_/  \___/_\_\\_, /___/\__/\_,_/_//_/_//_/_/_//_/\_, / 
                  /___/                              /___/  """)
print("root@bossy:~# Helps Download Proxy")
print('\r\n')


type = str(input("root@bossy:~# Type ( Socks4 / Socks5 / HTTP ) : "))
cty = str(input("root@bossy:~# Country (EX : TR / FR / RU / All ) : "))
anon = str(input("root@bossy:~# anonymity ( Anonymous / Elite / All ) : "))
to = str(input("root@bossy:~# Timeout : "))
sl = str(input("root@bossy:~# SSL Mode ( Yes / No / All ) : "))
file = str(input("root@bossy:~# File Name (EX : Proxies.txt / Socks4.txt / Socks5.txt ) : "))
rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype='+str(type)+'&country='+str(cty)+'&anonymity='+str(anon)+'&ssl='+str(sl)+'&timeout='+str(to))
with open(str(file),'wb') as fp:
	fp.write(rsp.content)
