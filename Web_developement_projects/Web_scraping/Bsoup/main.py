from bs4 import BeautifulSoup as BS
import requests as rt

response = rt.get("https://news.ycombinator.com/news")
soup = BS(response.text, "html.parser")

# 1. Get all the story rows (where the links are)
# 2. Get all the subtext rows (where the scores are)
stories = soup.select(".athing")
subtexts = soup.select(".subtext")

highest_score = 0
top_url = ""
top_title = ""

# Loop through stories and their corresponding subtexts
for i in range(len(stories)):
    # Check if a score exists (some posts, like jobs, have no score)
    score_span = subtexts[i].select_one(".score")
    if score_span:
        score = int(score_span.text.split(" ")[0])

        if score > highest_score:
            highest_score = score
            # Find the link inside the current story row
            link_tag = stories[i].select_one(".titleline a")
            top_url = link_tag.get("href")
            top_title = link_tag.text

print(f"Top Story: {top_title}")
print(f"URL: {top_url}")
print(f"Highest Score: {highest_score}")