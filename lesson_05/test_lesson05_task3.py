import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.xfail(reason="На странице 9 ссылок вместо ожидаемых 10")
def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")

    assert len(links) == 10

    for link in links:
        assert link.is_displayed()

    assert "1" in links[0].text

    driver.quit()
