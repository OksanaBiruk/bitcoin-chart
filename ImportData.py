from abc import ABC
from abc import abstractmethod


class ImportData(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_data(self, start_time, end_time):
        pass
