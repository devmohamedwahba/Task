import json

from flask_restful import Resource, reqparse
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


# class BookById(Resource):
#     @classmethod
#     def get(cls, id):
#         data_frame = pd.read_excel('books.xlsx')
#
#         data_frame = data_frame[data_frame['الترتيب'] == id]
#         book = data_frame.to_json(orient='records')
#         return {"message": json.loads(book)}, 201


class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "book", type=str, required=False, help="this field is required"
    )
    parser.add_argument(
        "author", type=str, required=False, help="this field is required"
    )
    parser.add_argument(
        "country", type=str, required=False, help="this field is required"
    )

    @classmethod
    def get(cls, id):
        data_frame = pd.read_excel('books.xlsx')

        data_frame = data_frame[data_frame['الترتيب'] == id]
        # data_frame.to_excel('books.xlsx', index=False, header=True)
        book = data_frame.to_json(orient='records')
        return {"message": json.loads(book)}, 200

    @classmethod
    def put(cls, id):
        data = cls.parser.parse_args()

        data_frame = pd.read_excel('books.xlsx')
        data_frame.loc[data_frame.الترتيب == id, 'الرواية'] = data.book
        data_frame.loc[data_frame.الترتيب == id, 'المولف'] = data.author
        data_frame.loc[data_frame.الترتيب == id, 'البلد'] = data.country

        data_frame.to_excel('books.xlsx', index=False, header=True)
        book = data_frame.to_json(orient='records')
        return {"message": json.loads(book)}, 200

    @classmethod
    def delete(cls, id):
        data_frame = pd.read_excel('books.xlsx')

        newdf = data_frame[(data_frame.الترتيب != id)]

        newdf.to_excel('books.xlsx', index=False, header=True)

        return {"message": ""}, 204

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        data_frame = pd.read_excel('books.xlsx')
        last_id = int(data_frame.iloc[-1:]['الترتيب']) + 1
        data_to_append = {"الترتيب": last_id, "الرواية": data.book, "المولف": data.author, "البلد": data.country}
        data_frame = data_frame.append(data_to_append, ignore_index=True)
        data_frame.to_excel('books.xlsx', index=False, header=True)
        book = data_frame.to_json(orient='records')
        return {"message": json.loads(book)}, 201


class Books(Resource):
    @classmethod
    def get(cls):
        df = pd.read_excel('books.xlsx')
        all_books = df.to_json(orient='records')
        if not all_books:
            return {"message": "there is no Books"}
        return json.loads(all_books), 200
