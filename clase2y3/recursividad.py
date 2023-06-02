# Funcion recursiva sin retorno - Funcion Vacia
def cuentaRegresiva(inf, sup):
    if sup > inf:
        print(sup)
        sup -= 1
        cuentaRegresiva(inf, sup)  # Recursividad
    else:
        print("***FIN DE LA CUENTA REGRESIVA ***", sup)


# cuentaRegresiva(0, 5)


# Funcion recursiva con retorno - Funcion normal
def factorial(num) -> int:
    print("Valor inicial (num)->", num)
    # 1 - 1*2 - 1*2*3 - 1*2*3*4 - 1*2*3*4*5
    if num > 1:
        num *= factorial(num-1)  # Lo pendiente
    elif num == 0:
        num = 1

    # Vuelvo y recupero lo pendiente
    return num


mi_factorial = factorial(5)

print(mi_factorial)
