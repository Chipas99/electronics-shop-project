import csv
import os.path

from src.csverror import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    discount_rate = 1.0
    all = []
    PATH_NAME = 'src/items.csv'

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

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

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
    def instantiate_from_csv(cls, path_name=PATH_NAME):
        """
        Создаёт объекты из данных файла .csv
        """

        items = []
        path_name = str(cls.path_file(path_name))

        try:
            with open(path_name, newline='', encoding='windows-1251') as csv_f:
                reader = csv.DictReader(csv_f)
                if reader.fieldnames != ['name', 'price', 'quantity']:
                    raise InstantiateCSVError
                for row in reader:
                    name = str(row['name'])
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    item = cls(name, price, quantity)
                    items.append(item)
                cls.all.extend(items)
        except FileNotFoundError:
            err_text = 'FileNotFoundError: Отсутствует файл item.csv'
            print(err_text)
            return err_text
        except InstantiateCSVError as err:
            print(err)
            return err

    @staticmethod
    def path_file(path_name):
        """
        Создаёт путь для файла при условии, что файл лежит в другой папке родительского каталога

        :param path_name: путь к файлу в подобном формате 'src/items.csv'
        """
        path_list = path_name.split('/')
        path_file = os.path.join('..', path_list[0], path_list[1])
        return path_file

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




