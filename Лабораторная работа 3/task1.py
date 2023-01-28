class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"\nКнига: {self.name}" \
               f"\nАвтор: {self.author}"

    def __repr__(self):
        return f"name={self.name!r}, author={self.author!r}"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

class PaperBook(Book):
    cover = "Твердый переплет"

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise ValueError("Число страниц должно быть положительным")
        else:
            raise TypeError("Число страниц должно быть типа 'int'")

    def __str__(self):
        return f"{Book.__str__(self)}" \
               f"\nФормат: {self.cover}" \
               f"\nЧисло страниц: {self.pages}"

    def __repr__(self):
        return f"({Book.__repr__(self)}, pages={self.pages}, cover={self.cover!r})"


class AudioBook(Book):
    format = "Аудио"

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0:
                self.duration = duration
            else:
               raise ValueError("Время должно быть положительным")
        else:
            raise TypeError("Время должно быть типа 'float'")

    def __str__(self):
        return f"{Book.__str__(self)}" \
               f"\nФормат: {self.format}" \
               f"\nПродолжительность: {self.duration}"

    def __repr__(self):
        return f"({Book.__repr__(self)}, duration={self.duration}, format={self.format!r})"


paper = PaperBook('Зеленая миля', 'Стивен Кинг', 980)
audio = AudioBook('Записки юного врача', 'Михаил Булгаков', 15.45)

print(paper)
print(audio)
