from account import Account\

class Car:
    id = int
    license = str
    driver = "",""
    passegenger = int
    
    
    #Declarando un metodo con sus respectivos objetos
    def __init__(self, license, driver, passegenger):
        self.license = license
        self.driver = driver
        self.passegenger = passegenger