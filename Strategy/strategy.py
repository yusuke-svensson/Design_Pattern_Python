import abc

class Strategy(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        pass
    @abc.abstractclassmethod
    def execute(self):
        pass


class ConcreteStrategy_1(Strategy):
    def __init__(self):
        super().__init__()
    def execute(self):
        print("Called_0")

class ConcreteStrategy_2(Strategy):
    def __init__(self):
        super().__init__()
    def execute(self):
        print("Called_1")

class Context():
    def __init__(self):
        self.__strategy=None
        pass
    def setStrategy(self,strategy):
        self.__strategy=strategy

    def dosomething(self):
        self.__strategy.execute()

if __name__=='__main__':
    c=Context()
    algorithms=[ConcreteStrategy_1(),ConcreteStrategy_2()]
    for al in algorithms:
        c.setStrategy(al)
        c.dosomething()
