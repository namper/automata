# Finite Determinstic State Machine
# from enum import Enum
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

SK = TypeVar('StateClass')


class State(ABC):
    """Abstract State Class """
    @abstractmethod
    def __next__(self) -> 'State':
        pass


class StateMachine(Generic[SK]):
    """ Abstract Implemantation Of State Machine,
    All State Machine Must Inherit From It """

    def __init__(self, feed: str) -> None:
        # self.state = SK.DEFAULT
        self.feed = feed

    def __call__(self):
        for char in self.feed:
            # do something
            pass

