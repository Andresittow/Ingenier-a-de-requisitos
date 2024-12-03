class Conagua:
    
    def __init__(self, precioMetroCubico):
        self.__precioMetroCubico = precioMetroCubico
        
    def getPrecio(self):
        return self.__precio
    
    def setPrecioMetroCubico(self, precio):
        self.__precioMetroCubico = precioMetroCubico
    
    def pagoConsumoDeAgua(self, alto, largo, ancho):
        volumen = alto * largo * ancho
        pago = volumen * self.__precioMetroCubico
        return pago
        