from abc import ABC, abstractmethod


class CollectionOfLinksInterface(ABC):

    @abstractmethod
    def sources_data(self, link):
        ...
        # todo поправить нейминг функции
