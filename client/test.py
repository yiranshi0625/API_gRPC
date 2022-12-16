import unittest
from unittest.mock import MagicMock
from get_book_titles import GetTitles
from inventory_client import InventoryClient
import greeting_pb2


class Test(unittest.TestCase):
    # Mock testing GetTitles in get_book_titles.py using Mock (w/o running server)
    def test_get_book_mock(self):
        example_book = greeting_pb2.Book(ISBN="1", title="Robinson Crusoe", author="Daniel Defoe",
                                         genre=greeting_pb2.ADVENTURE, publishing_year=1719)
        # mock object of InventoryClient
        client_mock = InventoryClient("mock", 00000)
        client_mock.GetTitle = MagicMock(return_value=greeting_pb2.GetResponse(book=example_book))
        titles = GetTitles(client_mock, ["1"])
        assert (titles == ["Robinson Crusoe"])

    # Testing GetTitles in get_book_titles.py using a live server to access the API
    def test_get_book_live_server(self):
        client = InventoryClient("localhost", 10086)
        # create a new book, adding to the existing book database
        client.CreateBook(ISBN="3", title="Jane Eyre", author="Charlotte Brontë",
                          genre=greeting_pb2.ROMANCE, publishing_year=1847)
        titles = GetTitles(client, ["1", "3"])
        assert (titles == ["Gone with the Wind", "Jane Eyre"])


if __name__ == "__main__":
    unittest.main()
