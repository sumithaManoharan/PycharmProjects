from bs4 import BeautifulSoup as BS
import requests as rt

response = rt.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BS(response.text, "html.parser")

movie_list = soup.select("div.article-title-description__text")
movies = []

for movie in movie_list:
    text = movie.select_one("h3.title").text+" \n"
    movies.append(text)

new_list = movies[::-1]


with open("movies.txt", "w") as f:
    f.writeli