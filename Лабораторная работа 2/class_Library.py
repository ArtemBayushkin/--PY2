BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name: str, pages):
        self.name = name
        self.id_ = id_
        self.pages = pages


class Library:
    def __init__(self, books: list[Book] = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        return len(self.books) + 1

    def get_index_by_book_id(self, id_):
        for i, id_ in enumerate(self.books):
            if id_ in self.books:  # Не понял, как выделить id из листа с данными о книгах. Тут явная ошибка!
                return i
        #if index_ not in self.books:
        #    ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(2))  # проверяем индекс книги с id = 1
