import requests
import math
from bs4 import BeautifulSoup

website = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(website.text, "html.parser")
a = soup.find_all('h3')

print("AA")
length = len(a)
movies = []
for i in range(length-1, -1, -1):
    movies.append(a[i].get_text()[int(math.log10(length-i))+3:])

with open(file="movies.txt", mode="w") as file:
    for i in movies:
        file.write(i+"\n")