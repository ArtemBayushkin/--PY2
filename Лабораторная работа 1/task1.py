import doctest
class Table:
    def __init__(self, length: float, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Стол"
        :param length: Длина стола (см.)
        :param width: Ширина стола (см)
        :param height: Высота стола (см)
        Примеры:
        table = Table(100, 200, 300) # инициализация экземпляра класса
        """
        if length < 0:
            raise ValueError("Длина не должна быть отрицательным числом")
        if not isinstance(length, (int, float)):
            raise TypeError("Длина стола должна быть числом!")
        self.length = length

        if width < 0:
            raise ValueError("Ширина не должна быть отрицательным числом")
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стола должна быть числом!")
        self.width = width

        if height < 0:
            raise ValueError("Высота не должна быть отрицательным числом")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должна быть числом!")
        self.height = height
    def if_can_fit(self, length_space: float, width_space: float, height_space: float):
        """
        Проверка возможности стола влезть в указанное пространство
        :param length: Длина пространства
        :param width: Ширина пространства
        :param height: Высота пространства
        :return: Может ли стол влезть в пространство
        :raise ValueError: Если один из указанных габаритов пространства отрицательный или не является числом
        Примеры:
        table = Table(100,200,300)
        table.if_can_fit(100,200,300)
        """
        if length_space < 0:
            raise ValueError("Длина не должна быть отрицательным числом")
        if not isinstance(length_space, (int, float)):
            raise TypeError("Длина стола должна быть числом!")
        if width_space < 0:
            raise ValueError("Ширина не должна быть отрицательным числом")
        if not isinstance(width_space, (int, float)):
            raise TypeError("Ширина стола должна быть числом!")
        if height_space < 0:
            raise ValueError("Высота не должна быть отрицательным числом")
        if not isinstance(height_space, (int, float)):
            raise TypeError("Высота стола должна быть числом!")
        ...
    def if_can_stand(self, legs_number: int):
        """
        Проверка, может ли стол устойчиво стоять при указанном числе ножек
        :param legs_number: Число ножек у стола
        :return: Может ли стол стоять
        :raise ValueError: Если указано отрицательное или дробное число ножек
        Примеры:
        table = Table(100,200,300)
        table.if_can_stand(4)
        """
        if legs_number < 0:
            raise ValueError("Число ножек не должно быть отрицательным числом")
        if not isinstance(legs_number, int):
            raise TypeError("Число ножек не должно быть дробным числом!")
        ...

class Fridge:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Холодильник"
        :param capacity_volume: Объем холодильника
        :param occupied_volume: Объем занимаемых продуктов
        Примеры:
        »> glass = Fridge(500, 0) # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем холодильника должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем холодильника должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество продуктов должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество продуктов не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

        def is_empty_fridge(self) -> bool:
            """
            Функция которая проверяет является ли холодильник пустым
            :return: Является ли холодильник пустым
            Примеры:
            fridge = Fridge(500, 0)
            fridge.is_empty_glass()
            """
        ...

    def add_product_to_fridge(self, product: float) -> None:
        """
        Добавление продуктов в холодильник.
        :param product: Объем добавляемых продуктов
        :raise ValueError: Если количество добавляемых продуктов превышает
        свободное место в холодильнике, то вызываем ошибку
        Примеры:
        fridge = Fridge(500, 0)
        fridge.add_product_to_fridge(200)
        """
        if not isinstance(product, (int, float)):
            raise TypeError("Добавляемые продукты должны быть типа int или float")
        if product < 0:
            raise ValueError("Добавляемые продукты должны быть положительным числом")
        ...

    def remove_product_from_fridge(self, estimate_product: float) -> None:
        """
        Извлечение продуктов из холодильника.
        :param estimate_product: Объем извлекаемых продуктов
        :raise ValueError: Если количество извлекаемых продуктов превышает количество продуктов в холодильнике,
        то возвращается ошибка.
        :return: Объем реально извлеченных продуктов
        Примеры:
        fridge = Fridge(500, 500)
        fridge.remove_product_from_glass(200)
        """
        ...


class Slippers:
    def __init__(self, color: str, size: (int, float), sole: bool):
        """
        Создание и подготовка к работе объекта "Тапки"
        :param color: Цвет тапок
        :param size: Российский размер тапок
        :param sole: Уточнение жесткости подошвы у тапок
        Примеры:
        »> slippers = Slippers("Клетчатые", 43.5, True)
        """
        if not isinstance(color, str):
            raise TypeError("Цвет тапок должен быть формата str")
        self.color = color

        if not isinstance(size, (int, float)):
            raise TypeError("Размер тапок должен быть формата int или float")
        if size < 0:
            raise ValueError("Размер тапок не может быть отрицательным числом")
        self.size = size

        if not isinstance(sole, bool):
            raise TypeError("Жесткость подошвы должна описываться True или False")
        self.sole = sole

        def init_size(self) -> str:
            """
            Функция, которая определяет детский или взрослый размер тапок
            :return: Является ли размер детским или взрослым
            Примеры:
            slipper1 = Slippers("Розовый", 17, True)
            slipper1.init_size()
            » "Тапки детские"
            """
        ...

        def cost(self) -> float:
            """
            Функция, которая определяет примерную стоимость тапок
            :return: Возвращает примерное значение стоимости
            Примеры:
            slipper1 = Slippers("Молочный", 39, True)
            fridge.cost()
            » "299.99"
            """
        ...


if __name__ == "__main__":
    table1 = Table(100,200,300)
    fridge1 = Fridge(300,200)
    print(table1.length)
    print(fridge1.occupied_volume)
    print(help(Slippers))
