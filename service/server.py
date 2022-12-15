import greeting_pb2_grpc
import greeting_pb2
import grpc
from concurrent import futures
import logging


class InventoryService(greeting_pb2_grpc.InventoryServiceServicer):
    # hardcode book database
    books = [
        {
            "ISBN": 1,
            "title": "Gone with the Wind",
            "author": "Margaret Mitchell",
            "genre": 2,
            "publishing_year": 1936,
        },
        {
            "ISBN": 2,
            "title": "Tale of Two Cities",
            "author": "Charles Dickens",
            "genre": 0,
            "publishing_year": 1859,
        },
    ]

    # Create a book with input book details
    def CreateBook(self, request, context):
        new_book = {
            "ISBN": request.ISBN,
            "title": request.title,
            "author": request.author,
            "genre": request.genre,
            "publishing_year": request.publishing_year,
        }

        self.books.append(new_book)
        return greeting_pb2.CreateResponse(success=1)

    # Retrieves a book's detail with input ISBN
    def GetBook(self, request, context):
        for book in self.books:
            if book['ISBN'] == request.ISBN:
                # found the book
                return greeting_pb2.Book(ISBN=book['ISBN'], title=book['title'], author=book['author'],
                                         genre=book['genre'], publishing_year=book['publishing_year'])
        # no book with given ISBN exists
        return greeting_pb2.Book(ISBN="-1", title="", author="", genre=[], publishing_year=-1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeting_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
