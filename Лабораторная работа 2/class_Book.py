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
        """
        Создание и подготовка к работе объекта "Книга"
        :param id_: ID книги
        :param name: Название книги
        :param pages: Кол-во страниц книги
        """
        self.name = name
        self.id_ = id_
        self.pages = pages


class Library:
    def __init__(self, books: list[Book] = None):
        """
        Создание и подготовка к работе объекта "Библиотека"
        :param books: список книг из объекта "Книга"
        """
        if books is None:                           # Проверка. Если переменная пуста, как изначально записано
            books = []                              # переменная принимает пустой список
        self.books = books                          # Описание объекта

    def get_next_book_id(self):                     # Метод, возвращающий ID для добавления новой книги
        return len(self.books) + 1                  # Возвращает увеличенный на 1 ID для добавления новой книги
    """ С точки зрения быстродействия такой метод менее эффективен, нежели использовать обратную индексацию списка. 
    Если будет миллион книг, то методу придется считать длину достаточно долго. Однако, если книг совсем нет, то
    индексация работать не будет, так как нет листа"""

    def get_index_by_book_id(self, id_):            # Метод, возвращающий ID книги
        flag = False
        for index, value in enumerate(self.books):  # Перебор ID в списке книг
            if value.id_ == id_:                    # Если во время перебора был найден ID
                return index                        # ID возвращается
        if flag is False:                           # Если ID не найден, возвращается ошибка
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
