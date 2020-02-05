"""This module compares the cast/crew of two or more movies"""


class Comparer:
    """This class compares movies"""

    movie_list = []

    def __init__(self, api):
        self.api = api

    def compare(self):
        """Compare cast/crew of movies"""
        print(self.movie_list)

    def add_movie(self, title):
        """Add a movie to the list"""
        self.movie_list.append(title)

    def remove_movie(self, title, clear_all=False):
        """Remove movie(s) from list"""

        if clear_all:
            self.movie_list.clear()
        else:
            self.movie_list.remove(title)
