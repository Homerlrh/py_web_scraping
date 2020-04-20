from abc import ABCMeta, abstractmethod


class Connect(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        return "%s connected"

    @abstractmethod
    def get_top_stories(self):
        pass

    @abstractmethod
    def get_link_only(self):
        pass

    @abstractmethod
    def get_search_title(self):
        pass
