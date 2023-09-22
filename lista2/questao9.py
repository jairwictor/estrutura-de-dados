# 9. Crie uma classe chamada triangulo com atributos lado1, lado2 e lado3.
#implemente um método chamado “calcular_perimetro” que retorna o perímetro do triângulo.

class Triangulo:
    def calcular_perimetro(self, lado1, lado2, lado3):
        perimetro = lado1 + lado2 + lado3
        print(f"O Perimetro do triangulo é de: {perimetro}")
        return perimetro
    
triangulo1 = Triangulo()
triangulo1.calcular_perimetro(11,10,9)