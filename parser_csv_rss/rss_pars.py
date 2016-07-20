# -*- coding: utf-8 -*-
"""
   RSS parser:
   - Grabs the rss feed: title, link, description, published, 
     links.image and returns them as a list of dict;
   - Parses the link url, grabs: title, image, content and 
     returns them as a dict

"""

import feedparser
import requests
from lxml import html


class Lenta():
    """
        RSS parser - consist of two methods.
        1. news - gets limit(5) number of the last news
        2. grub - parses the link url and gets content data from it
        
    """

    def __init__(self):
        # A list to hold all news
        self.news_data = []
        self.images = []
        self.grub_data = {}
        # List of RSS feeds that we will fetch and combine
        self.newsurls = {
            'lenta.ru':                'http://lenta.ru/rss',
            'www.interfax.ru':         'http://www.interfax.ru/rss.asp',
            'www.kommersant.ru':       'http://www.kommersant.ru/RSS/news.xml',
            'www.m24.ru':              'http://www.m24.ru/rss.xml',
        }
     
    def parseRSS(self, rss_url):
        '''
            Method to fetch the rss feed and return the parsed RSS

        '''
        return feedparser.parse(rss_url) 
        
    # Function 
    def news(self, limit = 5):
        """
            Grabs the rss feed: title, link, description, published, links.image
            and returns them as a list of dict

        """        
        news_data = []
        # Iterate over the feed urls
        for key, url in self.newsurls.items():
            rss = self.parseRSS(url)        
            
            for i in xrange(limit):
                temp_dict = {}
                # Collects data from rss
                temp_dict['title'] = rss.entries[i].title.encode('utf8')
                temp_dict['link'] = rss.entries[i].link.encode('utf8')
                temp_dict['desc'] = rss.entries[i].description.encode('utf8')
                temp_dict['published'] = rss.entries[i].published.encode('utf8')
                # Takes image url from rss
                for image in rss.entries[i].links:
                    if image['type'] == 'image/jpeg':
                        self.images.append(image['href'])
                    else:
                        self.images.append('None')
    
                self.news_data.append(temp_dict)
        
        return self.news_data

    def grub(self, link):
        """
            Parses the link url, grabs: title, image, content 
            and returns them as a dict
            
        """
        for i in xrange(len(self.news_data)):
            if self.news_data[i]['link'] == link:
                self.grub_data['image'] = self.images[i]
                self.grub_data['title'] = self.news_data[i]['title']
        #Gets html text from link
        s = requests.Session()
        d = s.get(link)
        tree = html.fromstring(d.text)

        keys = [key for key in self.newsurls.keys()]
        # Check the domain name for finding key
        dom_name = link.split('/')
        content = ''
        # parsing link url
        if dom_name[2] == 'lenta.ru':
            text = tree.xpath(".//*[@id='root']/div[2]/div/div[1]/div[1]/div/div[1]/div[2]/p/text()")
            for x in text:
                content += x
            self.grub_data['content'] = content.encode('utf8')

        elif dom_name[2] == 'www.interfax.ru':
            text = tree.xpath(".//*[@class='at']/p/text()")
            for x in text:
                content += x
            self.grub_data['content'] = content.encode('utf8')
            
        elif dom_name[2] == 'www.kommersant.ru':            
            text = tree.xpath(".//*[@id='divLetterBranding']/p/text()")
            for x in text:
                content += x
            self.grub_data['content'] = content.encode('utf8')

        elif dom_name[2] == 'www.m24.ru':
            text = tree.xpath(".//*[@class='b-material']/text()")
            for x in text:
                content += x.strip()
            self.grub_data['content'] = content.encode('utf8')            


        return self.grub_data


if __name__ == '__main__':

    lenta = Lenta()
    news = lenta.news(limit = 5)
    print news  
    data = lenta.grub(news[0]['link'])
    print data