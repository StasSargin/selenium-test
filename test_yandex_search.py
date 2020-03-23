from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import allure


@allure.title('Результат поиска')
@allure.severity(Severity.BLOCKER)
def test_yandex_search():
    driver = WebDriver(executable_path='D:\work\chromedriver.exe')
    with allure.step('открываем страницу посика'):
        driver.get('https://ya.ru/')

    with allure.step('Ищем market.yandex.ru'):
        search_input = driver.find_element_by_id("text")
        search_button = driver.find_element_by_xpath("//button[@type='submit']")
        search_input.send_keys("market.yandex.ru")
        search_button.click()

    def check_results_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        return len(inner_search_results) >= 10
    with allure.step('Ожидаем, что количество результатов будет больше 10'):
        WebDriverWait(driver, 5, 0.5).until(check_results_count)
    with allure.step('Переходим по ссылке первого результата'):
        search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        link = search_results[0].find_elements_by_xpath('.//h2/a]')
        link.click()

    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Проверяем тайтл')
        assert driver.title == 'Яндекс.Маркет — выбор и покупка товаров из проверенных интернет-магазинов'



