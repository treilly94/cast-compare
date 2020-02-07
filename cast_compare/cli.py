import argparse

from cast_compare.api import Api


class CLI:

    def __init__(self):
        self.args = self.get_args()
        self.api = Api(api_key=self.args.api_key)
        self.lookup_titles()

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="Compare some movies")
        parser.add_argument("-a", "--api-key", type=str, nargs="?", required=True,
                            help="A omdbapi key")
        parser.add_argument("-t", "--titles", type=str, nargs="*", required=False,
                            help="One or more movie titles to be compared")

        return parser.parse_args()

    def lookup_titles(self):
        if self.args.titles:
            response = self.api.search(title=self.args.titles[0])

            if len(response) > 1:
                print("Please select a title from the list below")
                for i, v in enumerate(response):
                    print(str(i) + " | " + v["Title"] + " " + v["Year"])
                selection = int(input("Select a number: "))
                return response[selection]
            else:
                return response[0]


if __name__ == "__main__":
    cli = CLI()
