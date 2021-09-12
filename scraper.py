from bs4 import BeautifulSoup
import requests
from lxml import etree

def wefunder_scrape():
    companyname, description, website_url, highlights = ([] for i in range(4))
    soup = BeautifulSoup(requests.get('https://wefunder.com/explore').text,'html.parser')
    
    for i in soup.find_all(class_='live-update-company-name'): companyname.append((i.text.replace('\n', '')).strip())
    print(companyname)
    
    for i in soup.find_all(class_='tagline'): description.append((i.text.replace('\n', '')).strip())
    print(description)
    
    for i in soup.find_all(class_='desc-text'): highlights.append((i.text.replace('\n', '')).strip())
    print(highlights)
    
    dom = etree.HTML(str(soup))
    res = (dom.xpath('//*[@class="company-url-bn"]/@href'))
    
    for i in res:
        website_url.append('https://wefunder.com' + i)
    print(website_url)

def seedinvest_scrape():
    companyname, description, website_url, highlights = ([] for i in range(4))
    soup = BeautifulSoup(requests.get('https://www.seedinvest.com/offerings').text,'html.parser')
    
    for i in soup.find_all(class_='thumbnail-title'): companyname.append((i.text.replace('\n', '')).strip())
    print(companyname)
    
    for i in soup.find_all(class_='tagline'): description.append((i.text.replace('\n', '')).strip())
    print(description)
    
    for i in soup.find_all(class_='highlights'): highlights.append((i.text.replace('\n', '')).strip())
    print(highlights)
    
    # TODO: Scraping for links broken
    # for i in soup.find_all(class_='thumbnail-hero-image-wrapper'): website_url.get('a')['href']
    # print(website_url)
    
seedinvest_scrape()
wefunder_scrape()