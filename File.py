
class File:
    def __init__(self, file_name: str, create_date: int):
        self.__f_name = file_name
        self.__c_date = create_date
        self.__extra_data = {}

    @classmethod
    def make_file(cls):
        ...
    @classmethod
    def delete_file(cls):
        ...
    @classmethod
    def save_file(cls):
        ...
    @classmethod
    def found_file(cls):
        ...
    @property
    def file_info(self) -> str:
        ...
    @property
    def file_contents(self):
        ...
