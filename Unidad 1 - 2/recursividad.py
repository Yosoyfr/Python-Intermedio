# Funcion recursiva sin retorno
def cuentaRegresiva(num):
    if num > 0:
        print(num)
        num -= 1
        cuentaRegresiva(num)
    else:
        print("***FIN DE LA FUNCION***", num)

    print("*"*num)
    print("hoLA")


cuentaRegresiva(3)

# Funcion recursiva con retorno


def factorial(num):
    #print("Valor inicial ->", num)
    if num > 1:
        num *= factorial(num-1)
    if num == 0:
        num = 1
    #print("Valor final ->", num)
    return num


myFactorial = factorial(-5)
#print("El factorial es:", myFactorial)
