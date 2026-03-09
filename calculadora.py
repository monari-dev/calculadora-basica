def somar(a,b ):
   return a + b

def subtrair(a, b):
   return a - b

def multiplicar(a, b):
   return a * b 
   
def dividir(a, b):
   if b == 0: 
     return "Erro Identificado: Divisão por Zero!"
   return a / b

print("  -  -  -  Calculadora Simples  -  -  -  ")
print("1. Soma | 2. Subtração | 3. Multiplicação | 4. Divisão")

while True:
    escolha = input("Selecione uma Operação 1 | 2 | 3 | 4: ")
    if escolha in ['1', '2', '3', '4']:
        break
    else:
        print("Erro identificado, você está tentando escolher uma operação inexistente!")

num1 = float(input("Selecione o Primeiro Número:"))
num2 = float(input("Selecione o Segundo Número"))

if escolha =='1':
   print(f"Resultado:{somar(num1,num2)}")
elif escolha =='2':
    print(f"Resultado:{subtrair(num1,num2)}")
elif escolha =='3':
    print(f"Resultado: {multiplicar(num1,num2)}")
elif escolha =='4':
    print(f"Resultado: {dividir(num1,num2)}")