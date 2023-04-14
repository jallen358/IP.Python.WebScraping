#!/usr/bin/env python
"""
Uses Requests and BeautifulSoup to Scrape the 100 best books
from the times article 'The 100 Best Fantasy Books of All Time'

In-Progress:
- Book Summary
- More Book Information:
    - Publish Date/Location etc.
(Both require new Req and BS)
- Potential Path:
    https://stackoverflow.com/questions/40629457/scrape-multiple-urls-using-beautiful-soup
    for url in urls

- Reformatting Results
    - Current Format is 2 Arrays
        [links] and [titles]
    - Use 2D array:
        [Title][Link]
    - Add all links and Titles to 1 Array and then split:
        ['Title', 'Link', 'Title', 'Link']
        - Make this 2D?
        [
            [Title, Link]
            [Title, Link]
        ]
    - Final Result: 
        - Get rid of 2D array and just add to the CSV every loop
        - May create issues when trying to do 2 loops


    - Got results for ISBN
"""
import numpy as np
import requests
import csv
from bs4 import BeautifulSoup as BS

_author__ = "Jason Allen"

__version__ = "7.1.2"
__maintainer__ = "Jason Allen"
__email__ = "jasonhlallen@gmail.com"
__status__ = "Development"


def getdata(url):
    r = requests.get(url)
    if r.status_code != 200:
        print('Status Code: ', r.status_code)
        raise Exception('Failed to get soup')
    return r.text


def html_code(url):
    page = getdata(url)
    soup = BS(page, "html.parser")
    return soup


def book_data(soup):
    data_str = ""
    for item in soup.find_all("strong", class_="section-list section-list--standard"):
        data_str = data_str + item.get_text()
    result_1 = data_str.split("\n")
    return (result_1)


def write_csv(items, path):
    with open(path, 'w') as fp:
        if len(items) == 0:
            return

        headers = list(items[0].keys())
        fp.write(','.join(headers) + '\n')

        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            fp.write(','.join(values) + '\n')


def read_csv(path):
    with open(path, 'r') as fp:
        fp = fp.read()
    return fp


def create_list():
    return


def deep_data(url):
    return


if __name__ == "__main__":

    url = "https://time.com/collection/100-best-fantasy-books/"

    soup = html_code(url)
    books = soup.find_all("li", class_="section-list__item")
    
    holder = []
    i = 0
    j = 0
    titles = []
    isbn = []
    headers = ['Title', 'Author', 'Link', 'ISBN']
    with open('books.csv', 'w') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        for book in books:
            link = book.find('a').get('href')
            info = book.find('h3', class_="section-list__item-headline").text.strip()

            #print(title)
            #print(link)
            info = info.rsplit(' by ', 1)
            #print(info)
            title = info[0]
            if j != 0 :
                
                titleURL = "https://bookscouter.com/search?query=" + title.replace(' ', '%20').replace('\'', '')
                r = requests.get(titleURL)
                soup = BS(r.content, 'html.parser')
                isbns = soup.find_all('span', class_='BookText_b1ofiyxa')
                if len(isbns) != 0:
                    isbn = isbns[2].text
                else:
                    isbn = []
            j = j+1
            author = []
            if  len(info) == 2:
                author = info[1]
                #book_array[i][1] = author

            #book_array[i][0] = title
            #book_array[i][2] = link
            holder = [title, author, link, isbn]

            writer.writerow(holder)


    # Creation of CSV
    
