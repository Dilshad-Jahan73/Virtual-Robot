import requests

url = "https://official-joke-api.appspot.com/random_joke"
json_data = requests.get(url).json()

arr = ["", ""]
arr[0] = json_data["setup"]
arr[1] = json_data["punchLine"]


def joke():
    return arr
