import os


def delete_file(path: str) -> None:
    '''
    Рекурсивная функция для удаления файлов/папок в заданном пути
    :param path: путь к файлу/папке
    :return: None
    '''
    # Если путь указывает на файл
    if os.path.isfile(path):
        os.remove(path)  # Удаление файла
    else:
        dir_list = os.listdir(path)  # Иначе получение списка файлов/папок в заданном пути
        for i in dir_list:
            file_path = os.path.join(path, i)  # Составление полного пути к файлу/папке
            if os.path.isfile(file_path):  # Если текущий элемент является файлом
                os.remove(file_path)  # Удалить файл
            else:
                delete_file(file_path)  # Рекурсивный вызов функции для удаления файлов/папок во вложенной папке
                os.rmdir(file_path)  # Удалить вложенную папку
        os.rmdir(path)  # Удалить исходную папку


def delete(path: str) -> bool:
    '''
    Функция принимает на вход путь к папке или файлу и удаляет его/её
    :param path: путь к папке/файлу
    :return: True - если удаление прошло успешно, в противном случае, вернёт False
    '''

    # Если путь не существует
    if not (os.path.exists(path)):
        return False
    else:
        delete_file(path)  # Вызов функции для удаления файлов/папок по заданному пути
        return True
