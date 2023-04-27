# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapebgmeaPipeline:
    def process_item(self, item, spider):
        return item


class MailingAddressPipeline:

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        if adapter.get('mailing_address'):

            ma = adapter['mailing_address']

            ma1 = ma.split('Mailling Address</strong></th><td>')[-1].replace(', <br>', '<br>').split('<br>')[0]
            ma2 = ma.split('Mailling Address</strong></th><td>')[-1].split('<br>')[2].split('</td>')[0]

            adapter['mailing_address'] = ma1 + ", " + ma2

            return item
        
class DistrictPipeline:

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        if adapter.get('district'):

            d = adapter['district'].split('Mailling Address</strong></th><td>')[-1].split('<br>')[1]

            adapter['district'] = d

            return item
        
class NoEmployeesPipeline:

    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        if adapter.get('no_employees'):

            splitted = adapter['no_employees'].split(',')
            n = int(len(splitted)/2)

            total = 0

            for i in range(n):

                total += int(splitted[i])

            adapter['no_employees'] = total

            return item