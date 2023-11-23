from dataclasses import dataclass


@dataclass
class File:
    file_name: str
    create_date: int
    def make_file(self):
        ...
    def delete_file(self):
        ...
    def save_file(self):
        ...
    def file_info(self) -> str:
        ...
    def file_contents(self):
        ...

@dataclass
class Folder:
    folder_name: str
    create_date: int
    folder_files: list

    def make_folder(self):
        ...
    def delete_folder(self):
        ...
    def save_folder(self):
        ...
    def folder_info(self) -> str:
        ...
    def folder_contents(self):
        ...



@dataclass
class User:
    name: str
    date_registation: int

    def check_users_rulls(self):
        ...