from inventory_client import InventoryClient


def GetTitles(client, ISBNs):
    titles = []
    for ISBN in ISBNs:
        book = client.GetTitle(ISBN=ISBN)
        print(book.book)
        titles.append(book.book.title)
    return titles


if __name__ == "__main__":
    client = InventoryClient("localhost", 10086)
    title_list = GetTitles(client, ["1", "2"])
    print(title_list)
