import pytest
from src.item import Item

@pytest.fixture(scope="function")
def setup_items():
    Item.items = []  # Очищаем список товаров перед каждым тестом
    yield
    Item.items = []  # Очищаем список товаров после каждого теста

def test_calculate_total_price():
    item = Item("Товар 1", 10.0, 5)
    assert item.calculate_total_price() == 50.0

def test_apply_discount():
    item = Item("Товар 1", 10.0, 5)
    item.apply_discount()
    assert item.price == 10.0  # Проверяем, что цена товара не изменилась

@pytest.mark.parametrize("discount_rate", [0.9, 0.8])
def test_set_discount_rate(discount_rate):
    Item.set_discount_rate(discount_rate)
    assert Item.discount_rate == discount_rate

def test_get_items(setup_items):
    item1 = Item("Товар 1", 10.0, 5)
    item2 = Item("Товар 2", 20.0, 3)
    items = Item.get_items()
    assert len(items) == 2
    assert item1 in items
    assert item2 in items
