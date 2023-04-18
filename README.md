# BeautifulSoup and Requests Python Web Scraping

This is an individual passion project that I used as an introduction to Python
and many libraries such as BeautifulSoup and Requests. The program scrapes
the top 100 fantasy books from the TIME and then uses their titles to scrape 
their ISBNs from a ISBN catalogue. 

### Required Libraries:
- Numpy
- Requests
- CSV
- BS4

The original goal of this project was to build up skills in Python and common data analytics tools and strategies. Building these tools, I am now closer to starting a 
career in the field of Data. 

The steps of the code are:
1. The html code is scraped from the webpage, This code contains all of the information that I want to scrape from the page.
2. This html code is not readible or easily traversable so I used BeautifulSoup to allow me
to traverse the html, searching for the information that I need to scrape. 
3. From the TIME page I get the Title, Author, and TIME Link to the page. I use the scraped title to build a URL to scrape the ISBN from on another webpage. 
4. All of this information is then entered into a .csv file with headers for distinctions. 
You can find this .csv file in the repository as well. 
5. These steps are repeated for all 100 books on the list. 

There are plans for adding additional information, i.e. ratings, which is why I scraped the IBSN but those are not complete yet.
