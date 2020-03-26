import requests
from bs4 import BeautifulSoup
import pprint

respond = requests.get('https://news.ycombinator.com/news')
respond2 = requests.get('https://news.ycombinator.com/news?p=2')

Beautiful_Soup = BeautifulSoup(respond.text, 'html.parser')
Beautiful_Soup2 = BeautifulSoup(respond2.text, 'html.parser')

page_links = Beautiful_Soup.select('.storylink')
page_links2 = Beautiful_Soup2.select('.storylink')
page_subtext = Beautiful_Soup.select('.subtext')
page_subtext2 = Beautiful_Soup2.select('.subtext')

page_megalinker = page_links + page_links2
page_megalinker2 = page_subtext + page_subtext2

def sort_by_votes(hnlist):
  return sorted(hnlist, key= lambda x:x['votes'], reverse = True)

def create_custom_scrap(links, subtext):
  scraped_hackernews = []
  for index, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[index].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        scraped_hackernews.append({'title': title, 'link': href, 'votes': points})
  return sort_by_votes(scraped_hackernews)
 
pprint.pprint(create_custom_scrap(page_megalinker, page_megalinker2))