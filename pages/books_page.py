from bs4 import BeautifulSoup

from locators.book_locators import BooksLocators
from parsers.book_parser import BookParser


class BookPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(BooksLocators.BOOKS)[1:]]
