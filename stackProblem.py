import sys


class MinStack:

    def __init__(self):
        self.container = []
        self.currentNumber = sys.maxsize
        self.mins = []

    def push(self, val: int) -> None:
        if val != None:
            self.container.append(val)

        if val <= self.currentNumber:
            self.mins.append(val)
            self.currentNumber = val

    def pop(self) -> None:
        if self.container[-1] == self.currentNumber:
            self.mins.pop()
            self.currentNumber = self.mins[-1]
        self.container.pop(-1)

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return self.currentNumber







