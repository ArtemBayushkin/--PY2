class Clothes:
    def __init__(self, name: str, description: str):
        """
        Базовый класс одежды

        :param name: Наименование одежды
        :param description: Описание одежды
        """
        self.name = name
        self.description = description

    def __str__(self) -> str:
        """
        Возвращает описание одежды

        :return: Возвращает описание одежды
        """
        return f"{self.name}: {self.description}"

    def __repr__(self) -> str:
        """
        Возвращает описание одежды для внутреннего пользования

        :return: Возвращает описание одежды
        """
        return f"Clothes(name={self.name}, description={self.description})"

    def get_class_name(self):
        """
        Метод, который возвращает название класса
        
        :return: Название базового класса
        """
        return self.__class__.__name__


class TShirt(Clothes):
    def __init__(self, name: str, description: str, size: int, color: str):
        """
        Дочерний класс одежды TShirt

        :param name: Наименование футболки
        :param description: Описание футболки
        :param size: Размер футболки
        :param color: Цвет футболки
        """
        super().__init__(name, description)
        self.size = size
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает описание футболки

        :return: Возвращает описание футболки
        """
        return f"{self.name}: {self.description}, size: {self.size}, color: {self.color}"

    def __repr__(self) -> str:
        """
        Возвращает описание футболок для внутреннего пользования

        :return: Возвращает описание футболок
        """
        return f"TShirt(name={self.name}, description={self.description}, size={self.size}, color={self.color})"

    def is_large(self) -> bool:
        """
        Проверяет размер футболки

        :return: Возвращает логический тип данных
        """
        return self.size > 10

    def get_class_name(self):
        """
        Перегрузка метода из базового класса
        
        :return: Название дочернего класса
        """
        return 'TShirts'


class Pants(Clothes):
    def __init__(self, name: str, description: str, length: int, color: str):
        """
        Дочерний класс одежды Pants

        :param name: Наименование штанов
        :param description: Описание штанов
        :param length: Размер штанов
        :param color: Цвет штанов
        """
        super().__init__(name, description)
        self.length = length
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает описание штанов

        :return: Возвращает описание штанов
        """
        return f"{self.name}: {self.description}, length: {self.length}, color: {self.color}"

    def __repr__(self) -> str:
        """
        Возвращает описание штанов для внутреннего пользования

        :return: Возвращает описание штанов
        """
        return f"Pants(name={self.name}, description={self.description}, length={self.length}, color={self.color})"

    def is_long(self) -> bool:
        """
        Проверяет размер штанов

        :return: Возвращает логический тип данных
        """
        return self.length > 30




if __name__ == "__main__":
    tshirt = TShirt('TShirt', 'oversized t-shirt for true fashion lovers', 15, 'red')
    print(tshirt, ";", tshirt.is_large())
    clother = Clothes('Clother', 'very good')
    print(clother.get_class_name())
