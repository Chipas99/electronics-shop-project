class Item:
    """
    Класс для представления товара в магазине.
    """
    discount_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

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
        Устанавливает уровень скидки для всех товаров.
        """
        cls.discount_rate = discount_rate

    @classmethod
    def get_items(cls):
        """
        Возвращает список всех созданных экземпляров класса all.
        """
        return cls.all
