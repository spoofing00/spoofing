#!/usr/bin/python3
'''
╔╦╗┌─┐┬─┐┬┌─╔═╗┌─┐┌─┐┌┐┌
 ║║│ │├┬┘├┴┐╚═╗│  ├─┤│││
═╩╝└─┘┴└─┴ ┴╚═╝└─┘┴ ┴┘└┘
'''
import re, requests, time, random, os, sys, urllib
from urllib.parse import unquote

color_array = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
Headers = {
    'Accept':'*/*',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'
}
Dirs = ['Generator','Grabber','Checker']
for diR in Dirs:
    try:
        os.mkdir(diR)
    except:
        pass
try:
    os.mkdir('Generator')
    os.mkdir('Grabber')
    os.mkdir('Checker')
except:
    pass

def Print_Logo():
    Cls = '\x1b[0m'
    Colors = [37,31,32,36,30,35,34,33]
    Logo = '''
                         ___           _     __                 
                        /   \___  _ __| | __/ _\ ___ __ _ _ __  
                       / /\ / _ \| '__| |/ /\ \ / __/ _` | '_ \ 
                      / /_// (_) | |  |   < _\ \ (_| (_| | | | |
                     /___,' \___/|_|  |_|\_\\__/\___\__,_|_| |_|
                                              
                           {GREEN}Instagram : @0zctn{WHITE}: {MAGENTA}DorkScan {YELLOW}| {GREEN}Version{WHITE}: {MAGENTA}1.0.0
                        {YELLOW}Choose An Option {WHITE}:
                         {GREEN}1{YELLOW}-{RED}Dork Generator
                         {GREEN}2{YELLOW}-{RED}Url Grabber
                         {GREEN}3{YELLOW}-{RED}SQL Bug Checker'''.format(GREEN=GREEN,WHITE=WHITE,MAGENTA=MAGENTA,YELLOW=YELLOW,RED=RED)
    for Line in Logo.split('\n'):
        print(random.choice(color_array)+Line)
        time.sleep(0.1)
def Clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
def Url_decoder(l_ink):
    b = unquote(unquote(l_ink))
    return str(b)
def Check(Source):
    sql_errors = {
    "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"MySQL Query fail.*", r"SQL syntax.*MariaDB server","mysql_fetch_array()"),
    "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"Warning.*PostgreSQL"),
    "Microsoft SQL Server": (r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*odbc_.*", r"Warning.*mssql_", r"Msg \d+, Level \d+, State \d+", r"Unclosed quotation mark after the character string", r"Microsoft OLE DB Provider for ODBC Drivers"),
    "Microsoft Access": (r"Microsoft Access Driver", r"Access Database Engine", r"Microsoft JET Database Engine", r".*Syntax error.*query expression"),
    "Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Warning.*oci_.*", "Microsoft OLE DB Provider for Oracle"),
    "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error"),
    "SQLite": (r"SQLite/JDBCDriver", r"System.Data.SQLite.SQLiteException"),
    "Informix": (r"Warning.*ibase_.*", r"com.informix.jdbc"),
    "Sybase": (r"Warning.*sybase.*", r"Sybase message")
    }
    Val = False
    Db = ''
    for db, errors in sql_errors.items():
        for error in errors:
            if re.compile(error).search(Source):
                Val = True
                Db = db
                return Val, Db
                break
                break
            else:
                Val = False
                Db = ''
    return Val, Db
def Generator():
    Clear()
    gen = 0
    f_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
    f1 = input(GREEN+' ['+YELLOW+'*'+GREEN+']'+BLUE+'Enter The Part1 File Address'+RED+'\n  > '+CYAN)
    f1_read = open(f1,'r').read().splitlines()
    print('\n')
    f2 = input(GREEN+' ['+YELLOW+'*'+GREEN+']'+BLUE+'Enter The Part2 File Address'+RED+'\n  > '+CYAN)
    f2_read = open(f2,'r').read().splitlines()
    print('\n')
    f3 = input(GREEN+' ['+YELLOW+'*'+GREEN+']'+BLUE+'Enter The Part3 File Address'+RED+'\n  > '+CYAN)
    f3_read = open(f3,'r').read().splitlines()
    print('\n')
    bef = input(GREEN+' ['+YELLOW+'*'+GREEN+']'+BLUE+'Please Enter The Text For Before Dork'+RED+'\n  > '+CYAN)
    print('\n')
    aft = input(GREEN+' ['+YELLOW+'*'+GREEN+']'+BLUE+'Please Enter The Text For After Dork'+RED+'\n  > '+CYAN)
    print('\n\n')
    print(GREEN+'   ['+YELLOW+'~'+GREEN+']'+BLUE+'Generateds'+WHITE+':')
    for one in f1_read:
        for two in f2_read:
            for three in f3_read:
                gen += 1
                dork = str(bef)+str(one)+str(two)+str(three)+' '+str(aft)
                print(YELLOW+'      ['+GREEN+'+'+YELLOW+']'+CYAN+dork)
                with open('Generator['+f_name+'].txt','a') as wr:
                    wr.write(dork+'\n')
    print('\n\n')
    print(GREEN+' ['+YELLOW+'!'+GREEN+']'+BLUE+'Generated'+CYAN+': '+RED+str(gen))
    input(GREEN+' ['+YELLOW+'!'+GREEN+']'+BLUE+'Press Enter To Continiue'+YELLOW+'...')
