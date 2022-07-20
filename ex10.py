#

def somar(valor1, valor2):
  return (valor1 * valor2)

class Somar:
  def __init__(self, val1 = None, val2 = None):
    self.valor1 = val1
    self.valor2 = val2    
  def somar(self):
    return (self.valor1 + self.valor2)


val1 = int(input("informe o valor 1: "))
val2 = int(input("informe o valor 2: "))
print(somar(val1, val2))

s1 = Somar()
s1.valor1 = int(input("informe 1: "))
s1.valor2 = int(input("informe 2: "))
print(s1.somar())
