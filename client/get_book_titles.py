from inventory_client import InventoryClient

# returns the list of titles with the given list of ISBNs
def GetTitles(client, ISBNs):
    titles = []
    for ISBN in ISBNs:
        book = client.GetTitle(ISBN=ISBN)
        print(book.book)
        titles.append(book.book.title)
    return titles


if __name__ == "__main__":
    # create an instance of client api object to access the server
    client = InventoryClient("localhost", 10086)
    # call the defined function using two hardcoded ISBNs as a parameter
    title_list = GetTitles(client, ["1", "2"])
    # print returned titles to standard output
    print(title_list)
