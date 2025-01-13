import datetime
start_time = datetime.datetime.now()
def fibo_recursiva(numero):
    n=0
    a=0
    if numero<=1:
        return numero
    else:
        return fibo_recursiva(numero-1)+fibo_recursiva(numero-2)
numero=int(input("Dime un numero "))
fibo_recursiva(numero)
print (fibo_recursiva(numero))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)
