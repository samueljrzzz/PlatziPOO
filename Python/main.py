from car import Car #De el archivo car importar la clase Car
from account import Account
from uberX import UberX

if __name__ == "__main__": #Script para ejecutar aqui mismo
    '''
    car = Car("ADS838", Account(10, "Samuel Jrz", "INE", "@gmail", 1234), 3)
    print(vars(car)) #sirve para imprimer la clase en forma de diccionarios en lista
    print(vars(car.driver))
    '''
    
    uberX = UberX("AMQ123", Account("Andres Herrera", "AND123", "INE", "@", "123"), 3, "Nissan", "2014")
