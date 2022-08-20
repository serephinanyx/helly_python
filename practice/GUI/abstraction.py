from abc import ABC , abstractmethod
#ABC : Abstrac Base CLass

"""
abstractmethod: which contain only method declaration - no body

this kind of method does not contain method defination

"""

class RBI(ABC):
    @abstractmethod
    def roi(self):
        pass

class SBI(RBI):
    def roi(self):
        print("6.5")

class HDFC(RBI):
    def roi(self):
        print("7.5")

sbi=SBI()
hdfc=HDFC()

sbi.roi()
hdfc.roi()