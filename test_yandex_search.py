from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


def test_yandex_search():
    driver = WebDriver(executable_path='D:\work\chromedriver.exe')            #Указываем путь к драйверу.
    driver.get('https://ya.ru/')                                              #Указываем путь к нужному сайту.
    search_input = driver.find_element_by_id("text")
    search_button = driver.find_element_by_xpath("//button[@type='submit']")
    search_input.send_keys("market.yandex.ru")
    search_button.click()

    def check_results_count(driver):                                          #Ищем количество элементов, проверяем и возвращаем True.
        inner_search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        return len(inner_search_results) >= 10

    WebDriverWait(driver, 5, 0.5).until(check_results_count)                   #Ждем пока не вернется True.

    search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]') #Ищем первый линк.
    link = search_results[0].find_elements_by_xpath('.//h2/a]')
    link.click()                                                               #Кликаем в него.
    driver.switch_to.window(driver.window_handles[1])                          #Переключаемся во 2ую вкладку.
    assert driver.title == 'Яндекс.Маркет — выбор и покупка товаров из проверенных интернет-магазинов' #Проверяем тайтл



