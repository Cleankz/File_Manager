class User:

    def __init__(self, name: str, date_registration: int):
        self.__user_name = name
        self.__registration_date = date_registration
        self.__extra_data = {}

    @property
    def check_users_rulls(self):
        ...