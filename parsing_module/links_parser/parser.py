import time
from fake_useragent import UserAgent
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from parsing_module.links_parser.interface import LinksParserInterface


class LinksParser(LinksParserInterface):

    def __init__(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument(f'user-agent={UserAgent().random}')
        # chrome_options.headless = True
        self._driver = Chrome(chrome_options=chrome_options)

    def _scroll(self, default_delay: int = 1):
        time.sleep(default_delay)
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(default_delay)

    def _collect_links_on_page(self):
        page_links = []
        link_cars = self._driver.find_elements(By.CLASS_NAME, "iva-item-root-_lk9K")
        for car in link_cars:
            link = car.find_element(By.TAG_NAME, "a")
            link = link.get_attribute("href")
            page_links.append(link)
        return page_links

    def _collect_all_links(self, link):
        links = []
        for page in range(1, 2):
            self._driver.get(link + '&p={}'.format(page))
            self._scroll()
            page_links = self._collect_links_on_page()
            links.extend(page_links)
        self._driver.quit()
        return links

    def parse_links(self, link):
        links = self._collect_all_links(link)
        return links






# if __name__ == '__main__':
#     link = "https://www.avito.ru/all/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1"
#     parser = LinksParser()
#     a = parser.parse_links(link)
#     print(len(a))
