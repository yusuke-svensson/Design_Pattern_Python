import abc

class Banner:
    string=None
    def __init__(self,string):
        self.string=string
    def showWithParen(self):
        print("("+self.string+")")
    def showWithAster(self):
        print("*"+self.string+"*")

class Print():
    @abc.abstractclassmethod
    def printWeak(self) ->None:
        pass
    def printStrong(self) ->None:
        pass

class PrintBanner(Print):
    banner=[]
    def __init__(self,string):
        self.banner=Banner(string)        
    def printWeak(self):
        self.banner.showWithParen()
    def printStrong(self):
        self.banner.showWithAster()
        
if __name__ =="__main__":
    p=PrintBanner("Hello World")
    p.printWeak()
    p.printStrong()