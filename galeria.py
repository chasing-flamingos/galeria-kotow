import unittest
from test.GalleryTestCase import GalleryTestCase

def suite():
  suite = unittest.TestSuite()
  suite.addTest(GalleryTestCase('test_show_modal_on_click'))
  suite.addTest(GalleryTestCase('test_next_image_arrow'))
  suite.addTest(GalleryTestCase('test_next_image_keyboard_shortcut'))
  suite.addTest(GalleryTestCase('test_previous_image_arrow'))
  suite.addTest(GalleryTestCase('test_previous_image_keyboard_shortcut'))
  suite.addTest(GalleryTestCase('test_images_carousel'))
  return suite


if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(suite())