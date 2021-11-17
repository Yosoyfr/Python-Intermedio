# Funcion recursiva sin retorno - Funcion Vacia
def cuentaRegresiva(inf, sup):
    if sup > inf:
        print(sup)
        sup -= 1
        cuentaRegresiva(inf, sup)  # Algo pendiente
    else:
        print("***FIN DE LA CUENTA REGRESIVA***", sup)
    # Realizacion de lo pendiente
    print('*'*sup)


# cuentaRegresiva(0, 5)


# Funcion recursiva con retorno - Funcion normal
def factorial(num) -> int:
    # print('Valor inicial ->', num)
    if num > 1:
        num *= factorial(num-1)  # Pendiente
    if num == 0:
        num = 1
    # Vuelvo y recupero lo pendiente
    return num


mi_factorial = factorial(10)
if mi_factorial < 0:
    print('No tiene factorial')
else:
    print("El factorial es:", mi_factorial)
