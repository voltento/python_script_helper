from grab import *
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase):#chars=string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

g = Grab(log_file='out.html')
g.setup(proxy='squid.wayray.local:3128', proxy_type='http')
domen = ".ru"
search = u'OpenStreetMap'
foo = True
while foo:
    cite = "http://"+id_generator(random.randint(6,20)) + domen;
    g.go(cite)
    if g.doc.text_search(search):
        foo = False
        print(cite)


