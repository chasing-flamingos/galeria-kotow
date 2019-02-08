import unittest
from selenium import webdriver
import os
from pathlib import Path
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from test.page_objects.MainPage import MainPage

class GalleryTestCase(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Remote(
      command_executor='http://127.0.0.1:4444/wd/hub',
      desired_capabilities=DesiredCapabilities.FIREFOX
    )
    self.workpath = Path().absolute()
    self.path = str(self.workpath) + "/src/galeria.html"
    self.myurl = "file://" + str(self.path)

  def tearDown(self):
    self.driver.close()

  def test_1(self):
    self.driver.get(self.myurl)
    img = self.driver.find_element_by_class_name("myImg")
    img.click()



