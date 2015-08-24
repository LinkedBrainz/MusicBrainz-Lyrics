#!/usr/bin/env python 

import sys, re, requests
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf8')

with open('work-withLyrics.nt') as file:
    for line in file:
        if '<http://purl.org/ontology/mo/lyrics> <http://lyrics.wikia.com/' in line:
            uuid = re.match('<http://musicbrainz.org/work/([^#]+)#_>', line).group(1)
            uri = re.search('http://lyrics.wikia.com/[^>]+', line).group(0)
            print 'Retrieving: ' + uri
            html = etree.HTML(requests.get(uri).text)
            lyrics = html.xpath('//div[@class="lyricbox"]/text()')
            file = open(uuid + '.txt', 'w')
            file.write('\n'.join(lyrics))
            file.close()
