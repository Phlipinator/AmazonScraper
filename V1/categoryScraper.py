import requests
from bs4 import BeautifulSoup
import pandas as pd

# TODO: Iterate trough list of search queries and assign the category by using the search term 


# Define the header, so that the website doesn't block the access
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


# Send the request
def getData(url):
    r = requests.get(url, headers=HEADERS)
    return r.text


# Convert data into HTML code and parse it
def html_code(url):

    # pass the url into getData function
    htmlData = getData(url)
    soup = BeautifulSoup(htmlData, 'html.parser')

    return (soup)


def getASIN(soup):
    className = "sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"
    data_str = []

    for item in soup.find_all("div", class_ = className):
        data_str.append(item['data-asin']) 

    return (data_str)

# https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A679255011&page=2&language=de&qid=1673108531&ref=sr_pg_2
urlPart_1 = "https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A679255011&page="
urlPart_2 = "&language=de&qid=1673108531&ref=sr_pg_2"

numberOfPages = 5

for index in range(1,numberOfPages):
    url = urlPart_1 + str(index) + urlPart_2

    #url = "https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A2476517011&dc&language=de&ds=v1%3Awyiu%2BruC5w8pQke599cKdJWGGiPxg8TDN9BiH8EeFw0&qid=1673097785&rnid=1040658&ref=sr_nr_n_1"
    soup = html_code(url)

    #print(getASIN(soup))

    data = {'ASIN': getASIN(soup) }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save the output.
    df.to_csv('shoes.csv', mode = 'a', index= False, header=False)

