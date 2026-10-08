from dataclasses import dataclass


class URL:
    BASE_URL = "https://foodgram-frontend-1.foodgram.education-services.ru"


@dataclass
class Credential:
    FIRST_NAME: str
    LAST_NAME: str
    USERNAME: str
    EMAIL: str
    PASSWORD: str
