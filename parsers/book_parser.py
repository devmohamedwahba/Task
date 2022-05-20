

class BookParser:
    def __init__(self, parent):
        self.parent = parent

    def to_json(self):
        return {
            "id": self.parent.select('td')[0].string.strip('\n'),
            "book": self.parent.select('td a')[0].string,
            "book_href": self.parent.select('td a')[0].attrs['href'],
            "author": self.parent.select('td a')[1].string,
            "author_href": self.parent.select('td a')[0].attrs['href'],
            "country": self.parent.select('td a')[2].string,
            "country_href": self.parent.select('td a')[0].attrs['href'],
        }

