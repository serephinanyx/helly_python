class RBIclass:
    def __init__(self):
        print("RATE OF INTEREST is :")
        self.ROI=10.6
    
    def RBI(self):
        print("RBI RATE OF INTEREST is:")
        self.ROI=11.5
   
    def SBI(self):
        print("SBI RATE OF INTEREST is:")
        self.__ROI=13.5

    def HDFC(self):
        print("HDFC RATE OF INTEREST is:")
        self.__ROI=15.5
    
    def display(self):
        print(self.ROI)
