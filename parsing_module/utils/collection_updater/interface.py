from abc import ABC, abstractmethod


class UpdaterInterface(ABC):

    @abstractmethod
    def update(self):
        ...

