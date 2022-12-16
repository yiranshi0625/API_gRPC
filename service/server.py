import greeting_pb2_grpc
import greeting_pb2
import grpc
from concurrent import futures
import logging


class InventoryService(greeting_pb2_grpc.InventoryServiceServicer):
    # hardcode book database
    books = [
        {
            "ISBN": "1",
            "title": "Gone with the Wind",
            "author": "Margaret Mitchell",
            "genre": greeting_pb2.ROMANCE,
            "publishing_year": 1936
        },
        {
            "ISBN": "2",
            "title": "Tale of Two Cities",
            "author": "Charles Dickens",
            "genre": greeting_pb2.HISTORICAL,
            "publishing_year": 1859
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
        for get in self.books:
            if get['ISBN'] == request.ISBN:
                # found the book
                return greeting_pb2.GetResponse(book=get)
        # no book with given ISBN exists
        return greeting_pb2.GetResponse(book={"ISBN": "-1", "title": "", "author": "", "genre": greeting_pb2.UNKNOWN,
                                              "publishing_year": -1})


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeting_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryService(), server)
    server.add_insecure_port('[::]:10086')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
