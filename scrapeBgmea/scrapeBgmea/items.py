# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MemberItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    member_or_company_name = scrapy.Field()
    bgmea_reg_no = scrapy.Field()
    contact_person = scrapy.Field()
    email_address = scrapy.Field()
    mobile_number = scrapy.Field()
    mailing_address = scrapy.Field()
    district = scrapy.Field()
    no_employees = scrapy.Field()
    no_machines = scrapy.Field()
    product_capacity = scrapy.Field()
