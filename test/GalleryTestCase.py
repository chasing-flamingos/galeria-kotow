import unittest
from selenium import webdriver
import os
from pathlib import Path
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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

  def test_show_modal_on_click(self):
    self.driver.get(self.myurl)
    main_page = MainPage(self.driver)
    main_page.select_image()
    main_page.expect_modal_image()
    original_image = main_page.get_modal_image()
    self.assertEqual("file://" + str(self.workpath) + "/src/galeria_foto/kot1.jpeg", original_image)

  def test_next_image_arrow(self):
    self.driver.get(self.myurl)
    main_page = MainPage(self.driver)
    main_page.select_image()
    main_page.expect_modal_image()
    original_image = main_page.get_modal_image()
    main_page.click_next_arrow()
    time.sleep(1)
    new_image = main_page.get_modal_image()
    self.assertEqual("file://" + str(self.workpath) + "/src/galeria_foto/kot2.jpg", new_image)

  def test_next_image_keyboard_shortcut(self):
    self.driver.get(self.myurl)
    main_page = MainPage(self.driver)
    main_page.select_image()
    main_page.expect_modal_image()
    original_image = main_page.get_modal_image()
    main_page.keydown_next_image()
    time.sleep(1)
    new_image = main_page.get_modal_image()
    self.assertEqual("file://" + str(self.workpath) + "/src/galeria_foto/kot2.jpg", new_image)

  def test_previous_image_arrow(self):
    self.driver.get(self.myurl)
    main_page = MainPage(self.driver)
    main_page.select_image()
    main_page.expect_modal_image()
    original_image = main_page.get_modal_image()
    main_page.click_prev_arrow()
    time.sleep(1)
    new_image = main_page.get_modal_image()
    self.assertEqual("file://" + str(self.workpath) + "/src/galeria_foto/kot9.jpg", new_image)

  def test_previous_image_keyboard_shortcut(self):
    self.driver.get(self.myurl)
    main_page = MainPage(self.driver)
    main_page.select_image()
    main_page.expect_modal_image()
    original_image = main_page.get_modal_image()
    main_page.keydown_prev_image()
    time.sleep(1)
    new_image = main_page.get_modal_image()
    self.assertEqual("file://" + str(self.workpath) + "/src/galeria_foto/kot9.jpg", new_image)

  def test_images_carousel(self):
    self.driver.get(self.myurl)
    main_page = MainPage(self.driver)
    main_page.select_last_image()
    main_page.expect_modal_image()
    original_image = main_page.get_modal_image()
    main_page.click_next_arrow()
    time.sleep(1)
    new_image = main_page.get_modal_image()
    self.assertEqual("file://" + str(self.workpath) + "/src/galeria_foto/kot1.jpeg", new_image)
