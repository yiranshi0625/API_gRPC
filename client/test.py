from unittest import mock
import unittest
from get_book_titles import GetTitles
import get_book_titles
from inventory_client import InventoryClient


class Reply:
    def __init__(self, book):
        self.book = book


class Book:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title


# mocked return result
mockReplyBook1 = Reply(Book("1", "book1"))
mockReplyNotExistRes = Reply(Book("-1", ""))


class Test_get_book_titles(unittest.TestCase):
    def test_01(self):
        '''get book title success'''
        print("get book title success mock test")
        # mock client api, each time return book1 as result
        client = InventoryClient("localhost", "50051")
        client.get_book = mock.Mock(return_value=mockReplyBook1)
        # get book titles based on mock result
        book_title_list = GetTitles(client, ["1", "2", "3"])
        print("whatever")
        print(book_title_list)
        self.assertEqual(len(book_title_list), 3)
        self.assertEqual(book_title_list[0], "book1")
        self.assertEqual(book_title_list[1], "book1")
        self.assertEqual(book_title_list[2], "book1")

    def test_02(self):
        '''get book title fail'''
        print("get book title fail mock test")
        # mock client api, each time return book1 as result
        # get book titles based on mock result
        client = InventoryClient("localhost", "50051")
        client.get_book = mock.Mock(return_value=mockReplyNotExistRes)
        # if the book does not exist, should not include its title
        book_title_list = GetTitles(client, ["not exist1", "not exist2"])
        print(book_title_list)
        self.assertEqual(len(book_title_list), 0)


if __name__ == "__main__":
    unittest.main()
