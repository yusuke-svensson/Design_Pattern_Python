import abc
class Component(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def __init__(self):
        pass
    def operation(self):
        print("Concrete")

        

class Decorator(Component):
    def __init__(self,component):
        self.component=component


class ConcreteDecorator(Decorator):
    def __init__(self,component):
        super().__init__(component)
    def operation(self):
        self.component.operation()
        print("Deco")


if __name__=="__main__":
    c=ConcreteDecorator(ConcreteComponent())
    c.operation()
