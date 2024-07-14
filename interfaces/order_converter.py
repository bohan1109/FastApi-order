from abc import ABC, abstractmethod
from model.order import Order

class OrderConverter(ABC):
    @abstractmethod
    def convert(self, order: Order):
        pass