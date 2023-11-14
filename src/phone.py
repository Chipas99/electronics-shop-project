# -*- coding: utf-8 -*-
from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)

        if not isinstance(number_of_sim, int) or number_of_sim <= 0:
            raise ValueError("Number of SIM cards must be a positive integer.")

        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            return Phone(
                f"{self.name} + {other.name}",
                self.price + other.price,
                self.quantity + other.quantity,
                self.number_of_sim + other.number_of_sim
            )
        else:
            raise TypeError("Unsupported type for addition.")
