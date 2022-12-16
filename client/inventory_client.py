import grpc
import greeting_pb2
import greeting_pb2_grpc


class InventoryClient:
    # handling  technical details in init
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel(str(host) + ":" + str(port))
        self.stub = greeting_pb2_grpc.InventoryServiceStub(self.channel)

    # create a book with given book details
    def CreateBook(self, ISBN, title, author, genre, publishing_year):
        request = greeting_pb2.CreateRequest(ISBN=ISBN, title=title, author=author, genre=genre,
                                                               publishing_year=publishing_year)
        return self.stub.CreateBook(request)

    # get a book's title with give ISBN
    def GetTitle(self, ISBN):
        request = greeting_pb2.GetRequest(ISBN=ISBN)
        return self.stub.GetBook(request)

