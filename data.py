import requests

parameters = {
    "amount": 100,
    "type": "boolean"
}
# get the trivia question from open trivia database
response = requests.get("https://opentdb.com/api.php", parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]

