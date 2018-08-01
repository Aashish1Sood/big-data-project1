from bs4 import BeautifulSoup
import urllib2


#Scrape the wikipedia page to fetch the list of all science fiction movies released between 1920 and 2010
f = open('sci-fi_database.csv', 'w')
for i in range(1920,2011,10):
    wiki = "https://en.m.wikipedia.org/wiki/List_of_science_fiction_films_of_the_"+str(i)+"s"
    header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia
    year=""
    try:
        req = urllib2.Request(wiki,headers=header)
    except Exception as e:
        print wiki
        print e
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page,"html5lib")

    table = soup.find("table", { "class" : "wikitable" }) #fetches the table from the wiki page

    for row in table.findAll("tr"): #iterates thru all the rows of the table
        cells = row.findAll("td")
        headers = row.findAll("th")

        if len(cells) == 1:
            year = cells[0].find(text=True)
        elif len(headers)>0:
            f.write("year"+',')
            for header in headers:
                f.write(str(header.find(text=True)).replace(',',"")+',')
            f.write('\n')
        else:
            if i==1930:  #year 1930 is in a different format than others
                year=cells[2].find(text=True)[8:12]
            if i==1980 and cells[0].find(text=True).isdigit(): #year 1980 is in a different format than others
                year=cells[0].find(text=True)
            f.write(year+',')
            for cell in cells:
                try:
                    if cell.find(text=True).isdigit():
                        continue
                    f.write(str(cell.find(text=True).encode('utf-8')).replace(',',"") + ',')
                except:
                    f.write(',')
            f.write('\n')

