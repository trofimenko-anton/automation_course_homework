from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)

    try:
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        driver.get(url)

        # Устанавливаем задержку 45 секунд
        delay = driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys("45")

        # Нажимаем 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Сохраняем элемент с результатом
        screen = driver.find_element(By.CLASS_NAME, "screen")

        # Ждём, пока в этом элементе не появится значение "15"
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), "15"
            )
        )

        assert screen.text == "15", (
            f"Ожидалось 15, но получено {screen.text}"
        )

    finally:
        driver.quit()
