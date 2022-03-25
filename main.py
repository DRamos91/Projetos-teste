a: int
b: int
c: int
D: int

print("Calculo de equação segundo grau")

a = int(input("Digite valor de a: "))
if a == 0:
    print("valor de a tem que ser diferente de 0");
    quit()


b = int(input("Digite valor de b: "))
c = int(input("Digite valor de c: "))
D = ((b**2)-(4*a*c))

resultado = (-1*(b+(D**0.5))/(2*a))
resultado1 = (-1*(b-(D**0.5))/(2*a))

print("x1: " , resultado1)
print("x2: " , resultado)
