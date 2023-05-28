from abc import ABC, abstractmethod


class LinksParserInterface(ABC):

    @abstractmethod
    def parse_links(self, link: str):
        '''
        :param link: ссылка на страницу с объявлениями, с которой парсятся ссылки на объявления
        '''
        ...
