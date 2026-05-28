from typing import Any # Any is a special type hint that tells the type checker "this can be absolutely anything — don't check it".

from bs4 import BeautifulSoup

# This is the implementation of our adapter interface
class XMLAdapter:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup

    def get(self, key: str, default: Any = None) -> Any | None:
        value = self.soup.find(key)
        if value:
            return value.get_text()
        return default


# Below is what you would need to do for a class adapter
# But it leads to a problem, because BeautifulSoup already has
# a get method with a different signature.
# This is exactly why I recommend avoiding class adapters.

# class XMLAdapter(BeautifulSoup):
#    def get(self, key: str, default: Any = None) -> Any | None:
#        value = self.find(key)
#        if value:
#            return value.get_text()
#        return default