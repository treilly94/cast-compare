"""This module gets movie info from the omdbapi-"""

import requests


class Api:
    """This class is used for interfacing with the omdbapi"""

    def __init__(self, api_key):
        self.root_url = "http://www.omdbapi.com/?apikey=" + api_key

    @staticmethod
    def query_api(url):
        """Query a url and return any json as a python dictionary"""
        response = requests.get(url=url)
        result = response.json()
        return result

    def search(self, title):
        """Search for movie titles"""
        url = self.root_url + "&s=" + title
        response = self.query_api(url=url)
        if response["Response"] == "False":
            print("No search results")
        elif response["Response"] == "True":
            return response["Search"]

    def detail(self, imdb_id):
        """Get movie details from a IMDb Id"""
        url = self.root_url + "&i=" + imdb_id
        return self.query_api(url=url)
