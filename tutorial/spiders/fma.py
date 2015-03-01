# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import TutorialItem

class FmaSpider(scrapy.Spider):
    name = "fma"
    allowed_domains = ["freemusicarchive.org"]
    start_urls = (
        'http://freemusicarchive.org/genre/Classical/?sort=track_date_published&d=1&page=1',
        'http://freemusicarchive.org/genre/Classical/?sort=track_date_published&d=1&page=2',
        'http://freemusicarchive.org/genre/Classical/?sort=track_date_published&d=1&page=3',
    )

    def parse(self, response):
        for sel in response.xpath("//div[contains(@class, 'play-item')]"):
            item = TutorialItem()
            item['artist'] = sel.xpath(".//span[@class='ptxt-artist']/b/a/text()").extract()
            item['track']  = sel.xpath(".//span[@class='ptxt-track']/a/b/text()").extract()
            item['album']  = sel.xpath(".//span[@class='ptxt-album']/a/b/text()").extract()
            
            yield item