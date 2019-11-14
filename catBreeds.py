# Scraping a Wikipedia site
import requests
from bs4 import BeautifulSoup
import json

# string for entire page
html = requests.get("https://en.wikipedia.org/wiki/List_of_cat_breeds").text
# soup string for entire page
soup = BeautifulSoup(html, 'html.parser')
#print(soup)

# column headers
headers = soup.select("table.wikitable tr")[0]
#print(headers)

# info for all cats (does not include column headers)
rows = soup.select("table.wikitable tr")[1:]
#print(rows)

breeds = {}  # dictionary for all cats

# for each cat, get info and add to breeds dictionary
for row in rows:
#    print(row)
    breed_name = row.select("th")[0].text
#    print(breed_name)
    td = row.select("td")
#    print(td)
    country = td[0].text
    origin = td[1].text
    body_type = td[2].text
    coat_length = td[3].text
    pattern = td[4].text
    picture = td[5].select("img")
#    print(picture)
#    if picture:
#        image_url = picture[0].attrs["src"]
#        print(image_url)
#    print("\nNew Cat:")
#    print(country)
#    print(origin)
#    print(body_type)
#    print(coat_length)
#    print(pattern)

    # create a dictionary for the current cat and add to breeds dictionary
    kitty = {"country": country,
             "origin": origin,
             "body_type": body_type,
             "coat_length": coat_length,
             "pattern": pattern
             }
    breeds[breed_name] = kitty
#    print(json.dumps(breeds, indent=4))  # pretty print