from src.item import Item


class LanguageMixin:
    def __init__(self, language='EN'):
        if language in ['EN', 'RU']:
            self._language = language
        else:
            raise ValueError("Language must be 'EN' or 'RU'")

    @property
    def language(self):
        return self._language

    def change_lang(self):
        self._language = 'RU' if self._language == 'EN' else 'EN'


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity, language='EN'):
        Item.__init__(self, name, price, quantity)
        LanguageMixin.__init__(self, language)
