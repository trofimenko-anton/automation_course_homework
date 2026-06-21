from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ВНИМАНИЕ: для запуска теста замените значения cookie
# на свои актуальные. Как получить cookie:
# 1. Войдите в аккаунт на https://gitflic.ru/
# 2. Откройте DevTools (F12) → Application → Cookies → https://gitflic.ru
# 3. Найдите куку с именем "SESSION" и скопируйте её значение (Value)
# 4. Вставьте скопированное значение вместо плейсхолдеров ниже

USER1_COOKIE = {
    "name": "SESSION",
    "value": "ваш_токен_пользователя1",
    "domain": "gitflic.ru",
}
USER2_COOKIE = {
    "name": "SESSION",
    "value": "ваш_токен_пользователя2",
    "domain": "gitflic.ru",
}
USER1_USERNAME = "ваше_имя_пользователя1"
USER2_USERNAME = "ваше_имя_пользователя2"


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    # ---- Пользователь 1 ----
    driver.delete_all_cookies()
    driver.add_cookie(USER1_COOKIE)
    driver.refresh()

    # Переходим на страницу профиля первого пользователя
    driver.get(f"https://gitflic.ru/user/{USER1_USERNAME}")

    # Явно ждём, пока URL не будет содержать "/user/username"
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains(f"/user/{USER1_USERNAME}"))
    url_user1 = driver.current_url

    # Проверяем отображение имени пользователя 1 на странице
    user1_name_element = wait.until(
        EC.visibility_of_element_located
        ((By.CSS_SELECTOR, ".user-profile__name h6.mb-0"))
    )
    assert user1_name_element.text.strip() == USER1_USERNAME, (
        f"Ожидалось имя пользователя '{USER1_USERNAME}', "
        f"но найдено '{user1_name_element.text}'"
    )

    # ---- Пользователь 2 ----
    # Разлогиниваемся
    driver.delete_all_cookies()
    driver.add_cookie(USER2_COOKIE)
    driver.refresh()
    # Переходим на страницу профиля второго пользователя
    driver.get(f"https://gitflic.ru/user/{USER2_USERNAME}")
    # Явно ждём, пока URL не будет содержать "/user/username"
    wait.until(EC.url_contains(f"/user/{USER2_USERNAME}"))
    url_user2 = driver.current_url

    # Проверяем отображение имени пользователя 2 на странице
    user2_name_element = wait.until(
        EC.visibility_of_element_located
        ((By.CSS_SELECTOR, ".user-profile__name h6.mb-0"))
    )
    assert user2_name_element.text.strip() == USER2_USERNAME, (
        f"Ожидалось имя пользователя '{USER2_USERNAME}', "
        f"но найдено '{user2_name_element.text}'"
    )

    # Проверяем, что URL двух профилей различаются
    assert url_user1 != url_user2, (
        f"URL профилей совпадают: {url_user1} == {url_user2}"
    )

    driver.quit()
