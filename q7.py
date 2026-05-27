n = int(input("Digite um número inteiro: "))

def contar_digitos(n):
    contador = 0

    if (n == 0):
        return 1

    while (n > 0):
        n = n // 10
        contador += 1

    return contador

resultado = contar_digitos(n)

print("Quantidade de dígitos:", resultado)