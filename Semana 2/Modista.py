class Modista:
    
    def __init__(self, telaEnMetros):
        self.__telaEnMetros = telaEnMetros
        
    def getTelaEnMetros(self):
        return self.__telaEnMetros
        
    def telaMetrosAPulgadas(self):
        metrosAPulgadas = self.__telaEnMetros / 0.0254
        return metrosAPulgadas