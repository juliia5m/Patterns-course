# from abc import ABCMeta

from abc import ABC, abstractmethod


class Transport(ABC):

    def __init__(self, cost, cost_of_usage):
        self.cost = cost
        self.cost_of_usage = cost_of_usage

    def get_cost(self):
        return self.cost

    def get_cost_of_usage(self):
        return self.cost_of_usage
