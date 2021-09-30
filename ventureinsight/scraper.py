from bs4 import BeautifulSoup
from lxml import etree
import requests
import sqlite3

class VentureData:
    def web_scrape():
        companyname, description, highlights, website = ([] for i in range(4))
        
        ## --------- WEBSITE #1 ---------
        soup = BeautifulSoup(requests.get('https://www.seedinvest.com/offerings').text,'html.parser')

        for i in soup.find_all(class_='thumbnail-title'): 
            companyname.append((i.text.replace('\n', '')).strip())
        
        for i in soup.find_all(class_='tagline'): 
            description.append((i.text.replace('\n', '')).strip())
        
        for i in soup.find_all(class_='highlights'): 
            highlights.append((i.text.replace('\n', '')).strip())

        dom = etree.HTML(str(soup))
        res = (dom.xpath('//*[@class="thumbnail-hero-image-wrapper"]/@href'))
        for i in res:
            website.append('https://www.seedinvest.com' + i)

        ## --------- WEBSITE #2 ---------
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

        dom = etree.HTML(str(soup))
        res = (dom.xpath('//*[@class="company-url-bn"]/@href'))
        for i in res:
            website.append('https://wefunder.com' + i)
        # print(website)

        return companyname, description, highlights, website
    
    companyname, description, highlights, website = web_scrape()
    
    ## DATABASE CONNECTIONS
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        print('The database connection is open.')

        cursor.execute('''CREATE TABLE IF NOT EXISTS scrapeddata(companyname UNIQUE, description TEXT, highlights TEXT, website TEXT)''')
        connection.commit()
        print('The scrapeddata table has been created.')
        
        for company, description, highlights, website in zip(companyname, description, highlights, website):
            cursor.execute(f'''INSERT OR REPLACE INTO scrapeddata VALUES("{company}", "{description}", "{highlights}", "{website}")''')
            connection.commit()
        print('New values have been inserted into the scrapeddata table.')
        
        # ## TEST ONLY:
        # ## Query the scrapeddata table from database
        # sqlite_select_query = '''SELECT * FROM scrapeddata ORDER BY companyname ASC'''
        # cursor.execute(sqlite_select_query)
        # print('Querying scrapeddata table from database.')
        # ## Fetch all rows from scrapeddata table
        # data = cursor.fetchall()
        # print(data)

    except sqlite3.Error as error:
        print('Failed to read from scrapeddata table.', error)
    
    finally:
        if connection:
            connection.close()
            print('The database connection is closed.')