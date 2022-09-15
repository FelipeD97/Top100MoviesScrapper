import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
# print(response.text)
# print(response)

page_data = BeautifulSoup(response.text, "html.parser")
movie_data = page_data.find_all(name="h3", class_="title")

movie_list = [movie.get_text() for movie in movie_data]

# Reverse List
movies = movie_list[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
