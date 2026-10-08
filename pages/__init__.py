from pages.base_page import BasePage
from pages.locators import (
    HeaderMenu,
    MainPageLocators,
    RecipeCreateLocators,
    SinginPageLocators,
    SingupPageLocators,
)
from pages.main_page import MainPage
from pages.recipe_page import RecipePage
from pages.singin_page import SinginPage
from pages.singup_page import SingupPage

__all__ = [
    "SingupPage",
    "SinginPage",
    "BasePage",
    "HeaderMenu",
    "MainPage",
    "RecipePage",
    "MainPageLocators",
    "SinginPageLocators",
    "SingupPageLocators",
    "RecipeCreateLocators",
]
