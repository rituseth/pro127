

from bs4 import BeautifulSoup as bs 
import time 
import csv 
#from selenium import webdriver
import pandas as pd
import requests 
 

Starturl = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
#browser = webdriver.Chrome('C:/Users/RITU.000/Desktop/vidhi seth/whitHat/chromedriver')
browser = requests.get(Starturl)
print(browser)
time.sleep(10)


  
  #finding all the url tags with class exoplanet 
  
soup = bs(browser.text , "html.parser") 

startable = soup.find("table")
templist = []
tablerow = startable.find_all("tr")
for tr in tablerow : 
  td = tr.find_all("td")
  row = [i.text.rstrip( ) for i in td]
  templist.append(row)
  
  
starnames = []
distance = []  
mass =[]
radius = []
lum = []

for i in range(1 , len(templist)): 
  starnames.append(templist[i][1])
  distance.append(templist[i][3])
  mass.append(templist[i][5])
  radius.append(templist[i][6])
  lum.append(templist[i][7])
  
df = pd.DataFrame(list(zip(starnames , distance , mass , radius , lum)) , 
                  columns=["starname" , "distance" , "mass" , "radius" , "luminosity"])
print(df)
df.to_csv("stars2.csv")
