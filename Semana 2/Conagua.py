class Conagua:
    
    def __init__(self, precioMetroCubico):
        self.__precioMetroCubico = precioMetroCubico
        
    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, precio):
        self.__precio = precio
    
    def pagoConsumoDeAgua(self, alto, largo, ancho):
        volumen = alto * largo * ancho
        pago = volumen * self.__precioMetroCubico
        return pago
        