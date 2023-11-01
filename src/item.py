import csv

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
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv.
        """
        with open('src/items.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, price, quantity = row
                item = Item(name, float(price), int(quantity))
                cls.all.append(item)

    @staticmethod
    def string_to_number(value: str) -> float:
        """
        Статический метод, преобразующий строку в число.

        :param value: Строка, представляющая число.
        :return: Число.
        """
        return float(value)
