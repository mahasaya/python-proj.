#pip install request
#pip install bs4 
#pip install 
import requests
from bs4 import BeautifulSoup

url= "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2019;trophy=12;type=season"

 #get the html

r =  requests.get(url)
htmlContent = r.content
print(htmlContent) 

# parse the html

soup = BeautifulSoup(htmlContent , 'html.parser')
print(soup.prettify)

#tree ko traverse krengai jo cheez chahiye vo yhi se niklega 




