import csv
import os.path

class Item:
    """
    Класс для представления товара в магазине.
    """
    discount_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """
        Геттер для получения названия товара.

        :return: Название товара.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Сеттер для установки названия товара.

        :param value: Новое название товара.
        """
        if len(value) <= 10:
            self._name = value
        else:
            self._name = value[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.discount_rate

    @classmethod
    def set_discount_rate(cls, discount_rate):
        """
        Устанавливает скидку для всех товаров.

        :param discount_rate: Скидка.
        """
        cls.discount_rate = discount_rate

    @classmethod
    def instantiate_from_csv(cls, filename):
        items = []
        with open(filename, 'r', encoding='cp1251') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)
            for row in csv_reader:
                name = row[0]
                price = float(row[1])
                quantity = int(row[2])
                item = cls(name=name, price=price, quantity=quantity)
                items.append(item)
        return items

    @staticmethod
    def string_to_number(value: str) -> float:
        """
        Статический метод, преобразующий строку в число.

        :param value: Строка, представляющая число.
        :return: Число.
        """
        return float(value)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        """
        Складывает атрибут количество товара (quantity)
        класса Item и (или) его дочерних классов
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            raise ValueError('Складываться должны атрибуты quantity класса Item и (или) его дочерних классов')


