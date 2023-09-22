# crie uma classe chamada retangulo que tenha atributos de base e altura.
#implemente um metodo chamado de calcular_area que retorna a area do retangulo.
class retangulo():

    def __init__(self,altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self, altura, base):
        area= (altura * base)
        print("A area do retângulo é: ", area)

retangulo1 = retangulo(12,30)
retangulo1.calcular_area(12, 30)
    
