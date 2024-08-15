class Conagua:
    
    def __init__(self, precio):
        self.__precio = precio
        
    def getPrecioMetroCubico(self):
        return self.__precio
    
    def setPrecioMetroCubivo(self, precio):
        self.__precio = precio
    
    def pagoConsumoDeAgua(self, alto, largo, ancho):
        volumen = alto * largo * ancho
        pago = volumen * self.__precio
        return pago
        