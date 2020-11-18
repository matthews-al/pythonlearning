""" Quote scraping excercise - Section 15
Base URL: http://quotes.toscrape.com/page/1/

End goal - Get a list of authors on the site
Extended - Unique tags
"""

from collections import Counter
import requests
import bs4

# Page base URL
BASEURL = "http://quotes.toscrape.com/page/{}/"

def get_page(num):
    """ Get one page from the site.
    Return a tupple:
        bool:  Page had content
        bs4 parsed object
    """
    result = requests.get(BASEURL.format(num))
    soup = bs4.BeautifulSoup(result.text, "lxml")
    if len(soup.select('.quote')) == 0:
        return True, soup
    return False, soup

def get_list(soup, selector):
    """ Return a list of authors found on a page """
    sel = soup.select(selector)
    items = (item.text for item in sel)
    return items

if __name__ == "__main__":
    page = 0
    authors = Counter()
    (end, tent) = get_page(1)
    toptags = get_list(tent, '.tag-item > a')
    print(list(toptags))
    while page := page + 1:
        (end, tent) = get_page(page)
        authors.update(get_list(tent, '.quote .author'))
        if end:
            break
    print(authors)
