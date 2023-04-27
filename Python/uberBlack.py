from car import Car

class UberBlack(Car):
    typeCarAccepted = []
    seatsMaterial = []
    
    def __init__ (self, license, driver, passegenger, typeCarAccepted, seatsMaterial):
        super(). __init__(license, driver, passegenger)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial