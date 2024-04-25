from scrapers.Property import Property
from scrapers.Scraper import Scraper
from requests.models import PreparedRequest

# scrapers container helper functions followed by scraping code will called by Scrapper.scrape()
class  CraigslistScraper(Scraper):
    def __init__(self, rooms):
        self.name = "craigslist scraper"
        self.htmlclass = "cl-app-anchor text-only posting-title"
        self.rooms = rooms

    def scrape(self):
        import requests
        # get entries with filters
        params = {'hasPic': '1', 'max_bedrooms': self.rooms, 'min_bedrooms': self.rooms, "rent_period": "3"}

        response = requests.get('https://vancouver.craigslist.org/search/bnc/apa?#search=1~gallery~0~60', params=params)

        # get entry information here
        from bs4 import BeautifulSoup

        html_soup = BeautifulSoup(response.text, 'html.parser')

        entryPages = [] # entryPages are URLs of each possible entry
        # get all values and init Property objects
        posts = html_soup.find_all('a', href=True)
        #print(posts)
        for post in posts:
            if len(post.get("href")) > 20:
                response = requests.get(post.get("href"))
                html_soup = BeautifulSoup(response.text, "html.parser")
                loc = html_soup.find('div', id="map")
                property = Property(post.get("price"), self.rooms, post.get("href"))
                property.setLocation(loc.get("data-latitude"), loc.get("data-longitude"))
                entryPages += [property]
        return entryPages
