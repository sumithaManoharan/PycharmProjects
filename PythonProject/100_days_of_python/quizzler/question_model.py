import requests
class QuestionModel:
    def __init__(self):
        self.url = 'https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean'

    def get_questions(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Checks for internet errors
        data = response.json()

        # The Open Trivia DB puts results inside a "results" key
        return data["results"]