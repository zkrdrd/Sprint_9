from pathlib import Path

import allure

from helpers import generate_random_string
from pages import BasePage, RecipeCreateLocators


class RecipePage(BasePage):

    @allure.step("Нажимаем кнопку 'Создать рецепт'")
    def click_create_recipe_link(self):
        self.click(RecipeCreateLocators.CREATE_RECIPE)

    def generate_recipe_name(self):
        return generate_random_string()

    @allure.step("Заполняем поле 'Название рецепта'")
    def recipe_name_input(self, recipe_name):
        self.input_text(RecipeCreateLocators.RECIEPE_NAME_INPUT, recipe_name)

    @allure.step("Заполняем поле 'Ингридиенты'")
    def ingridient_input(self):
        self.input_text(RecipeCreateLocators.INGRIDIENT, "к")
        self.click(RecipeCreateLocators.ZUCCHINI)
        self.input_text(RecipeCreateLocators.INGRIDIENT_WEIGHT, "100")

    @allure.step("Нажимаем кнопку 'Добавить ингридиент'")
    def click_add_ingridient_button(self):
        self.click(RecipeCreateLocators.INGRIDIENT_ADD)

    @allure.step("Заполняем поле 'Время приготовления'")
    def cooking_time_input(self):
        self.input_text(RecipeCreateLocators.COOKING_TIME, "10")

    @allure.step("Заполняем поле 'Описание рецепта'")
    def description_input(self):
        self.input_text(RecipeCreateLocators.DESCRIPTION, generate_random_string())

    @allure.step("Заушружаем фото")
    def upload_image_input(self):
        self.upload_image(
            str(
                Path(__file__)
                .parents[1]
                .joinpath("helpers")
                .joinpath("media")
                .joinpath("zucchini.png")
            ),
            *RecipeCreateLocators.UPLOAD_IMAGE,
        )

    @allure.step("Нажимаем кнопку 'Создать рецепт'")
    def click_create_recipe_button(self):
        self.click(RecipeCreateLocators.CREATE_BUTTON)

    def get_text_recipe_name(self):
        return self.get_text(RecipeCreateLocators.RECIPE_NAME)

    def visible_recipe_card(self):
        return self.is_element_present(RecipeCreateLocators.RECIPE_CARD)
