import pytest
import csv
from src.item import Item

@pytest.fixture
def item():
    return Item("Test Item", 10.0, 3)

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 30.0

def test_apply_discount(item):
    item.apply_discount()
    assert item.calculate_total_price() == 30.0  # После применения скидки, общая цена должна остаться такой же

def test_set_discount_rate():
    Item.set_discount_rate(0.9)
    assert Item.discount_rate == 0.9

def test_instantiate_from_csv():
    # Создайте временный CSV файл для тестов
    with open('test_items.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'price', 'quantity'])
        writer.writerow(['Test Item 1', '10.0', '3'])
        writer.writerow(['Test Item 2', '20.0', '2'])

    Item.instantiate_from_csv('test_items.csv')
    items = Item.get_items()
    assert len(items) == 2
    assert items[0].name == 'Test Item 1'
    assert items[1].name == 'Test Item 2'

    # Удалите временный файл после завершения теста
    import os
    os.remove('test_items.csv')

def test_string_to_number():
    assert Item.string_to_number('123') == 123
    assert Item.string_to_number('12.34') == 12.34
    with pytest.raises(ValueError):
        Item.string_to_number('abc')

def test_item_repr():
    item = Item("Тестовый товар", 20.0, 10)
    assert repr(item) == "Item(name=Тестовый товар, price=20.0, quantity=10)"

def test_item_str():
    item = Item("Тестовый товар", 20.0, 10)
    assert str(item) == "Тестовый товар - $20.0 - 10 items"
