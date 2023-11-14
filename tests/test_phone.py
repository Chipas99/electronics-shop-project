from src.phone import Phone
import pytest

def test_phone_repr():
    phone = Phone("Test Phone", 500, 3, 2)
    expected_repr = "Phone('Test Phone', 500, 3, 2)"
    assert repr(phone) == expected_repr

def test_phone_addition():
    phone1 = Phone("Phone 1", 100, 2, 1)
    phone2 = Phone("Phone 2", 150, 3, 2)

    result = phone1 + phone2
    expected_result = Phone("Phone 1 + Phone 2", 250, 5, 3)

    assert result.name == expected_result.name
    assert result.price == expected_result.price
    assert result.quantity == expected_result.quantity
    assert result.number_of_sim == expected_result.number_of_sim

def test_invalid_number_of_sim():
    with pytest.raises(ValueError):
        invalid_phone = Phone("Invalid Phone", 200, 1, 0)
