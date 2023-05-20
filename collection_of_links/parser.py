from selenium.webdriver.common.by import By
from collection_of_links.collection_of_links_interface import CollectionOfLinksInterface
import time
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


class CollectionOfLinks(CollectionOfLinksInterface):

    def __init__(self):
        chrome_options = ChromeOptions()
        ua = UserAgent()
        userAgent = ua.random
        chrome_options.add_argument(f'user-agent={userAgent}')
        # chrome_options.headless = True
        self._driver = Chrome(chrome_options=chrome_options)

    # chrome_options = chrome_options - аргумент Crome

    def _scroll(self, default_delay: int = 1):
        time.sleep(default_delay)
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(default_delay)

    def _collecting_links(self):
        page_links = []
        link_cars = self._driver.find_elements(By.CLASS_NAME, "iva-item-root-_lk9K")
        for car in link_cars:
            link = car.find_element(By.TAG_NAME, "a")
            link = link.get_attribute("href")
            page_links.append(link)
        return page_links

    def _pagination(self, link):
        links = []
        for i in range(1, 2):
            self._driver.get(link + '&p={}'.format(i))
            self._scroll()
            page_links = self._collecting_links()
            links.extend(page_links)
        self._driver.quit()
        return links

    def sources_data(self, link):
        links = self._pagination(link)
        return links

#
# model = "https://www.avito.ru/all/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1"
# obj = CollectionOfLinks()
# a = obj.sources_data(model)
# print(len(a))
