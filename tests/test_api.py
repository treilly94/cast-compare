from unittest import TestCase

import httpretty as httpretty

from cast_compare.api import Api


class TestApi(TestCase):

    def setUp(self):
        self.api = Api(api_key="test")

    @httpretty.activate
    def test_query_api(self):
        # Read data for mock response
        with open("tests/data/sample.json", "r", encoding="utf-8") as file:
            json = file.read()

        # Mock the response
        httpretty.register_uri(
            httpretty.GET,
            "http://www.test.com/",
            body=json
        )

        expected = {
            "string": "John",
            "num": 30,
            "bool": True,
            "null_value": None,
            "list": [
                "1",
                "2",
                "3"
            ],
            "object": {
                "string": "John",
                "num": 30
            }
        }

        result = self.api.query_api(url="http://www.test.com/")

        self.assertEqual(expected, result)

    @httpretty.activate
    def test_search(self):
        # Read data for mock response
        with open("tests/data/search_cats.json", "r", encoding="utf-8") as file:
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

        result = self.api.search(title="cats")

        self.assertEqual(expected, result)

    @httpretty.activate
    def test_detail(self):
        # Read data for mock response
        with open("tests/data/detail_cats.json", "r", encoding="utf-8") as file:
            json = file.read()

        # Mock the response
        httpretty.register_uri(
            httpretty.GET,
            "http://www.omdbapi.com/?apikey=test&i=test_id",
            body=json
        )

        expected = {
            "Title": "Cats",
            "Year": "2019",
            "Rated": "PG",
            "Released": "20 Dec 2019",
            "Runtime": "110 min",
            "Genre": "Comedy, Drama, Family, Fantasy, Musical",
            "Director": "Tom Hooper",
            "Writer": "T.S. Eliot (poetry collection \"Old Possum's Books of Practical Cats\"), Lee Hall (screenplay), Tom Hooper (screenplay), Andrew Lloyd Webber (musical)",
            "Actors": "Jennifer Hudson, Judi Dench, Taylor Swift, Robbie Fairchild",
            "Plot": "A tribe of cats called the Jellicles must decide yearly which one will ascend to the Heaviside Layer and come back to a new Jellicle life.",
            "Language": "English",
            "Country": "UK, USA",
            "Awards": "Nominated for 1 Golden Globe. Another 1 win & 1 nomination.",
            "Poster": "https://m.media-amazon.com/images/M/MV5BNjRlNTY3MTAtOTViMS00ZjE5LTkwZGItMGYwNGQwMjg2NTEwXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_SX300.jpg",
            "Ratings": [
                {
                    "Source": "Internet Movie Database",
                    "Value": "2.8/10"
                },
                {
                    "Source": "Metacritic",
                    "Value": "32/100"
                }
            ],
            "Metascore": "32",
            "imdbRating": "2.8",
            "imdbVotes": "20,921",
            "imdbID": "tt5697572",
            "Type": "movie",
            "DVD": "N/A",
            "BoxOffice": "N/A",
            "Production": "N/A",
            "Website": "N/A",
            "Response": "True"
        }

        result = self.api.detail(imdb_id="test_id")

        self.assertEqual(expected, result)
