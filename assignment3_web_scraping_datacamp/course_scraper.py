import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

class CoursesSpider(scrapy.Spider):
    name = "courses"
    start_urls = [
                'https://www.datacamp.com/courses/tech:python',
                'https://www.datacamp.com/courses/tech:r',
    ]

    def parse(self, response):
        language = response.url.split(":")[-1]
 
        filename = 'courses'

        open(filename, 'w')

        with open(filename, 'a') as f:
            for course in response.css(".course-block__title::text"):
                f.write("" + language + ", ")
                f.write(course.get() + "\n")
        self.log('Saved file %s' % filename)

        for course in response.css(".course-block__title::text"):
            yield{
                "tech": course.get(),
                "language": language
            }

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(CoursesSpider)
process.start()

df = pd.read_csv("courses", names=["Language", "Tech"])

print(df)
