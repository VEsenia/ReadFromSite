from grab import Grab
import urllib.parse

GEOCODE_URL = 'http://geocode-maps.yandex.ru/1.x/?'

g = Grab()
g.go('НАЗВАНИЕ сайта')
iter=0
#print('РЕГИОНЫ')
for region in g.doc.select('//div[contains(@class, "sale-group")]')[0].select('.//div[@class="panel-heading"]'): 
  #print('#######')
  regName = region.text()
  shopName=''
  if regName.find(' район') >=0:
     shopName='Ижевск Удмуртская республика ' + regName + " " 
  else: shopName=regName + " "

  RegionHref = region.select('.//a').attr('href')
 
  for shop in g.doc.select('//div[contains(@class, "sale-group")]')[0].select('.//ul[@class="aside-links-menu"]')[iter].select('.//a') :
    shopStr = shopName + shop.text() 
    print(shopStr) 
    #Получим координаты
    
    params = urllib.parse.urlencode({'geocode': shopStr, 'key': 'ADBtnFgBAAAA1eTFSgIAyDrzmyVO9aGQNIKI-FDOBJ_SgDwAAAAAAAAAAAAaxBIO6vnCckEA_mCVDUalQYyhEA=='})
    url=GEOCODE_URL+params

    gNew = Grab()
    gNew.setup(url=url, log_file='out.xml')
    gNew.request()

    from xml.dom import minidom
    xmldoc = minidom.parse('out.xml')
    itemlist = xmldoc.getElementsByTagName('pos')
    print(len(itemlist))
    for item in itemlist:
        print(shopStr)
        print(item.firstChild.nodeValue)
 
  iter+=1


