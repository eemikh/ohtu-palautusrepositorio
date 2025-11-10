import requests

class PlayerReader:
    def __init__(self, url: str):
        self.set_url(url)

    def read(self) -> dict[any]:
        response = requests.get(self._url, timeout=10).json()

        return response

    def set_url(self, url):
        self._url = url
