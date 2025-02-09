from datetime import datetime, date
import os
import unittest
import tempfile

import functional


class TestFunctional(unittest.TestCase):
    """
    Итак, тут мы сетапим простенькую тестовую директорию, она состоит из:
    temp_dir, в который вложены: файл temp_file, папка temp_dir_layer_2, а внутри нее - файл temp_file_2
    Каждая переменная - str(путь к файлу)
    """

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_dir_path = self.temp_dir.name
        self.temp_file = os.path.join(self.temp_dir_path, 'test_file.txt')
        self.temp_dir_2_layer = tempfile.TemporaryDirectory(dir=self.temp_dir_path, prefix='temp_dir_2_layer')
        self.temp_dir_2_layer_path = self.temp_dir_2_layer.name
        self.temp_file_2_layer = os.path.join(self.temp_dir_2_layer_path, 'test_file_2_layer.txt')

        with open(self.temp_file, 'w') as file:
            file.write('Hello world!')

        with open(self.temp_file_2_layer, 'w') as file:
            file.write('Hello world!')

    # Тут мы удаляем папки, сначала вложенную, а потом корневую
    def tearDown(self):
        self.temp_dir_2_layer.cleanup()
        self.temp_dir.cleanup()

    """
    В этом блоке мы тестируем функцию copy.
    Вызываем саму функцию, потом заводим переменную, которая содержит в себе имя файла с _copy
    В первую очередь проверяем, а создалась ли копия вообще, а потом проверяем, одинаково ли содержание og и copy
    """

    def test_copy(self):
        functional.copy_file(self.temp_file)
        copied_file = f"{os.path.splitext(self.temp_file)[0]}_copy{os.path.splitext(self.temp_file)[1]}"
        self.assertTrue(os.path.isfile(copied_file), 'There is no copy!!!')
        with open(self.temp_file, 'r') as og, open(copied_file, 'r') as copy:
            self.assertEqual(og.read(), copy.read(), 'Files differ')
        with self.assertRaises(NotADirectoryError):
            functional.copy_file('file_name.txt')

    # Проверяем функцию delete, если файла нет, то мы его удалили, да.
    def test_delete(self):
        functional.delete_file(self.temp_file)
        self.assertFalse(os.path.isfile(self.temp_file), 'File is still here!!!')
        with self.assertRaises(NotADirectoryError):
            functional.delete_file('file_name.txt')

    # Проверяем умеет ли функция count считать.
    def test_count_files(self):
        self.assertEqual(functional.count_files(self.temp_dir_path), 1)
        with self.assertRaises(NotADirectoryError):
            functional.count_files('file_name.txt')

    # Проверяем поиск файлов с помощью регулярных выражений(эмоджи черепа)
    def test_re_search(self):
        self.assertEqual(functional.re_search('test_file.txt', self.temp_dir_path), [self.temp_file])
        with self.assertRaises(NotADirectoryError):
            functional.re_search('file_name.txt', 'C:\\Dir')

    """
    Тестируем функцию date, и вот тут уже больно, у нее три вариации
    Для файла, папки, и рекурсивная 
    И хоть сейчас, когда все тесты написаны, и я свободен от них
    Я все равно помню боль, когда я писал эти тесты 
    """

    def test_date_file(self):
        functional.date_file(self.temp_file)
        self.assertTrue(f'{date.today().strftime('%Y_%m_%d')}_test_file.txt' in os.listdir(self.temp_dir_path))
        with self.assertRaises(NotADirectoryError):
            functional.date_file('file_name.txt')

    def test_date_dir(self):
        functional.date_file(self.temp_dir_path)
        self.assertTrue(f'{date.today().strftime('%Y_%m_%d')}_test_file.txt' in os.listdir(self.temp_dir_path))
        with self.assertRaises(NotADirectoryError):
            functional.date_file('C:\\NotADir')

    def test_date_dir_re(self):
        functional.date_file(self.temp_dir_path, recursive=True)
        expected = []
        for _, _, file in os.walk(self.temp_dir_path):
            expected.append(file[0])
        self.assertTrue(
            f'{date.today().strftime('%Y_%m_%d')}_test_file.txt' and f'{date.today().strftime('%Y_%m_%d')}_test_file_2_layer.txt' in expected)
        with self.assertRaises(NotADirectoryError):
            functional.date_file('C:\\NotADir', recursive=True)

    # Я думал, для функции анализа веса файлов понадобится более сложный тест, наверно да, нужен, но и это неплохо работает
    def test_analyze(self):
        self.assertEqual(functional.analyze(self.temp_dir_path), 24)
        with self.assertRaises(NotADirectoryError):
            functional.analyze('C:\\NotADir')


if __name__ == "__main__":
    unittest.main()
