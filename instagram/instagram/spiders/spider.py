import scrapy
import json 
from scraper_user.items import UserItem
from scraper_user.items import PostItem

class InstagramSpider(scrapy.Spider):

    name = 'instagramspider'
    allowed_domains = ['instagram.com']
    start_urls = []

    def __init__(self):
        self.start_urls = ["https://www.instagram.com/_spataru/?__a=1"]

    def parse(self, response):
        # get the json file
        json_response = {}

        try:
            json_response = json.loads(response.body_as_unicode())
        except:
            self.logger.info('%s doesnt exist', response.url)
            pass
        if json_response["user"]["is_private"]:
            return
        # check if the username even worked
        try:
            json_response = json_response["user"]

            item = UserItem()

            # get User Info
            item["username"] = json_response["username"]
            item["follows_count"] = json_response["follows"]["count"]
            item["followed_by_count"] = json_response["followed_by"]["count"]
            item["is_verified"] = json_response["is_verified"]
            item["biography"] = json_response.get("biography")
            item["external_link"] = json_response.get("external_link")
            item["full_name"] = json_response.get("full_name")
            item["posts_count"] = json_response.get("media").get("count")
            