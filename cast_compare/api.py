import requests


class Api:

    def __init__(self, api_key):
        self.root_url = "http://www.omdbapi.com/?apikey=" + api_key

    @staticmethod
    def query_api(url):
        response = requests.get(url=url)
        result = response.json()
        return result

    def search(self, title):
        url = self.root_url + "&s=" + title
        return self.query_api(url=url)

    def detail(self, imdb_id):
        url = self.root_url + "&i=" + imdb_id
        return self.query_api(url=url)
