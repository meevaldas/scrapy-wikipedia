import scrapy
from scrapy.crawler import CrawlerProcess

from wikipedia.spiders.splash import SplashSpider


def main():
    process = CrawlerProcess(
        settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        }
    )

    process.crawl(SplashSpider)
    process.start()  # the script will block here until the crawling is finished


if __name__ == "__main__":
    main()
