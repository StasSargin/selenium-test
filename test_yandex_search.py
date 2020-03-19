from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


def test_yandex_search():
    driver = WebDriver(executable_path='D:\work\chromedriver.exe')
    driver.get('https://ya.ru/')
    search_input = driver.find_element_by_id("text")
    search_button = driver.find_element_by_xpath("//button[@type='submit']")
    search_input.send_keys("market.yandex.ru")
    search_button.click()

    def check_results_count(driver):
        search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        return len(search_results) == 10

    WebDriverWait(driver, 5, 0.5).until(check_results_count)

