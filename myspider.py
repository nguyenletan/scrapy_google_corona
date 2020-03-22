import scrapy


class CoronaSpider(scrapy.Spider):
    name = 'CoronaSpider'
    start_urls = ['https://google.org/crisisresponse/covid19-map/']
    
    def parse(self, response):
        i = 0
        for td in response.css('.table_scroll tr'):
            country_name = td.css('td.table_card_cell_col_0 > span ::text').get()
            confirmed_cases = td.css('td.table_card_cell_col_1 ::text').get()
            cases_per_1_million_people = td.css('td.table_card_cell_col_2 ::text').get()
            recovered = td.css('td.table_card_cell_col_3 ::text').get()
            deaths = td.css('td.table_card_cell_col_4 ::text').get()
            if country_name is not None:
                result = {
                    'id'                        : i,
                    'country_name'              : country_name.strip(),
                    'confirmed_cases'           : confirmed_cases.strip(),
                    'cases_per_1_million_people': cases_per_1_million_people.strip(),
                    'recovered'                 : recovered.strip(),
                    'deaths'                    : deaths.strip()
                }
                i = i + 1
                yield result