def Grabber():
    Clear()
    grab = 0
    f_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
    d_ = input(GREEN+' ['+YELLOW+'*'+GREEN+']'+BLUE+'Enter The Dorks File Address'+RED+'\n  > '+CYAN)
    d_read = open(d_,'r').read().splitlines()
    print('\n\n')
    print(GREEN+'   ['+YELLOW+'~'+GREEN+']'+BLUE+'Grabbeds'+WHITE+':')
    for drk in d_read:
        try:
            r = requests.get('https://www.google.com/search?hl=en&q='+str(drk)+'&num=10&start=10&tbs=0s&safe=off&tbm=').text
        except:
            sys.exit(0)
        reg = re.findall('<div class="g"><h3 class="r"><a href="(.*)&amp;sa=U&amp;ved=',r)
        for _Url in reg:
            grab += 1
            uurl = Url_decoder(_Url.replace('/url?q=','').split(';')[0].split('&')[0])
            if not '/search?ie=UTF-8' in uurl:
                print(YELLOW+'      ['+GREEN+'+'+YELLOW+']'+CYAN+uurl)
                with open('Grabber/Grabbed['+f_name+'].txt','a',encoding="utf-8") as wr:
                    wr.write(uurl+'\n')
    print('\n\n')
    print(GREEN+' ['+YELLOW+'!'+GREEN+']'+BLUE+'Grabbed'+CYAN+': '+RED+str(grab))
    
    input(GREEN+' ['+YELLOW+'!'+GREEN+']'+BLUE+'Press Enter To Continiue'+YELLOW+'...')

def Checker():
    Clear()
    is_v = 0
    not_v = 0
    f_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
    sites = input(GREEN+' ['+YELLOW+'*'+GREEN+']'+BLUE+'Enter The Websites File Address'+RED+'\n  > '+CYAN)
    sites_read = open(sites,'r').read().splitlines()
    v = []
    not_vu = []
    exp = ["'", "')", "';", '"', '")', '";', '`', '`)', '`;', '\\', "%27", "%%2727", "%25%27", "%60", "%5C"]
    print('\n\n')
    print(GREEN+'   ['+YELLOW+'~'+GREEN+']'+BLUE+'Checkeds '+WHITE+':')
    for link in sites_read:
        link = link.replace('ï»¿','')
        v_txt = ''
        if not link in v:
            for e in exp:
                if not link in v:
                    try:
                        res = requests.get(link+e,headers=Headers).text
                    except:
                        res = ''
                    Val, Db = Check(res)
                    if Val is True and Db != '':
                        v_txt = YELLOW+'      ['+WHITE+'$'+YELLOW+']'+CYAN+link+BLUE+' :'+'\n'+BLUE+'         ['+GREEN+'+'+BLUE+']'+GREEN+'Is Vulnerable'+WHITE+': '+YELLOW+'Yes'+'\n'+BLUE+'         ['+GREEN+'+'+BLUE+']'+GREEN+'DataBase'+WHITE+': '+YELLOW+Db
                        if not link in v:
                            is_v += 1
                            with open('Checker/Vulnerable['+f_name+'].txt','a') as wr:
                                wr.write(link+'\n')
                            v.append(link)
                        continue
                    else:
                        v_txt = YELLOW+'      ['+WHITE+'$'+YELLOW+']'+CYAN+link+BLUE+' :'+'\n'+BLUE+'         ['+RED+'-'+BLUE+']'+GREEN+'Is Vulnerable'+WHITE+': '+YELLOW+'No'+'\n'+BLUE+'         ['+RED+'-'+BLUE+']'+GREEN+'DataBase'+WHITE+': '+YELLOW+'None'
                        if not link in not_vu:
                            not_v += 1
                            with open('Checker/Not Vulnerable['+f_name+'].txt','a') as wr:
                                wr.write(link+'\n')
                            not_vu.append(link)
                            continue


            print(v_txt)
    print('\n\n')
    print(GREEN+' ['+YELLOW+'!'+GREEN+']'+BLUE+'Vulnerable Links'+CYAN+': '+RED+str(is_v))
    print(GREEN+' ['+YELLOW+'!'+GREEN+']'+BLUE+'Not Vulnerable Links'+CYAN+': '+RED+str(not_v))
    print('\n')
    input(GREEN+' ['+YELLOW+'!'+GREEN+']'+BLUE+'Press Enter To Continiue'+YELLOW+'...')
while True:
    Clear()
    Print_Logo()
    op = input(CYAN+'                        > '+YELLOW)
    if op == '1':
        Generator()
    elif op == '2':
        Grabber()
    elif op == '3':
        Checker()
    else:
        continue
