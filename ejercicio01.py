#Escribir dos funciones, una función que reciba un número entero positivo n y calcule el número de fibonacci asociado a ese número de manera recursiva y otra función que haga la misma operación pero con bucles.
import datetime
start_time = datetime.datetime.now()
def fibo_recursiva(numero):
    a, b = 0, 1
    for i in range(numero):
        a, b = b, a + b
    print (a)
numero=int(input("Dime un numero "))
fibo_recursiva(numero)
end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)