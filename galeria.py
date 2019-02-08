import unittest
from test.GalleryTestCase import GalleryTestCase

def suite():
  suite = unittest.TestSuite()
  suite.addTest(GalleryTestCase('test_1'))
  return suite


if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(suite())