import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

class CoursesSpider(scrapy.Spider):
    name = "courses"
    start_urls = [
                "https://w2.brreg.no/kunngjoring/kombisok.jsp?datoFra=01.01.2019&datoTil=01.02.2019&id_region=0&id_niva1=51&id_niva2=56&id_bransje1=0",
    ]

    def parse(self, response):
        date_from = response.url.split("&")[1]
        date_to = response.url.split("&")[2]
        course = course[:-7]
 
        filename = date_from + date_to

        # Count number of bankruptcies for the given month
        i = 0
        for field in response.css('tr[bgcolor="#FFFFFF"] td>p>a::text'):
            i += 1
        with open(filename, 'w') as f:
            f.write(str(i))
        self.log('Saved file %s' % filename)

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(CoursesSpider)
process.start()

df = pd.read_csv("dates", names=["Date", "Time", "Course", "Description", "Teacher"])

df.info()

print(df)
