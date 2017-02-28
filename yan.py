# coding: utf-8
import xml.dom.minidom
import xml.dom.minidom
import urllib.parse
from grab import Grab
import xml.etree.ElementTree

GEOCODE_URL = 'http://geocode-maps.yandex.ru/1.x/?'
	

params = urllib.parse.urlencode({'geocode': 'Санкт-Петербург, Бумажная 4', 'key': 'ADBtnFgBAAAA1eTFSgIAyDrzmyVO9aGQNIKI-FDOBJ_SgDwAAAAAAAAAAAAaxBIO6vnCckEA_mCVDUalQYyhEA=='})
url=GEOCODE_URL+params
timeout=2

g = Grab()
g.setup(url=url, log_file='out.xml')
g.request()

from xml.dom import minidom
xmldoc = minidom.parse('out.xml')
itemlist = xmldoc.getElementsByTagName('pos')
print(len(itemlist))
for item in itemlist:
  print(item.firstChild.nodeValue)

#response = http.request('GET', url, timeout=timeout)
#print response
#dom = xml.dom.minidom.parseString(response)
#pos_elem = dom.getElementsByTagName('pos')[0]
#pos_data = pos_elem.childNodes[0].data
        #return tuple(pos_data.split())
