import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup


file_soccer = 'Pinnacle_Soccer'
base_url = "https://www.pinnacle.com/"

#load browser driver
pin_driver = webdriver.Chrome()
pin_driver.get(base_url)

#parse page
new_soup = BeautifulSoup(pin_driver.page_source, 'lxml')
menu_soup = new_soup.find("li", class_="level-1 no-live ")

#search for soccer link and load page
league_soccer = menu_soup.find_all("a",onclick="return ewt.trackLink({name: 'Soccer', type:'click', link:this});")

for i in league_soccer:
    url_league = base_url+i.get('href')
    pin_driver.get(url_league)
    pin_driver.refresh()


# # #load each soccer league page
# for url_soccer in urls_soccer:
#     #load url
#     file_name_socc = (file_soccer +" " +url_soccer.text.strip() + ".csv").replace("/","-")
#     with open(file_name_socc, 'w') as f:
#         f.write("Section,Selection,Odds\n")
#     url_soccer_href = base_url+url_soccer.get('href')
#     print(url_soccer_href)
#     driver.get(url_soccer_href)
#     driver.refresh()
#     soup2 = BeautifulSoup(driver.page_source, 'lxml')
#     body_soup = soup2.find('body',class_="sport")
#     soup=body_soup.find('div',class_="main-outer").find('div',class_="main").find('div',id="game-page")   
#     #Parse betting page and extract all bets
#     # # Get Game Name
#     match_soccer = soup.find('h3', class_="name").text
#     #Find all Sections
#     sec_soccer = soup.find_all('div', class_="option option_fpw")
#     for i in sec_soccer:
#         # Get Section Name
#         sec_soccer_name = i.find('a', class_="js-state description").text
#         # #selection - 'td', class=c2 cnorder-selection
#         lines_socc = i.find_all('td', class_="c2 cnorder-selection")
#         odds_socc = i.find_all('td', class_="odds-fpw c3 cnorder-odds")
#         for x in range(len(lines_socc) -1):
#             with open(file_name_socc, 'a') as f:
#                 f.write(sec_soccer_name+","+lines_socc[x].text.strip()+","+odds_socc[x].span.text+"\n")

#pin_driver.close()
