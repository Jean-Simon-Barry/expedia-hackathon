# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from lxml import html
import six
nodes = """ <div class="item event_item vevent" id="event_instance_994286">
    <a href="http://events.seetorontonow.com/event/the_physicists"><img alt="The Physicists" class="img_medium" height="80" src="http://images-cf.localist.com/photos/235438/medium/4ec837e96d687768fba39e0047dbb73e12e30971.jpg" title="The Physicists" width="80" /></a>
    <div class="item_content_medium">
      <h3>
        <span class="summary">
          <a href="http://events.seetorontonow.com/event/the_physicists">The Physicists</a>
        </span>
        <span class="dateright">
          <abbr title="2015-06-01T00:00:00-05:00" class="dtstart">
            
          </abbr>
        </span>
      </h3>

      
        <h6><a href="http://events.seetorontonow.com/calendar/week?event_types%5B%5D=36151">Theatre &amp; Performing Arts</a></h6>
      
      <h4 class="description">Three inmates of an asylum are under investigation for murder – but who are they really? As funny as it is full of unexpected twists, this brilliant 1960s...</h4>      <h5>

<a href="http://events.seetorontonow.com/event/the_physicists" class="event_item_venue">Stratford Festival -- Stratford, Ontario</a>
        
        &nbsp;
      </h5>
    </div>
  </div>

 <div class="item event_item vevent" id="event_instance_1110232">
    <a href="http://events.seetorontonow.com/event/the_second_city_2015_spring_revue"><img alt="The Second City 2015 Spring Revue" class="img_medium" height="80" src="http://images-cf.localist.com/photos/249796/medium/d55f8313d43cfb128b6ecfaadb18dce6078c5088.jpg" title="The Second City 2015 Spring Revue" width="80" /></a>
    <div class="item_content_medium">
      <h3>
        <span class="summary">
          <a href="http://events.seetorontonow.com/event/the_second_city_2015_spring_revue">The Second City 2015 Spring Revue</a>
        </span>
        <span class="dateright">
          <abbr title="2015-06-01T00:00:00-04:00" class="dtstart">
            
          </abbr>
        </span>
      </h3>

      
        <h6><a href="http://events.seetorontonow.com/calendar/week?event_types%5B%5D=36151">Theatre &amp; Performing Arts</a></h6>
      
      <h4 class="description">Prepare for a night of outrageous laughs. The Second City is excited to present our Spring 2015 Mainstage Revue - a wild collection of hilarious sketches,...</h4>
      <h5>
        
          <a href="http://events.seetorontonow.com/the_second_city" class="event_item_venue">The Second City</a>
        
        &nbsp;
      </h5>
    </div>
  </div>
"""

tree = html.fromstring(nodes.encode('utf-8'))
events = []
counter = 0;
for atag in tree.xpath('//div[@class="item event_item vevent"]'):

    print(atag.xpath('//span/abbr/@title')[counter])
    events.append(atag.text_content().strip())
    counter = counter + 1
#print(events)
