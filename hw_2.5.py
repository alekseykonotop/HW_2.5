import subprocess
import os
from pprint import pprint

# 1. Получаем список файлов в папке Source
# 2. Используем название элемента списка файлов, чтобы прописать путь
# 3. Делаем полную копию каждого файла и сохраняем в папке "Result" с проверкой
#    существования этой папки. Если нет, создаем, если есть, то кладем в нее очеердной файл.
# 4. Используя функцию sips --resampleWidth 200 input.jpg изменяем размер и сохраняем результат.


def get_photos_list():
    """Функция получает в виде списка перечень файлов и папок
    в папке Source для последующей передачи."""
    photos_list = os.listdir(path="Source/")
    return photos_list
    # pprint(photos_list) # Отладочный принт, удалить


def get_photos_copies() # Остановился на написании фукции, которая создает копию фото и сохраняет ее с папке "Result"

get_photos_list()