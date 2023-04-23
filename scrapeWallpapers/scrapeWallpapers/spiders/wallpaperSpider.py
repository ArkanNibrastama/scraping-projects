import scrapy


class WallpaperspiderSpider(scrapy.Spider):
    name = "wallpaperSpider"
    allowed_domains = ["designs.colefax.com"]
    page = 1
    start_urls = [f"https://designs.colefax.com/Search/W/Brand/C/Colour/All/Use/All/Category/All/SubType/F:All,T:All,W:All/New/1/Page/{page}"]

    def parse(self, response):
        
        wallpapers = response.css('[class="item new"]')

        for wallpaper in wallpapers:

            link = "https://designs.colefax.com"+wallpaper.css('p.title a.name::attr(href)').get()
            yield scrapy.Request(link, callback=self.parse_detail)

    def parse_detail(self, response):   

        stockcode = response.css('a.active::attr(href)').get().split('/')[-1]

        if 'W' not in stockcode:

            stockcode = stockcode.replace('-','/')

        details = response.css(f'[data-stockcode="{stockcode}"] div.details p::text').getall()

        yield{

            "name" : response.css('h1.name::text').get().split(' by')[0],
            "brand" : details[1],
            "code" : details[3],
            "color" : details[5],
            "repeat" : details[7],
            "roll size" : details[9],
            "composiotion" : details[11],
            "care code" : details[13].replace('\r\n                        ',''),
            "pattern book" : details[15],
            "image" : response.css(f'[data-stockcode="{stockcode}"] img::attr(src)').get()

        }
            
