# File Name: IMDB Webcrawler.py
# Author: David Loi
# Date: 6/5/2018
# Purpose: To gather data on a number of movies from the IMDB website for a math CPT

from bs4 import BeautifulSoup
import requests
import xlwt

# Link to be searched
source = requests.get('https://www.imdb.com/search/title?title_type=feature&release_date=2009-01-01,2009-12-31').text

# Initializing lists
link_list = []
name_list = []
rating_list = []
budget_list = []
weekend_list = []
cumulative_gross_list = []
director_list = []

soup = BeautifulSoup(source, "html.parser")

# Obtaining links of all movies
for div in soup.find_all('div', class_="lister-item mode-advanced"):
    link_name = div.find('h3').a["href"]
    link_start = "http://www.imdb.com"
    link_full = link_start + link_name
    link_list.append(link_full)

# Obtaining names of all movies
for div1 in soup.find_all('div', class_="lister-item mode-advanced"):
    name = div1.find('h3').a.text
    name_list.append(name)

name_num = 0
for link in link_list:
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", "$", "£"]

    # Changing source to link of movie
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'html.parser')

    # Obtaining rating
    rating1 = soup.find('div', class_="ratingValue")
    rating = rating1.find('span').text
    rating_list.append(rating)

    # Obtaining budget
    details = soup.find(id="titleDetails")
    budget1 = details.find_all('div', class_="txt-block")
    budget2 = budget1[6].text
    budget = ""
    for i in budget2:
        if i in numbers:
            budget += i
    budget = budget.split(" ")
    if len(budget) == 0:
        budget.append("Missing")

    # Cleaning up certain figures that include the date at the end of the price
    if budget[0][-4:] == "2009":
        budget = budget[0][:-6]
    else:
        budget = budget[0]
    budget_list.append(budget)

    # Obtaining opening weekend profit
    weekend1 = budget1[7].text
    weekend = ""
    for i in weekend1:
        if i in numbers:
            weekend += i
    weekend = weekend.split(" ")
    if len(weekend) == 0:
        weekend.append("Missing")
    while weekend[0] == "":
        weekend = weekend[1:]

    # Cleaning up certain figures that include the date at the end of the price
    if weekend[0][-4:] == "2009" or weekend[0][-4:] == "2010":
        weekend = weekend[0][:-6]
    else:
        weekend = weekend[0]
    weekend_list.append(weekend)

    # Obtaining cumulative gross profit
    cumulative_gross1 = budget1[9].text
    cumulative_gross = ""
    for i in cumulative_gross1:
        if i in numbers:
            cumulative_gross += i
    cumulative_gross = cumulative_gross.split()
    if len(cumulative_gross) == 0:
        cumulative_gross.append("Missing")
    cumulative_gross_list.append(cumulative_gross[0])

    # Obtaining directors name
    director1 = soup.find('div', class_="credit_summary_item",)
    add = False
    director = ""
    for i in director1.find('a'):
        director = i
    director_list.append(director)

# Selecting excel file to write to
wb = xlwt.Workbook()
ws = wb.add_sheet("Movie Information")

# Initializing headers of each column
ws.write(0, 0, "Movie Names")
ws.write(0, 1, "Budget")
ws.write(0, 2, "Opening Weekend (USA)")
ws.write(0, 3, "Cumulative Worldwide Gross")
ws.write(0, 4, "Director")
ws.write(0, 5, "IMDb Rating")

# Writing names
num = 1
for variable in name_list:
    ws.write(num, 0, variable)
    num += 1

# Writing budget
num = 1
for variable in budget_list:
    ws.write(num, 1, variable)
    num += 1

# Writing opening weekend profit
num = 1
for variable in weekend_list:
    ws.write(num, 2, variable)
    num += 1

# Writing cumulative gross profit
num = 1
for variable in cumulative_gross_list:
    ws.write(num, 3, variable)
    num += 1

# Writing directors name
num = 1
for variable in director_list:
    ws.write(num, 4, variable)
    num += 1

# Writing rating
num = 1
for variable in rating_list:
    ws.write(num, 5, variable)
    num += 1

# Saving excel file
wb.save("Movie Information.xls")
