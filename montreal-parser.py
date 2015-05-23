from lxml import html
import requests

for x in range(1,10):

    pageUrl =  "http://www.tourisme-montreal.org/What-To-Do/Events/Page" + str(x)
    page = requests.get(pageUrl)
    tree = html.fromstring(page.text)

    events = []
    for atag in tree.xpath('//td[@class="data"]'):
        events.append(atag.text_content().strip())
    
    eventFile = "events" + str(x) + ".txt"
    file = open(eventFile,"w")
    for event in events:
        encoded = event.encode('utf-8')
        print >> file, encoded
        print >> file, '\n'

    file.close()

    

