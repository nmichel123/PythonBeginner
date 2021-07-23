import random
import requests
from bs4 import BeautifulSoup

def scrapeWikiArticle(url):
    response = requests.get(
        url=url
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    #Pulls header element from page
    title = soup.find(id='firstHeading')
    print(title.string)

    #Get all links on page
    allLinks =  soup.find(id='bodyContent').find_all('a')
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        #Code to exclude non wikipedia links
        if link['href'].find('/wiki/') == -1:
            continue

        #Choose a random link to scrape
        linkToScrape = link
        break

    scrapeWikiArticle('https://en.wikipedia.org' + linkToScrape['href'])

scrapeWikiArticle('https://en.wikipedia.org/wiki/Muammar_Gaddafi')