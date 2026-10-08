from random import choice
from string import ascii_lowercase


def generate_random_string(length=10):
    """Генерирует случайную строку из строчных букв."""
    letters = ascii_lowercase
    return "".join(choice(letters) for _ in range(length))


def generate_unique_email():
    """Генерирует уникальный email."""
    return f"{generate_random_string()}@example.com"
