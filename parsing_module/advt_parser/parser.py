import tqdm
import time
from pymongo import MongoClient
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from parsing_module.links_parser.parser import LinksParser
from parsing_module.advt_parser.interface import AdsParserInterface


class AdsParser(AdsParserInterface):
    def __init__(self):
        client = MongoClient()
        self._driver = Chrome()
        self._links_parser = LinksParser()
        self._collection = client["data_cars"]["cars"]

    def _scroll(self, default_delay: int = 1):
        time.sleep(default_delay)
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def parse(self, request_link):
        links = self._links_parser.parse_links(request_link)
        for link in tqdm.tqdm(links):
            try:
                data_car = {}
                self._driver.get(link)
                self._scroll()
                basic_information = self._driver.find_elements(By.CLASS_NAME, 'params-paramsList__item-appQw')
                car_name = self._driver.find_elements(By.CLASS_NAME, 'title-info-title-text')
                data_car["Ссылка"] = link
                price = self._driver.find_elements(By.CLASS_NAME, "style-price-value-main-TIg6u")[1].text
                data_car["Цена"] = price
                if car_name: data_car["Автомобиль"] = car_name[-1].text
                for car in basic_information:
                    key, value = car.text.split(':')
                    data_car[key] = value
                try:
                    data_car["Описание"] = self._driver.find_element(By.CLASS_NAME, "style-item-description-text-mc3G6")
                except NoSuchElementException:
                    data_car["Описание"] = None
                self._collection.insert_one(data_car)
            except Exception as error:
                print(f"[ERROR]: {str(error)}")
                input('press to continue')
                continue


# if __name__ == '__main__':
#     request = "https://www.avito.ru/all/avtomobili/bmw/x7-ASgBAQICAUTitg3EtCgBQOC2DRTklyg?cd=1"
#     parser = AdsParser()
#     parser.parse(request)
