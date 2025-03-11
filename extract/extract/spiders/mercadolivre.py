import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/informatica/componentes-pc/placas/placas-video/usado/rtx-3060ti_NoIndex_True"]
    page_count = 1
    max_pages = 3

    def parse(self, response):

        products = products = response.css('div.ui-search-result__wrapper')

        for product in products:

            yield {

                'product_name': product.css('h3.poly-component__title-wrapper a::text').get(),
                'product_value': product.css('span.andes-money-amount__fraction ::text').get(),
                'product_condition': product.css('span.poly-component__item-condition ::text').get() 
            
            }

        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
