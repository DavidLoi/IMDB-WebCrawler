# IMDB-WebCrawler
This webcrawler parses through the most popular movies of 2009 on IMDB and returns the budget, opening week USA revenue, worldwide gross, the director and the rating of each movie. This data is then exported to an excel spreadsheet.

# Motivation
I created this webcrawler to help me on a project I had to do for my advanced functions class. My group had to gather the data figures mentioned above and identify any relationships between them. In order to avoid gathering all this data by hand I decided to create this program that could do it for us and we would just have to modify the figures for some pages that had different formatting.

# Screenshots
The following is a screenshot of the excel spreadsheet after the program has finished running, this spreadsheet can also be found in the repository.

![Data](https://github.com/DavidLoi/IMDB-WebCrawler/blob/main/Screenshots/Data.PNG)

# How to use?
The base url can be changed if the user would like to change the year for the movie releases, refer to the snippet shown below.

![Source](https://github.com/DavidLoi/IMDB-WebCrawler/blob/main/Screenshots/Source.PNG)

In addition, in some cases a date will be included in the end of the opening weekend profit or budget, so the following are measures against this which will remove the date. Keep in mind that if the year is changed, these measures will need to be changed accordingly.

![Change1](https://github.com/DavidLoi/IMDB-WebCrawler/blob/main/Screenshots/Change1.PNG)
![Change2](https://github.com/DavidLoi/IMDB-WebCrawler/blob/main/Screenshots/Change2.PNG)
