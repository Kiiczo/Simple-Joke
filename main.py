import requests

text = requests.get("https://official-joke-api.appspot.com/random_joke")
text = text.json()
print(text["setup"])
print("Click enter to see punchline")
input()
print(text["punchline"])