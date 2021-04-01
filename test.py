
# #list_comprehension
# movies_and_ratings = {"Interstellar":9, "Dark Knight":8, "50 Shades Darker": 2, "50 Shades Darkest": 1}
 
# l = []
# for movie in movies_and_ratings:
#     if movies_and_ratings[movie] > 6:
#          l.append(movie)
# print(l)

# print( [movie for movie in movies_and_ratings if movies_and_ratings[movie] > 6] )

# #Email Address Text Scraper
# import re

# text = "random string. MyName123@website.com . some more random text. Your_Name.8-8-8@company.net"

# pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

# result = pattern.findall(text)

# print(result)

#datetime module
# import datetime
# import pytz


# today = datetime.date.today()
# print(today)

# birthday = datetime.date(1998, 1, 13)
# print(birthday)

# days_since_birth = (today - birthday).days
# print(days_since_birth)

# # adding 10 days to current day 
# tdelta = datetime.timedelta(days=10)
# print(today + tdelta)

# print(datetime.time(7, 2, 20, 15))
# #datetime.date (Y, M, D)
# #datetime.time (h, m, s, ms)
# #datetime.datetime(Y, M, D, h, m, s, ms)

# # Add 10 hours to current day
# hour_delta = datetime.timedelta(hours=10)
# print(datetime.datetime.now() + hour_delta)

# datetime_today = datetime.datetime.now(tz=pytz.UTC)
# datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
# print(datetime_pacific)
# for tz in pytz.all_timezones:
#     print(tz)

# #string formatting with dates
# #2021-03-09 -> March 8, 2021
# #strftime (f = formatting)

# print(datetime_pacific.strftime('%B %d, %Y'))

# # March 08, 2021 -> datetime(2021,3,8)
# #strptime (p = parsing)
# datetime_thing = datetime.datetime.strptime('March 08, 2021', '%B %d, %Y')
# print(datetime_thing)

##web scraping 

import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09969000000007&lon=-118.33512999999999#.YFfENK8zaUk')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)