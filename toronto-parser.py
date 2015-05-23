from lxml import html
import requests

for x in range(5,12):

    pageUrl =  "http://events.seetorontonow.com/calendar/month/2015/" + str(x)
    page = requests.get(pageUrl)
    tree = html.fromstring(page.text)

    events = []
    counter = 0
    for atag in tree.xpath('//div[@class="item event_item vevent"]'):
        events.append(atag.xpath('//span/abbr/@title')[counter])
        events.append(atag.text_content().strip())
        counter = counter + 1
    
    eventFile = "events_month_of_" + str(x) + ".txt"
    file = open(eventFile,"w")
    for event in events:
        encoded = event.encode('utf-8')
        print >> file, encoded
        print >> file, '\n'

    file.close()
