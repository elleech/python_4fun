# I was trying to write my own Chinese calendar converter
# but I couldn't find a pattern of it :(
# Instead I can only parse data from wikipedia
# Sorry for the dates outside 2001-2100

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
page = urllib.request.urlopen('https://en.wikipedia.org/wiki/Chinese_New_Year')
soup = BeautifulSoup(page, 'html.parser')

loop = 0
chinese = {}
for data in soup.find_all('table', {'class': 'wikitable'}):

    # Remove unwanted items in wikitable
    for remove in data.find_all('td', {'rowspan': '26'}):
        remove.extract()
    for remove in data.find_all('th'):
        remove.extract()

    table = data.find_all('tr')
    loop += 1

    # Scan only the first two tables
    if loop <= 2:
        for info in table:
            row = info.find_all('td')
            if len(row) == 8:
                year1 = row[0].text
                year2 = row[4].text
                date1 = row[1].text
                date2 = row[5].text
                zodiac1 = row[2].text
                zodiac2 = row[6].text
                weekday1 = row[3].text
                weekday2 = row[7].text
                
                chinese[year1] = [date1, weekday1, zodiac1]
                chinese[year2] = [date2, weekday2, zodiac2]
# Checking
# print(chinese)

print('''
Welcome to find Chinese New Year!

Type any year between 2001-2100
I'll show you the date of Chinese New Year
and the zodiac animal of that year
''')

while True:
    find = input('Enter a year: ')
    if len(find) == 4 and '2001' <= find <= '2100':
        print('It is on %s, %s.' %(chinese[find][0], chinese[find][1]))
        print('The animal of %s is %s.\n' %(find, chinese[find][2]))
    elif len(find) == 0:
        break
    else:
        print('Invalid year. Try again.\n')
