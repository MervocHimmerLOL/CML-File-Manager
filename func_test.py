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
        self.temp_file_2_layer = os.path.join(self.temp_dir_2_layer_path, 'test_file.txt')

        with open(self.temp_file, 'w') as file:
            file.write('Hello world!')

        with open(self.temp_file_2_layer, 'w') as file:
            file.write('Hello world!')

    def tearDown(self):
        self.temp_dir_2_layer.cleanup()
        self.temp_dir.cleanup()

    def test_copy(self):
        functional.copy_file(self.temp_file)
        copied_file = f"{os.path.splitext(self.temp_file)[0]}_copy{os.path.splitext(self.temp_file)[1]}"
        self.assertTrue(os.path.isfile(copied_file), 'There is no copy!!!')
        with open(self.temp_file, 'r') as og, open(copied_file, 'r') as copy:
            self.assertEqual(og.read(), copy.read(), 'Files differ')

    def test_delete(self):
        functional.delete_file(self.temp_file)
        self.assertFalse(os.path.isfile(self.temp_file), 'File is still here!!!')


if __name__ == "__main__":
    unittest.main()
