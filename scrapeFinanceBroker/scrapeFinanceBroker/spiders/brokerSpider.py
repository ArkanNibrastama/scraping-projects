import scrapy


class BrokerspiderSpider(scrapy.Spider):

    name = "brokerSpider"
    allowed_domains = ["www.mortgageandfinancehelp.com.au"]
    start_urls = ["https://www.mortgageandfinancehelp.com.au/find-accredited-broker/?page=1"]
    
    def __init__(self):

        self.page = 1
        

    def parse(self, response):
        
        brokers = response.css('div.broker-tile-body.standard')

        for broker in brokers:

            yield{

                "first name" : broker.css('a::attr(data-preferred_name)').get(),
                "last name" : broker.css('a::attr(data-last_name)').get(),
                "company" : broker.css('a::attr(data-company)').get(),
                "city" : broker.css('a::attr(data-city)').get(),
                "state" : broker.css('a::attr(data-state)').get(),
                "phone" : broker.css('a::attr(data-phone)').get(),
                "mobile phone" : broker.css('a::attr(data-mobile)').get(),
                "email" : broker.css('a::attr(data-email)').get()

            }

        self.page += 1
        print(f"scraping {self.page}th page")

        if self.page <= 506:

            yield scrapy.Request(f"https://www.mortgageandfinancehelp.com.au/find-accredited-broker/?page={self.page}", callback=self.parse)
