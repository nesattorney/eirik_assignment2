import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

class CoursesSpider(scrapy.Spider):
    name = "courses"
    start_urls = [
                "http://timeplan.uit.no/emne_timeplan.php?sem=20h&module%5B%5D=BED-2056-1&View=list",
    ]

    def parse(self, response):
        course = response.url.split("=")[-2]
        course = course[:-7]
 
        filename = 'dates'

        open(filename, 'w')

        i = 0
        delimiter = ", "
        with open(filename, 'a') as f:
            for field in response.css("td ::text"):
                if (i % 7) == 6:
                    delimiter = "\n"
                elif (i % 7) == 4:
                    delimiter = " & "
                elif (i % 7) == 0:
                    delimiter = " "
                else:
                    delimiter = ", "
                f.write(field.get() + delimiter)
                i += 1
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
