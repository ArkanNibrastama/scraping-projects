# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Scrapeimdbtop1000Pipeline:
    def process_item(self, item, spider):
        return item
        

class StarsPipeline:

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        if adapter.get('stars'):

            adapter['stars'] = ", ".join(adapter['stars'].split(', ')[:5])

            return item