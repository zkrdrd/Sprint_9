import allure

from pages import BasePage, SinginPageLocators


class SinginPage(BasePage):

    @allure.step("Нажимаем кнопку 'Создать аккаунт'")
    def click_singup_button(self):
        self.click(SinginPageLocators.SINGUP_LINK)

    @allure.step("Заполняем поле 'Адрес электронной почты'")
    def username_input(self, value):
        self.input_text(SinginPageLocators.EMAIL_INPUT, value)

    @allure.step("Заполняем поле 'Пароль'")
    def password_input(self, value):
        self.input_text(SinginPageLocators.PASSWORD_INPUT, value)

    @allure.step("Нажимаем кнопку 'Войти'")
    def click_singin_button(self):
        self.click(SinginPageLocators.SINGIN_BUTTON)

    def visibility_email_input(self):
        return self.visibility_element(SinginPageLocators.EMAIL_INPUT)

    def visibility_password_input(self):
        return self.visibility_element(SinginPageLocators.PASSWORD_INPUT)

    def visibility_registaion_input(self):
        return self.visibility_element(SinginPageLocators.SINGIN_BUTTON)

    def visibility_singin_text(self):
        return self.visibility_element(SinginPageLocators.SINGIN_TEXT)
