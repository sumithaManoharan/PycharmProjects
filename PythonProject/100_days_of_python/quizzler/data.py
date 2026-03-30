import requests as rt
import json

questions = rt.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
q = questions.json()
quizz_qns = q["results"]

with open("quizz_qns.json", "w") as file:
    json.dump(quizz_qns, file)



