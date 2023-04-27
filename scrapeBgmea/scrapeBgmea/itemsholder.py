from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst, Join

class MemberItemLoader(ItemLoader):

    default_input_processor = Join(',')
    default_output_processor = TakeFirst()

    member_or_company_name_in = MapCompose(lambda x : x.split(',')[0])
    bgmea_reg_no_in = MapCompose(lambda x : x.split(',')[0])
    email_address_in = MapCompose(lambda x : x.split(',')[0])
    mobile_number_in = MapCompose(lambda x : x.split(',')[0])
    contact_person_in = MapCompose(lambda x : x.split(',')[0])
    no_machines_in = MapCompose(lambda x : x.split(',')[0])
    product_capacity_in = MapCompose(lambda x : x.split(',')[0])
    mailing_address_in = MapCompose(lambda x : x.replace('\t', '').replace('\n',''))
    district_in = MapCompose(lambda x : x.replace('\t', '').replace('\n',''))
