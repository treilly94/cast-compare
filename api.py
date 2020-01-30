import requests


class Api:

    def __init__(self, api_key):
        self.root_url = "http://www.omdbapi.com/?apikey=" + api_key

    def search(self, title):
        url = self.root_url + "&s=" + title
        response = requests.get(url=url)
        result = response.json()
        return result
