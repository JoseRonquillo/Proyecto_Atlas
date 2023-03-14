max = 0
menor= 0

num1 = int(input("Agruegue el primer numero"))
num2 = int(input("Agruegue el segundo numero"))

if num1 < num2:
  max = num1
  menor = num2
else:
  max = num2
  menor = num1
  
  
 resultado = max / menor
print(resultado)
