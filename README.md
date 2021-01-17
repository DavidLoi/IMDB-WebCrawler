# IMDB-WebCrawler
This webcrawler parses through the most popular movies of 2009 on IMDB and returns the budget, opening week USA revenue, worldwide gross, the director and the rating of each movie. This data is then exported to an excel spreadsheet.

# Motivation
I created this webcrawler to help me on a project I had to do for my advanced functions class. My group had to gather the data figures mentioned above and identify any relationships between them. In order to avoid gathering all this data by hand I decided to create this program that could do it for us and we would just have to modify the figures for some pages that had different formatting.

# Screenshots
The following is a screenshot of the excel spreadsheet after the program has finished running, this spreadsheet can also be found in the repository.

![Data](https://github.com/DavidLoi/IMDB-WebCrawler/blob/main/Screenshots/Data.PNG)

# How to use?
The base url can be changed (the line of code underneath) if the user would like to change the year for the movie releases.

source = requests.get('https://www.imdb.com/search/title?title_type=feature&release_date=2009-01-01,2009-12-31').text
