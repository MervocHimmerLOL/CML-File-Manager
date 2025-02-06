from datetime import datetime, date
import os
import unittest
import tempfile
import functional


class TestFunctional(unittest.TestCase):

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

    def tearDown(self):
        self.temp_dir_2_layer.cleanup()
        self.temp_dir.cleanup()

    def test_copy(self):
        functional.copy_file(self.temp_file)
        print(f'TEST OF COPY FUNC TEMP FILE = {self.temp_file}')
        copied_file = f"{os.path.splitext(self.temp_file)[0]}_copy{os.path.splitext(self.temp_file)[1]}"
        print(f'TEST OF COPY FUNC COPIED FILE = {copied_file}')
        print(os.listdir(self.temp_dir_path))
        self.assertTrue(os.path.isfile(copied_file), 'There is no copy!!!')
        with open(self.temp_file, 'r') as og, open(copied_file, 'r') as copy:
            self.assertEqual(og.read(), copy.read(), 'Files differ')

    def test_delete(self):
        print(f'TEST OF DELETE FUNC TEMP FILE = {self.temp_file}')
        functional.delete_file(self.temp_file)
        self.assertFalse(os.path.isfile(self.temp_file), 'File is still here!!!')

    def test_count_files(self):
        print('GOTTA TEST COUNT FUNC')
        self.assertEqual(functional.count_files(self.temp_dir_path), 1)
        print("^^^ COUNT FUNC")

    def test_re_search(self):
        self.assertEqual(functional.re_search('test_file.txt', self.temp_dir_path), [self.temp_file])

    def test_date_file(self):
        print('DATE FILE TEST')
        functional.date_file(self.temp_file)
        print(os.listdir(self.temp_dir_path))
        self.assertTrue(f'{date.today().strftime('%Y_%m_%d')}_test_file.txt' in os.listdir(self.temp_dir_path))

    def test_date_dir(self):
        print("DATE DIR TEST")
        functional.date_file(self.temp_dir_path)
        print(os.listdir(self.temp_dir_path))
        self.assertTrue(f'{date.today().strftime('%Y_%m_%d')}_test_file.txt' in os.listdir(self.temp_dir_path))

    def test_date_dir_re(self):
        print("DATE DIR RECURSIVELY TEST")
        functional.date_file(self.temp_dir_path, recursive=True)
        expected = []
        for _, _, file in os.walk(self.temp_dir_path):
            expected.append(file[0])
            print(file)
        print(expected)
        self.assertTrue(f'{date.today().strftime('%Y_%m_%d')}_test_file.txt' and f'{date.today().strftime('%Y_%m_%d')}_test_file_2_layer.txt' in expected)


    def test_analyze(self):
        print('TEST ANALYZE')
        self.assertEqual(functional.analyze(self.temp_dir_path), 24)


if __name__ == "__main__":
    unittest.main()
