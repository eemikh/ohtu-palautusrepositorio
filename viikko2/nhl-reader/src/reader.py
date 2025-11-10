import requests

class PlayerReader:
    def __init__(self, url: str):
        self.url = url

    def read(self) -> dict[any]:
        response = requests.get(self.url).json()

        return response
