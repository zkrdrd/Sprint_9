from pages import BasePage, MainPageLocators


class MainPage(BasePage):

    def visibility_recipe_header(self):
        return self.visibility_element(MainPageLocators.RECIPE_HEADER)

    def visibility_exit_button(self):
        return self.visibility_element(MainPageLocators.EXIT_BUTTON)
