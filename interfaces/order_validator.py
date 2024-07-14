from abc import ABC, abstractmethod
from model.order import Order

class OrderValidator(ABC):
    @abstractmethod
    def validate(self, order: Order):
        pass