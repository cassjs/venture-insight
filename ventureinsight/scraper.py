from bs4 import BeautifulSoup
from lxml import etree
import requests
import sqlite3

class VentureData:
    
    # Scraped data for wefunder
    def wefunder_scrape():
        companyname, description, highlights = ([] for i in range(3))
        soup = BeautifulSoup(requests.get('https://wefunder.com/explore').text,'html.parser')

        for i in soup.find_all(class_='live-update-company-name'): 
            companyname.append((i.text.replace('\n', '')).strip())
        # print(companyname)

        for i in soup.find_all(class_='tagline'): 
            description.append((i.text.replace('\n', '')).strip())
        # print(description)

        for i in soup.find_all(class_='desc-text'): 
            highlights.append((i.text.replace('\n', '')).strip())
        # print(highlights)

        # TODO: Scraping for links broken
        # dom = etree.HTML(str(soup))
        # res = (dom.xpath('//*[@class="company-url-bn"]/@href'))
        # for i in res:
        #     website.append('https://wefunder.com' + i)
        # print(website)

        return companyname, description, highlights
    
    companyname, description, highlights = wefunder_scrape()

    # Scraped data for seedinvest
    def seedinvest_scrape():
        companyname, description, highlights = ([] for i in range(3))
        soup = BeautifulSoup(requests.get('https://www.seedinvest.com/offerings').text,'html.parser')

        for i in soup.find_all(class_='thumbnail-title'): 
            companyname.append((i.text.replace('\n', '')).strip())
        # print(companyname)

        for i in soup.find_all(class_='tagline'): 
            description.append((i.text.replace('\n', '')).strip())
        # print(description)

        for i in soup.find_all(class_='highlights'): 
            highlights.append((i.text.replace('\n', '')).strip())
        # print(highlights)

        # TODO: Scraping for links broken
        # for i in soup.find_all(class_='thumbnail-hero-image-wrapper'): website.get('a')['href']
        # print(website)

        return companyname, description, highlights

    companyname, description, highlights = seedinvest_scrape()

    # Open database connection
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    print("Connecting to database ...")

    # Create database table 'scrapeddata' 
    c.execute('''CREATE TABLE IF NOT EXISTS scrapeddata(companyname TEXT, description TEXT, highlights TEXT)''')
    conn.commit()
    print("Created 'scrapeddata' table in database ...")
            
    # Insert scraped values into database under scrapeddata table
    for company, description, highlights in zip(companyname, description, highlights):
        c.execute(f'''INSERT INTO scrapeddata VALUES("{company}", "{description}", "{highlights}")''')
        conn.commit()
        # # TEST ONLY:
        # print(company)
        # print(f'''INSERT INTO scrapeddata VALUES("{company}", "{description}", "{highlights}")''')

    # # TEST ONLY: Preview values inserted into 'scrapeddata' table
    # def select_all_data(cur):
    #     cur.execute("SELECT * FROM scrapeddata")
    #     rows = cur.fetchall()
    #     for row in rows:
    #         print(row)

    # select_all_data(cur=c) 