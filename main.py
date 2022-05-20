"""
    Main app concern with run main core functionality of app
"""
from utils.logger import Logger
import requests
import pandas as pd
import gspread
from pages.books_page import BookPage


def main():
    try:
        url = 'https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D9%85%D8%A6%D8%A9_%D8%B1%D9%88%D8%A7%D9%8A%D8%A9_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9'
        page_content = requests.get(url).content

        page = BookPage(page_content=page_content)

        books = page.books
        data = {'الترتيب': [book.to_json()['id'] for book in books],
                'الرواية': [book.to_json()['book'] for book in books],
                'رابط الرواية': [book.to_json()['book_href'] for book in books],
                'المولف': [book.to_json()['author'] for book in books],
                'رابط المولف': [book.to_json()['author_href'] for book in books],
                'البلد': [book.to_json()['country'] for book in books],
                'رابط البلد': [book.to_json()['country_href'] for book in books]}

        df = pd.DataFrame(data, columns=['الترتيب', 'الرواية', 'رابط الرواية', 'المولف', 'رابط المولف', 'البلد', 'رابط البلد'])
        df.to_excel('books.xlsx', index=False, header=True)

        sa = gspread.service_account(filename='nagwa-347411-f82ce102ce07.json')

        sh = sa.open("books")
        wks = sh.worksheet('Sheet1')

        for book in books[:2]:
            wks.update(f'A{book.to_json()["id"]}', book.to_json()['id'])
            wks.update(f'B{book.to_json()["id"]}', book.to_json()['book'])
            wks.update(f'C{book.to_json()["id"]}', book.to_json()['book_href'])
            wks.update(f'D{book.to_json()["id"]}', book.to_json()['author'])
            wks.update(f'E{book.to_json()["id"]}', book.to_json()['author_href'])
            wks.update(f'F{book.to_json()["id"]}', book.to_json()['country'])
            wks.update(f'G{book.to_json()["id"]}', book.to_json()['country_href'])




    except Exception as e:
        Logger.error(e, exc_info=True)


if __name__ == '__main__':
    main()
