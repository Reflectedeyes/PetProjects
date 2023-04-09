# -*- coding: utf-8 -*-
# Импорт нужных библиотек
import os
from shutil import copy2
from time import gmtime

# Указываем путь до папки, которую нужно отсортировать
source_path = 'PATH_TO_SOURCE_DIRECTORY'
my_dir = os.path.dirname(__file__)
# Указываем путь до папки, в которую будем перемещать сортированные файлы
sorted_directory = os.path.normpath(os.path.join(my_dir, 'PATH_TO_SORTED_DIRECTORY'))
os.makedirs(sorted_directory, exist_ok=True)

# Сам скрипт


class FilesArrange:

    def __init__(self, folder_in, folder_out):
        self.folder_in = folder_in
        self.folder_out = folder_out
        self.extract()

    def extract(self):
        for dirpath, dirnames, filenames in os.walk(self.folder_in):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = gmtime(secs)
                file_year = str(file_time[0])
                file_month = str(file_time[1])

                file_src_year = os.path.normpath(os.path.join(sorted_directory, file_year))
                os.makedirs(file_src_year, exist_ok=True)

                file_src_year_month = os.path.normpath(os.path.join(file_src_year, file_month))
                os.makedirs(file_src_year_month, exist_ok=True)

                copy2(full_file_path, file_src_year_month)


# Вызов функции


FilesArrange(source_path, sorted_directory)
