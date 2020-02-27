import scrapy


# from app.config.settings import BASE_DIR

# CHROME_DRIVER = os.path.join(BASE_DIR, 'festascraper', 'festascraper', 'chromedriver')


class QuotesSpider(scrapy.Spider):
    name = "festa-spider"
    start_urls = [
        'https://festa.io',
    ]

    def parse(self, response):
        title = response.css('h3.lpbKDy::text').getall()

        yield {
            'title': title
        }
