__author__ = '12345'
import urllib.request
#import gena
import stars.request as sr

#urllib.request.urlretrieve ('http://www.astronet.ru/cgi-bin/skyc.cgi?ut=13.5333333333333&day=19&month=11&year=2016&longitude=-30.3000&latitude=59.9667&azimuth=0&height=0&m=5.0&dgrids=0&dcbnd=0&dfig=1&colstars=1&names=1&xs=800&theme=0&dpl=1&drawmw=1&pdf=0&lang=1', '1.jpg')
#urllib.request.urlretrieve ('http://www.astronet.ru/cgi-bin/skyc.cgi?'+gena.link+'&longitude=-30.3000&latitude=59.9667&azimuth=0&height=0&m=5.0&dgrids=0&dcbnd=0&dfig=1&colstars=1&names=1&xs=800&theme=0&dpl=1&drawmw=1&pdf=0&lang=1', '1.jpg')
urllib.request.urlretrieve(sr.link, '1.jpg')
