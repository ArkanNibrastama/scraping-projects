import scrapy


class AgentspiderSpider(scrapy.Spider):
    name = "agentSpider"
    allowed_domains = ["www.usamls.net"]
    start_urls = ["https://www.usamls.net/riograndemls/default.asp?content=agents&menu_id=63743&the_letter=ALL&page=1"]

    def __init__(self):

        self.page = 1

    def parse(self, response):
        
        agents = response.css('table.agent_inside_link')

        for agent in agents:

            yield{

                "name" : agent.css('td:first-child div.agent_heading_inline::text').get(),
                "phone_number" : agent.css('td:first-child div.agent_info_inline::text').get(),
                "email" : agent.css('td:first-child div.agent_info_inline a::text').get(), 
                "office_name" : agent.css('td:last-child div.agent_heading_inline::text').get(),
                "office_number" : agent.css('td:last-child div:nth-child(3)::text').get(),
                "office_address1" : agent.css('td:last-child div:nth-child(4)::text').get(),
                "office_address2" : agent.css('td:last-child div.agent_info_inline span::text').getall(),
                "office_email" : agent.css('td:last-child div.agent_info_inline a::text').get()

            }

        self.page += 1

        if self.page <= 109 :

            yield scrapy.Request(f'https://www.usamls.net/riograndemls/default.asp?content=agents&menu_id=63743&the_letter=ALL&page={self.page}', callback=self.parse)