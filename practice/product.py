class productclass:
    """
        __init__work as a constructor
        it automatically call when object of class create
    """
    
    def __init__(self):
        print("welcome to product panel")
        self.mobile=50000
        self.__laptop=45000         #self.__laptop(private it will not chng price of laptop)

    def display(self):
        print(self.mobile)
        print(self.__laptop)

    def updateprice(self,newlaptopprice):
        self.__laptop=newlaptopprice