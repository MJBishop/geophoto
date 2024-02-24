import unittest
import os
from geophoto.exif_reader import read_exif


class TestExifReader(unittest.TestCase):

    def setUp(self):
        self.in_path = 'tests/test_files/test_images/test_exif/'
        self.file_dir = 'test_folder/EXIF.jpg'
        self.filepath = os.path.join(self.in_path, self.file_dir)

    def test_read_exif_coord(self):
        test_coord = (-8.631052777777779, 115.09526944444444)
        with open(self.filepath, 'rb') as image_file:
            coord, props, thumb_f = read_exif(image_file)
        self.assertEqual(test_coord, coord)

    def test_read_exif_datetime(self):
        datetime = "2023-05-05 06:19:24"
        with open(self.filepath, 'rb') as image_file:
            coord, props, thumb_f = read_exif(image_file)
        self.assertEqual(props['datetime'], datetime)

    def test_read_exif_thumbnail_file(self):
        with open(self.filepath, 'rb') as image_file:
            coord, props, thumb_f = read_exif(image_file)
        self.assertIsNotNone(thumb_f)



if __name__ == '__main__':
    unittest.main()