import selenium.common.exceptions
from selenium.webdriver.common.by import By
from parser_links.parser_links_interface import ParserLinksInterface
from collection_of_links.parser import CollectionOfLinks
from selenium.webdriver import Chrome
from pymongo import MongoClient
import tqdm
import time


class ParserLinks(ParserLinksInterface):
    def __init__(self):
        self._data_links = CollectionOfLinks()
        self._driver = Chrome()
        client = MongoClient()
        self._collection = client["data_cars"]["cars"]

    def _scroll(self, default_delay: int = 1):
        time.sleep(default_delay)
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def parse_links(self, link_model):
        data_links = self._data_links.sources_data(link_model)
        for link in tqdm.tqdm(data_links):
            try:
                data_car = {}
                self._driver.get(link)
                self._scroll()
                basic_information = self._driver.find_elements(By.CLASS_NAME, 'params-paramsList__item-appQw')
                car_name = self._driver.find_elements(By.CLASS_NAME, 'title-info-title-text')
                data_car["Ссылка"] = link
                price = self._driver.find_elements(By.CLASS_NAME, "style-price-value-main-TIg6u")[1].text
                data_car["Цена"] = price
                if car_name:
                    car_name = car_name[-1].text
                    data_car["Автомобиль"] = car_name
                # if car_name[-1].text:
                #     car_name = car_name[-1].text
                #     data_car["car"] = car_name
                # else:
                #     car_name = car_name[0].text
                #     data_car["car"] = car_name
                for car in basic_information:
                    key, value = car.text.split(':')
                    data_car[key] = value
                try:
                    description = self._driver.find_element(By.CLASS_NAME, "style-item-description-text-mc3G6")
                    data_car["Описание"] = description.text
                except selenium.common.exceptions.NoSuchElementException:
                    data_car["Описание"] = None
                self._collection.insert_one(data_car)
            except:
                input('press to continue')
                continue


# model = "https://www.avito.ru/all/avtomobili/audi-ASgBAgICAUTgtg3elyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/100-ASgBAgICAkTgtg3elyjitg3gmSg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/80-ASgBAQICAUTitg2MnSgBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/a3-ASgBAQICAUTitg3gnSgBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/a4-ASgBAQICAUTitg3inSgBQOC2DRTelyg?cd=1"
# model ="https://www.avito.ru/all/avtomobili/audi/a5-ASgBAQICAUTitg3mnSgBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/a6-ASgBAQICAUTitg3onSgBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/a7-ASgBAQICAUTitg3snSgBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/a8-ASgBAQICAUTitg3unSgBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/q3-ASgBAQICAUTitg3KrSgBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/q5-ASgBAQICAUTitg3OrSgBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/q7-ASgBAQICAUTitg3UrSgBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/q8-ASgBAQICAUTitg3YrSgBQOC2DRTelyg?cd=1 ------"
# model = "https://www.avito.ru/all/avtomobili/audi/rs5-ASgBAQICAUTitg3wrigBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/rs6-ASgBAQICAUTitg3yrigBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/rs7-ASgBAQICAUTitg30rigBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/s5-ASgBAQICAUTitg2arygBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/s6-ASgBAQICAUTitg2crygBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/s8-ASgBAQICAUTitg2mrygBQOC2DRTelyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/audi/tt-ASgBAQICAUTitg3gsigBQOC2DRTelyg?cd=1"
# ----------------------------------------
# model = "https://www.avito.ru/all/avtomobili/bmw/1_seriya-ASgBAQICAUTitg2qmigBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/3_seriya-ASgBAQICAUTitg32mygBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/4_seriya-ASgBAQICAUTitg28nCgBQOC2DRTklyg?cd=1"
model = "https://www.avito.ru/all/avtomobili/bmw/5_seriya-ASgBAQICAUTitg3UnCgBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/6_seriya_gran_coupe-ASgBAQICAUTitg2O8jIBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/7_seriya-ASgBAQICAUTitg2KnSgBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/i3-ASgBAQICAUTitg3YpygBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/i7-ASgBAQICAUTitg2I~aoQAUDgtg0U5Jco?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/i8-ASgBAQICAUTitg3epygBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/x1-ASgBAQICAUTitg2utCgBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/x2-ASgBAQICAUTitg2wtCgBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/x3-ASgBAQICAUTitg2ytCgBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/x5-ASgBAQICAUTitg22tCgBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/x5_m-ASgBAQICAUTitg26tCgBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/x6-ASgBAQICAUTitg2~tCgBQOC2DRTklyg?cd=1"
# model = "https://www.avito.ru/all/avtomobili/bmw/x7-ASgBAQICAUTitg3EtCgBQOC2DRTklyg?cd=1"



# try:
#     obj = ParserLinks()
#     obj.parse_links(model)
# except Exception as error:
#     print(error)
#     time.sleep(60)

obj = ParserLinks()
obj.parse_links(model)