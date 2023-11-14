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

@pytest.fixture
def sample_csv(tmp_path):
    csv_content = """Name,Price,Quantity
                    Item1,10.5,3
                    Item2,20.0,5
                    Item3,15.75,2"""
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(csv_content)
    return csv_file

def test_instantiate_from_csv(sample_csv):
    items = Item.instantiate_from_csv(sample_csv)

    assert len(items) == 3, "Ожидалось получить три элемента из файла CSV"

    # Проверка первого элемента с учетом пробелов
    assert items[0].name.strip() == "Item1"
    assert items[0].price == 10.5
    assert items[0].quantity == 3

    # Проверка второго элемента
    assert items[1].name.strip() == "Item2"
    assert items[1].price == 20.0
    assert items[1].quantity == 5

    # Проверка третьего элемента
    assert items[2].name.strip() == "Item3"
    assert items[2].price == 15.75
    assert items[2].quantity == 2
def test_string_to_number():
    assert Item.string_to_number('123') == 123
    assert Item.string_to_number('12.34') == 12.34
    with pytest.raises(ValueError):
        Item.string_to_number('abc')

def test_item_rept_and_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
