import scrapy
from scrapeBgmea.items import MemberItem
from scrapeBgmea.itemsholder import MemberItemLoader

class MemberspiderSpider(scrapy.Spider):
    name = "memberSpider"
    allowed_domains = ["www.bgmea.com.bd"]
    start_urls = ["https://www.bgmea.com.bd/page/member-list?page=1"]

    def __init__(self):

        self.page = 1

    def parse(self, response):
        
        members = response.css('table tbody tr')

        for member in members:

            detail_url = member.css('a.btn.btn-sm.btn-info::attr(href)').get()
            yield scrapy.Request(detail_url, callback=self.scrape_detail)

        self.page += 1

        if self.page <= 186:

            yield scrapy.Request(f"https://www.bgmea.com.bd/page/member-list?page={self.page}", callback=self.parse)



    def scrape_detail(self, response):

        member_detail = response.css('div.row')

        load_member = MemberItemLoader(item=MemberItem(), selector=member_detail)

        load_member.add_css('member_or_company_name', 'table th strong::text')
        load_member.add_css('bgmea_reg_no', 'div.my-2.profile-values [id="company_info"] table tr:first-child td::text')
        load_member.add_css('contact_person', 'div.my-2.profile-values [id="company_info"] table tr:last-child table tbody td:nth-child(2)::text')
        load_member.add_css('email_address', 'div.my-2.profile-values [id="company_info"] table tr:last-child table tbody td:last-child::text')
        load_member.add_css('mobile_number', 'div.my-2.profile-values [id="company_info"] table tr:last-child table tbody td:nth-child(3)::text')
        load_member.add_css('mailing_address', 'div.my-2.profile-values [id="address_info"] table tbody')
        load_member.add_css('district', 'div.my-2.profile-values [id="address_info"] table tbody')
        load_member.add_css('no_employees', 'div.my-2.profile-values [id="final_info"] tr:nth-child(4) tr td::text')
        load_member.add_css('no_machines', 'div.my-2.profile-values [id="final_info"] tr:nth-child(5) td::text')
        load_member.add_css('product_capacity', 'div.my-2.profile-values [id="final_info"] tr:nth-child(6) td::text')

        yield load_member.load_item()

