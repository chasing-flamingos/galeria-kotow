from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(object):

  def __init__(self, driver):
    self.driver = driver

  def select_image(self):
    img = self.driver.find_element_by_class_name("myImg")
    img.click()

  def expect_modal_image(self):
    try:
      element = WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.ClassName, "modal"))
      )
    except:
      pass

  def click_next_arrow(self):
    next_arrow = self.driver.find_element_by_class_name("next")
    next_arrow.click()

  def keydown_next_image(self):
    document = self.driver.find_element_by_tag_name("html")
    document.send_keys(Keys.ARROW_RIGHT)

  def get_modal_image(self):
    img = self.driver.find_element_by_id("myModalImg")
    return img.get_attribute("src")

  def click_prev_arrow(self):
    prev_arrow = self.driver.find_element_by_class_name("prev")
    prev_arrow.click()

  def keydown_prev_image(self):
    document = self.driver.find_element_by_tag_name("html")
    document.send_keys(Keys.ARROW_LEFT)

  def select_last_image(self):
    last_img = self.driver.find_element_by_xpath("//img[@src='galeria_foto/kot9.jpg']")
    last_img.click()








