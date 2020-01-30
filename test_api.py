from unittest import TestCase

import httpretty as httpretty

from api import Api


class TestApi(TestCase):

    @httpretty.activate
    def test_search(self):
        # Init API
        api = Api(api_key="test")

        # Read data for mock response
        with open("search_cats.json", "r", encoding="utf-8") as file:
            json = file.read()

        # Mock the response
        httpretty.register_uri(
            httpretty.GET,
            "http://www.omdbapi.com/?apikey=test&s=cats",
            body=json
        )

        expected = {
            "Search": [
                {
                    "Title": "Cats & Dogs",
                    "Year": "2001",
                    "imdbID": "tt0239395",
                    "Type": "movie",
                    "Poster": "https://m.media-amazon.com/images/M/MV5BY2JmMDJlMmEtYTk4OS00YWQ5LTk2NzMtM2M3NzhkMjI4MGJkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_SX300.jpg"
                },
                {
                    "Title": "Cats",
                    "Year": "2019",
                    "imdbID": "tt5697572",
                    "Type": "movie",
                    "Poster": "https://m.media-amazon.com/images/M/MV5BNjRlNTY3MTAtOTViMS00ZjE5LTkwZGItMGYwNGQwMjg2NTEwXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_SX300.jpg"
                },
                {
                    "Title": "Cats & Dogs: The Revenge of Kitty Galore",
                    "Year": "2010",
                    "imdbID": "tt1287468",
                    "Type": "movie",
                    "Poster": "https://m.media-amazon.com/images/M/MV5BMTYwNTk2NTc3OV5BMl5BanBnXkFtZTcwMDUwMzgyMw@@._V1_SX300.jpg"
                }
            ],
            "totalResults": "297",
            "Response": "True"
        }

        result = api.search("cats")

        self.assertEquals(expected, result)
