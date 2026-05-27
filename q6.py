n = int(input("Digite um número inteiro: "))

def contar_divisiveis_por_5 (n):
    contador = 0
    for x in range(1, n+1):
        if (x % 5 == 0): 
            contador += 1
    return contador

resultado = contar_divisiveis_por_5(n)
print("A quantidade de números divisíveis é:", resultado)