class Valores:
    
    def __init__(self, valor1, valor2):
        self.__valor1 = valor1
        self.__valor2 = valor2
        
    def determinarMayorValor(self):
        if self.__valor1 > self.__valor2:
            return self.__valor1
        elif self.__valor1 < self.__valor2:
            return self.__valor2
        else:
            return None        