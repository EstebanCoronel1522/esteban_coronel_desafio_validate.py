#Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
"""def sumar_digitos (numero: int) -> int:
    if numero== 0:
        resultado= 0
    else:
        resultado= numero % 10 + sumar_digitos (numero // 10)
    return resultado
print (sumar_digitos(123))"""

#Realizar una función para calcular el número de Fibonacci de un número ingresado por consola

def numero_fibonacci (numero:int)-> int:
    
    if numero < 2:
        return numero
    return numero_fibonacci  (numero -1) + numero_fibonacci (numero - 2)

def suma_fibonacci(numero: int) -> int:
    suma = 0
    for i in range(numero + 1):
        suma += numero_fibonacci(i)
    return suma
       
print(suma_fibonacci(6))



"""def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
"""

        