from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    start_url = "https://httpbin.org/"
    driver.get(start_url)

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML form")
    html_form_link.click()

    assert driver.current_url.endswith("/forms/post"), \
        f"Новый URL: /forms/post, получен: {driver.current_url}"

    driver.back()

    assert driver.current_url == start_url, \
        f"Ожидался {start_url}, получен: {driver.current_url}"

    driver.quit()
