from bs4 import BeautifulSoup
import requests
from lxml import etree

import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# # Create Table
# c.execute('''CREATE TABLE scrapeddata(companyname TEXT, description TEXT, highlights TEXT)''')
# conn.commit()

def wefunder_scrape():
    companyname, description, highlights = ([] for i in range(4))
    soup = BeautifulSoup(requests.get('https://wefunder.com/explore').text,'html.parser')

    for i in soup.find_all(class_='live-update-company-name'): companyname.append((i.text.replace('\n', '')).strip())
    # print(companyname)

    for i in soup.find_all(class_='tagline'): description.append((i.text.replace('\n', '')).strip())
    # print(description)

    for i in soup.find_all(class_='desc-text'): highlights.append((i.text.replace('\n', '')).strip())
    # print(highlights)

    # dom = etree.HTML(str(soup))
    # res = (dom.xpath('//*[@class="company-url-bn"]/@href'))

    # for i in res:
    #     website.append('https://wefunder.com' + i)
    # print(website)

    return companyname, description, hightlights

def seedinvest_scrape():
    companyname, description, website, highlights = ([] for i in range(4))
    soup = BeautifulSoup(requests.get('https://www.seedinvest.com/offerings').text,'html.parser')

    for i in soup.find_all(class_='thumbnail-title'): companyname.append((i.text.replace('\n', '')).strip())
    # print(companyname)

    for i in soup.find_all(class_='tagline'): description.append((i.text.replace('\n', '')).strip())
    # print(description)

    for i in soup.find_all(class_='highlights'): highlights.append((i.text.replace('\n', '')).strip())
    # print(highlights)

    # TODO: Scraping for links broken
    # for i in soup.find_all(class_='thumbnail-hero-image-wrapper'): website.get('a')['href']
    # print(website)

    return companyname, description, highlights

companyname, description, hightlights = seedinvest_scrape()

for company, description, highlights in zip(companyname, description, hightlights):
    # Insert scraped data into database
    c.execute(f'''INSERT INTO scrapeddata VALUES("{company}", "{description}", "{highlights}")''')
    conn.commit()
    # print(company)
    # print(f'''INSERT INTO scrapeddata VALUES("{company}", "{description}", "{highlights}")''')

def select_all_data(cur):
    cur.execute("SELECT * FROM scrapeddata")

    rows = cur.fetchall()

    for row in rows:
        print(row)

select_all_data(cur=c) 