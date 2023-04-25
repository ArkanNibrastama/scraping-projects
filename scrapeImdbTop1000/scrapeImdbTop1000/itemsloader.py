from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst, Join

class MovieItemLoader(ItemLoader):

    default_input_processor = Join(', ')
    default_output_processor = TakeFirst()