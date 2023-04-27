from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial = []
    
    def __init__(self, license, driver, passegenger, typeCarAccepted, seatsMaterial):
        super().__init__(license, driver, passegenger, typeCarAccepted, seatsMaterial)