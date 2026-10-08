import allure

from pages import MainPage, SinginPage, SingupPage


class TestSingUp:
    @allure.title("Создание учетной записи")
    def test_sing_up(self, driver, credentials):
        singin = SinginPage(driver)
        singin.open_page()
        singin.click_singup_button()
        singup = SingupPage(driver)
        singup.first_name_input(credentials.FIRST_NAME)
        singup.last_name_input(credentials.LAST_NAME)
        singup.username_input(credentials.USERNAME)
        singup.email_input(credentials.EMAIL)
        singup.password_input(credentials.PASSWORD)
        singup.click_registaion_button()
        assert singin.visibility_email_input()
        assert singin.visibility_password_input()
        assert singin.visibility_registaion_input()
        assert singin.visibility_singin_text()


class TestSingIn:
    @allure.title("Вход в учетную запись")
    def test_sing_in(self, driver, registration_user):
        singin = SinginPage(driver)
        singin.open_page()
        singin.username_input(registration_user.USERNAME)
        singin.password_input(registration_user.PASSWORD)
        singin.click_singin_button()
        main_page = MainPage(driver)
        assert main_page.visibility_exit_button()
        assert main_page.visibility_recipe_header()
