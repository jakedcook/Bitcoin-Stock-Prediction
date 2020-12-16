#this is the final project 
from bs4 import BeautifulSoup
import requests

r = requests.get("https://api.scrapingdog.com/scrape?api_key=5fcfb0f0cf3cb873ffbe0766&url=https://finance.yahoo.com/chart/BTC-USD#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjEsImZsaXBwZWQiOmZhbHNlLCJ2b2x1bWVVbmRlcmxheSI6dHJ1ZSwiYWRqIjp0cnVlLCJjcm9zc2hhaXIiOnRydWUsImNoYXJ0VHlwZSI6ImxpbmUiLCJleHRlbmRlZCI6ZmFsc2UsIm1hcmtldFNlc3Npb25zIjp7fSwiYWdncmVnYXRpb25UeXBlIjoib2hsYyIsImNoYXJ0U2NhbGUiOiJsaW5lYXIiLCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6IkJUQy1VU0QiLCJjaGFydE5hbWUiOiJjaGFydCIsImluZGV4IjowLCJ5QXhpcyI6eyJuYW1lIjoiY2hhcnQiLCJwb3NpdGlvbiI6bnVsbH0sInlheGlzTEhTIjpbXSwieWF4aXNSSFMiOlsiY2hhcnQiLCLigIx2b2wgdW5kcuKAjCJdfX0sInNldFNwYW4iOm51bGwsImxpbmVXaWR0aCI6Miwic3RyaXBlZEJhY2tncm91bmQiOnRydWUsImV2ZW50cyI6dHJ1ZSwiY29sb3IiOiIjMDA4MWYyIiwic3RyaXBlZEJhY2tncm91ZCI6dHJ1ZSwicmFuZ2UiOm51bGwsInN5bWJvbHMiOlt7InN5bWJvbCI6IkJUQy1VU0QiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiQlRDLVVTRCIsInF1b3RlVHlwZSI6IkNSWVBUT0NVUlJFTkNZIiwiZXhjaGFuZ2VUaW1lWm9uZSI6IkV1cm9wZS9Mb25kb24ifSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsIjoiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOm51bGx9XSwiZXZlbnRNYXAiOnsiY29ycG9yYXRlIjp7ImRpdnMiOnRydWUsInNwbGl0cyI6dHJ1ZX0sInNpZ0RldiI6e319LCJzdHVkaWVzIjp7IuKAjHZvbCB1bmRy4oCMIjp7InR5cGUiOiJ2b2wgdW5kciIsImlucHV0cyI6eyJpZCI6IuKAjHZvbCB1bmRy4oCMIiwiZGlzcGxheSI6IuKAjHZvbCB1bmRy4oCMIn0sIm91dHB1dHMiOnsiVXAgVm9sdW1lIjoiIzAwYjA2MSIsIkRvd24gVm9sdW1lIjoiI2ZmMzMzYSJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJ3aWR0aEZhY3RvciI6MC40NSwiY2hhcnROYW1lIjoiY2hhcnQiLCJwYW5lbE5hbWUiOiJjaGFydCJ9fX19").text

soup = BeautifulSoup(r, 'html.parser')

alldata = soup.find_all("tbody")


try:
 table1 = alldata[0].find_all('tr')
except:
 table1= None
try:
 table2 = alldata[1].find_all('tr')
except:
 table2 = None

l={}
u=list()

for i in range(0,len(table1)):
 try:
   table1_td = table1[i].find_all('td')
 except:
   table1_td = None
 l[table1_td[0].text] = table1_td[1].text
 u.append(l)
 l={}


for i in range(0,len(table2)):
 try:
   table2_td = table2[i].find_all('td')
 except:
   table2_td = None
 l[table2_td[0].text] = table2_td[1].text
 u.append(l)
 l={}

 print(u)