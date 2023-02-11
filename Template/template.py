import abc

class AbstractDisplay(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def display(self):
        pass

class StarDisplay(AbstractDisplay):
    def __init__(self):
        super().__init__()
    
    def display(self,text):
        print("*"*3+text+"*"*3)

class minusDisplay(AbstractDisplay):
    def __init__(self):
        super().__init__()
    
    def display(self,text):
        print("-"*3+text+"-"*3)
    

if __name__=='__main__':
    m=StarDisplay()
    m.display("hello")