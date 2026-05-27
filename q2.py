n = float(input("Digite o radicando: "))
x = float(input("Digite a ordem: "))

def raiz(n, x):
    return n ** (1/x)

resultado = raiz(n, x)
print("A raiz será:", resultado)