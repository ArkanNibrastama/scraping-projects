import scrapy
from scrapeImdbTop1000.items import MovieItem
from scrapeImdbTop1000.itemsloader import MovieItemLoader

class MoivespiderSpider(scrapy.Spider):
    name = "movieSpider"
    allowed_domains = ["m.imdb.com"]
    start_urls = ["https://m.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc"]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):
        
        movies = response.css('div.lister-item.mode-advanced')

        for movie in movies:

            detail_link = movie.css('h3.lister-item-header a::attr(href)').get()
            yield scrapy.Request("https://m.imdb.com"+detail_link, callback=self.scrapeDetail)

        next_page_url = response.css('a.lister-page-next.next-page::attr(href)').get()

        if next_page_url is not None:
    
            yield scrapy.Request("https://m.imdb.com"+next_page_url, callback=self.parse)

    def scrapeDetail(self, response):

        section = response.css('section.ipc-page-background.ipc-page-background--base.sc-f9e7f53-0.ifXVtO')
        load_movie = MovieItemLoader(item=MovieItem(), selector=section)

        load_movie.add_css('title', 'span.sc-afe43def-1.fDTGTb::text')
        load_movie.add_css('genre', 'div.ipc-chip-list__scroller a::text')
        load_movie.add_css('director', 'div.sc-52d569c6-3.jBXsRT ul li:first-child div ul li a::text')
        load_movie.add_css('stars', 'div.sc-bfec09a1-7.dpBDvu a::text')
        load_movie.add_css('year','div.sc-52d569c6-0.kNzJA-D ul li:first-child a::text')

        yield load_movie.load_item()