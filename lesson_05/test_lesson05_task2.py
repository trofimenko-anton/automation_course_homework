from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    old_url = driver.current_url

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Anton")

    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit order']")
    submit_button.click()

    wait = WebDriverWait(driver, 5)
    wait.until(lambda driver: driver.current_url != old_url)

    assert driver.current_url == "https://httpbin.org/post"

    driver.quit()
