from scrapers.scraper_craigslist import *

def main():
    s = CraigslistScraper(6)
    entries = s.scrape()
    for e in entries:
        print(e)

if __name__ == "__main__":
    main()
    