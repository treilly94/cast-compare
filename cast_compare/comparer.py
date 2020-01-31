class Comparer:

    movie_list = []

    def __init__(self, api):
        self.api = api

    def compare(self):
        """Compare cast/crew of movies"""
        pass

    def add_movie(self):
        """Add a movie to the list"""
        pass

    def remove_movie(self, title, clear_all=False):
        """Remove movie(s) from list"""

        if clear_all:
            self.movie_list.clear()
        else:
            self.movie_list.remove(title)
