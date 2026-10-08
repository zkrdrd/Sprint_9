import allure

from pages import RecipePage, SinginPage


class TestCreateRecipe:
    @allure.title("Создание рецепта")
    def test_create_recipe(self, driver, registration_user):
        singin = SinginPage(driver)
        singin.open_page()
        singin.username_input(registration_user.USERNAME)
        singin.password_input(registration_user.PASSWORD)
        singin.click_singin_button()
        recipe_creator = RecipePage(driver)
        recipe_name = recipe_creator.generate_recipe_name()
        recipe_creator.click_create_recipe_link()
        recipe_creator.recipe_name_input(recipe_name)
        recipe_creator.ingridient_input()
        recipe_creator.click_add_ingridient_button()
        recipe_creator.cooking_time_input()
        recipe_creator.description_input()
        recipe_creator.upload_image_input()
        recipe_creator.click_create_recipe_button()
        assert recipe_creator.visible_recipe_card()
        assert recipe_creator.get_text_recipe_name() == recipe_name
