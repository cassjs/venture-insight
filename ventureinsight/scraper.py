from bs4 import BeautifulSoup
from lxml import etree
import requests
import sqlite3

class VentureData:
    ## Scrape data from wefunder
    # def wefunder_scrape():
    #     companyname, description, highlights = ([] for i in range(3))
    #     soup = BeautifulSoup(requests.get('https://wefunder.com/explore').text,'html.parser')

    #     for i in soup.find_all(class_='live-update-company-name'): 
    #         companyname.append((i.text.replace('\n', '')).strip())
    #     # print(companyname)

    #     for i in soup.find_all(class_='tagline'): 
    #         description.append((i.text.replace('\n', '')).strip())
    #     # print(description)

    #     for i in soup.find_all(class_='desc-text'): 
    #         highlights.append((i.text.replace('\n', '')).strip())
    #     # print(highlights)

    #     # TODO: Scraping for links broken
    #     # dom = etree.HTML(str(soup))
    #     # res = (dom.xpath('//*[@class="company-url-bn"]/@href'))
    #     # for i in res:
    #     #     website.append('https://wefunder.com' + i)
    #     # print(website)

    #     return companyname, description, highlights

    # companyname, description, highlights = wefunder_scrape()

    ## Scrape data from seedinvest
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

    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        print('The database connection is open.')

        cursor.execute('''CREATE TABLE IF NOT EXISTS scrapeddata(companyname UNIQUE, description TEXT, highlights TEXT)''')
        connection.commit()
        print('The scrapeddata table has been created.')
        
        for company, description, highlights in zip(companyname, description, highlights):
            cursor.execute(f'''INSERT OR REPLACE INTO scrapeddata VALUES("{company}", "{description}", "{highlights}")''')
            connection.commit()
        print('New values have been inserted into the scrapeddata table.')
            
        ## Query the scrapeddata table from database
        sqlite_select_query = '''SELECT * FROM scrapeddata;'''
        cursor.execute(sqlite_select_query)
        print('Querying scrapeddata table from database.')
        
        ## Fetch all rows from scrapeddata table
        data = cursor.fetchall()
        print(data)

    except sqlite3.Error as error:
        print('Failed to read from scrapeddata table.', error)
    
    finally:
        if connection:
            connection.close()
            print('The database connection is closed.')