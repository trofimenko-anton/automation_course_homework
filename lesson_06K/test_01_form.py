from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_form_validation():
    driver = webdriver.Edge()
    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        wait = WebDriverWait(driver, 10)

        # Заполняем форму
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставляем пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Отправляем форму
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Ждём, пока поле zip-code получит класс alert-danger и станет красным
        wait.until(
            lambda d: "alert-danger" in d.find_element
            (By.ID, "zip-code").get_attribute("class")
        )

        # Проверяем Zip code – красный
        zip_code = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code.get_attribute("class")

        # Проверяем остальные поля – зелёные
        green_fields = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]
        for field_id in green_fields:
            element = driver.find_element(By.ID, field_id)
            assert "alert-success" in element.get_attribute("class"), \
                f"Поле {field_id} должно быть зелёным"

    finally:
        driver.quit()
