from car import Car

class UberX(Car):
    brand = str
    model = str
    
    def __init__(self, license, driver, passegenger, brand, model):
        super().__init__(license, driver, passegenger)
        self.brand = brand
        self.model = model
    