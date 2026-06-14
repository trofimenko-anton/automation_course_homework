from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    old_url = driver.current_url

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Антон Трофименко")

    submit_button = driver.find_element(
        By.XPATH,
        "//button[text()='Submit order']"
    )
    submit_button.click()

    time.sleep(3)

    assert driver.current_url != old_url

    driver.quit()
