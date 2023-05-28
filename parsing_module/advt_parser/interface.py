from abc import ABC, abstractmethod


class AdsParserInterface(ABC):

    @abstractmethod
    def parse(self, request_link: str):
        ...


