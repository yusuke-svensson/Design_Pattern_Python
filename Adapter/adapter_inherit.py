import abc

class Banner:
    string=None
    def __init__(self,string):
        self.string=string
    def showWithParen(self):
        print("("+self.string+")")
    def showWithAster(self):
        print("*"+self.string+"*")

class Print(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def printWeak(self) ->None:
        pass
    def printStrong(self) ->None:
        pass

class PrintBanner(Banner,Print):
    def __init__(self,string):
        super().__init__(string)
    def printWeak(self):
        self.showWithParen()
    def printStrong(self):
        self.showWithAster()
        
if __name__ =="__main__":
    p=PrintBanner("Hello World")
    p.printWeak()
    p.printStrong()
