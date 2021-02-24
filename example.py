from Automata.state_machine import State
from enum import Enum


class Nothing(State):
    def __next__(self):
        return self


class Branch(Enum):
    Default = Nothing()

    def __next__(self,):
        return next(self.value)


print(Branch.Default)

print(next(Branch.Default))
