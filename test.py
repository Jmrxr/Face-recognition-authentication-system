# Programa que sume, reste, multiplique y divida dos números ingresados por el usuario.

def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b

print("Operaciones matemáticas")
print("Digite el primer número")
a = int(input())
print("Digite el segundo número")
b = int(input())
print("Suma:", sumar(a, b))
print("Resta:", restar(a, b))
print("Multiplicación:", multiplicar(a, b))
print("División:", dividir(a, b))   