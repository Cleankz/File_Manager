
class Folder:

    def __init__(self,folder_name: str, create_date: int,folder_files: list):
        self.__folder_name = folder_name
        self.__create_date = create_date
        self.__folder_files = folder_files
        self.__extra_data = {}

    @classmethod
    def found_folder(cls):
        ...

    @classmethod
    def make_folder(cls):
        ...

    @classmethod
    def delete_folder(cls):
        ...

    @classmethod
    def save_folder(cls):
        ...

    @property
    def folder_info(self) -> str:
        ...

    @property
    def folder_contents(self):
        ...
    # варавптаптавьлангьрпь