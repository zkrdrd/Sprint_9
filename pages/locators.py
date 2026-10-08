from selenium.webdriver.common.by import By


class HeaderMenu:
    __MENU_ELEMENT = "//div[contains(@class, 'style_headerContent__fyAv7')]"
    SINGUP_LINK = (
        By.XPATH,
        f"{__MENU_ELEMENT}//a[contains(text(),'Создать аккаунт')]",
    )
    SINGIN_LINK = (
        By.XPATH,
        f"{__MENU_ELEMENT}//a[contains(text(),'Войти')]",
    )
    RECIPES_LINK = (
        By.XPATH,
        f"{__MENU_ELEMENT}//a[contains(text(),'Рецепты')]",
    )
    EXIT_BUTTON = (By.XPATH, f"{__MENU_ELEMENT}//a[contains(text(), 'Выход')]")
    CREATE_RECIPE = (
        By.XPATH,
        f"{__MENU_ELEMENT}//a[contains(text(), 'Создать рецепт')]",
    )


class SingupPageLocators:
    """Локаторы страницы регистрации"""

    __REGISTRATION_FORM = (
        "//form[contains(@class, 'styles_form__2nwxz styles_form__24nV3')]"
    )
    FIRST_NAME_INPUT = (
        By.XPATH,
        f"{__REGISTRATION_FORM}//input[contains(@name, 'first_name')]",
    )
    LAST_NAME_INPUT = (
        By.XPATH,
        f"{__REGISTRATION_FORM}//input[contains(@name, 'last_name')]",
    )
    USERNAME_INPUT = (
        By.XPATH,
        f"{__REGISTRATION_FORM}//input[contains(@name, 'username')]",
    )
    EMAIL_INPUT = (
        By.XPATH,
        f"{__REGISTRATION_FORM}//input[contains(@name, 'email')]",
    )
    PASSWORD_INPUT = (
        By.XPATH,
        f"{__REGISTRATION_FORM}//input[contains(@name, 'password')]",
    )
    CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        f"{__REGISTRATION_FORM}//button[contains(text(),'Создать аккаунт')]",
    )


class SinginPageLocators(HeaderMenu):
    __SINGIN_FORM = "//form[contains(@class, 'styles_form__2nwxz styles_form__2_42b')]"
    SINGIN_TEXT = (
        By.XPATH,
        "//div[contains(@class, 'style_container__mLpjI')]//h1[contains(text(), 'Войти на сайт')]",
    )
    EMAIL_INPUT = (By.XPATH, f"{__SINGIN_FORM}//input[contains(@name, 'email')]")
    PASSWORD_INPUT = (By.XPATH, f"{__SINGIN_FORM}//input[contains(@name, 'password')]")
    SINGIN_BUTTON = (
        By.XPATH,
        f"{__SINGIN_FORM}//button[contains(text(),'Войти')]",
    )


class MainPageLocators(HeaderMenu):
    RECIPE_HEADER = (By.XPATH, "//h1[contains(text(), 'Рецепты')]")


class RecipeCreateLocators(HeaderMenu):
    RECIEPE_NAME_INPUT = (
        By.XPATH,
        "//div[contains(text(), 'Название рецепта')]//following-sibling::input",
    )
    INGRIDIENT = (
        By.XPATH,
        "//div[contains(@class,'styles_ingredientsInputs__1W-NV')]//div[contains(text(),'Ингредиенты')]//following-sibling::input",
    )
    ZUCCHINI = (By.XPATH, "//div[text()='кабачки']")
    INGRIDIENT_WEIGHT = (
        By.XPATH,
        "//input[contains(@class, 'styles_inputField__3eqTj styles_ingredientsAmountValue__2matT')]",
    )
    INGRIDIENT_ADD = (By.XPATH, "//div[contains(text(), 'Добавить ингредиент')]")
    COOKING_TIME = (
        By.XPATH,
        "//div[contains(text(), 'Время приготовления')]//following-sibling::input",
    )
    DESCRIPTION = (
        By.XPATH,
        "//div[contains(text(), 'Описание рецепта')]//following-sibling::textarea",
    )
    UPLOAD_IMAGE = (
        By.XPATH,
        "//div[contains(text(),'Выбрать файл')]//preceding-sibling::input[@type='file']",
    )
    CREATE_BUTTON = (By.XPATH, "//button[contains(text(),'Создать рецепт')]")
    RECIPE_NAME = (
        By.XPATH,
        "//h1[contains(@class, 'styles_single-card__title__2QMPq')]",
    )
    RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'styles_single-card__1yTTj')]")
