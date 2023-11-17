import pytest
from src.keyboard import Keyboard

def test_keyboard_initialization():
    kb = Keyboard('Test Keyboard', 50, 15)
    assert kb.name == 'Test Keyboard'
    assert kb.price == 50
    assert kb.quantity == 15
    assert kb.language == 'EN'

def test_keyboard_initial_language():
    kb = Keyboard('Test Keyboard', 50, 15)
    assert kb.language == 'EN'

def test_keyboard_change_language():
    kb = Keyboard('Test Keyboard', 50, 15)
    kb.change_lang()
    assert kb.language == 'RU'

def test_language_initialization():
    with pytest.raises(ValueError):
        Keyboard('Test Keyboard', 50, 15, 'DE')

def test_language_change_error():
    kb = Keyboard('Test Keyboard', 50, 15)
    kb.change_lang()
    kb.change_lang()
    assert kb.language == 'EN'
