import allure

from pages import BasePage, SingupPageLocators


class SingupPage(BasePage):

    @allure.step("Заполняем поле 'Имя'")
    def first_name_input(self, value):
        self.input_text(SingupPageLocators.FIRST_NAME_INPUT, value)

    @allure.step("Заполняем поле 'Фамилия'")
    def last_name_input(self, value):
        self.input_text(SingupPageLocators.LAST_NAME_INPUT, value)

    @allure.step("Заполняем поле 'Имя пользователя'")
    def username_input(self, value):
        self.input_text(SingupPageLocators.USERNAME_INPUT, value)

    @allure.step("Заполняем поле 'Адрес электронной почты'")
    def email_input(self, value):
        self.input_text(SingupPageLocators.EMAIL_INPUT, value)

    @allure.step("Заполняем поле 'Пароль'")
    def password_input(self, value):
        self.input_text(SingupPageLocators.PASSWORD_INPUT, value)

    @allure.step("Нажимаем кнопку 'Создать аккаунт'")
    def click_registaion_button(self):
        self.click(SingupPageLocators.CREATE_ACCOUNT_BUTTON)
