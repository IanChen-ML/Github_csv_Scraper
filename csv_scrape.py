from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import os

my_url = "https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks/data"
target_path = "/Users/chenyian/Documents/scrape_path"
#opening up the connection
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

fileLine = page_soup.findAll("div", {"role":"rowheader"})

#create a empty list to store our file names
ls=[] 
# the first a is useless, so start from index=1
for i in range(1, len(fileLine)):
    fileName = fileLine[i].a["title"]
    ls.append(fileName)

content = "https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/"
for j in ls:
    file_link = content + j
    df = pd.read_csv(file_link)
    df.to_csv(os.path.join(target_path,j), index=False)
