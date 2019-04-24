# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    username = scrapy.Field()
    follows_count = scrapy.Field()
    followed_by_count = scrapy.Field()
    is_verified = scrapy.Field()
    biography = scrapy.Field()
    external_link = scrapy.Field()
    full_name = scrapy.Field()
    posts_count = scrapy.Field()
    posts = scrapy.Field()

class PostItem(scrapy.Item):
    code = scrapy.Field()
    likes = scrapy.Field()
    thumbnail = scrapy.Field()
    hashtags = scrapy.Field()
    
    
