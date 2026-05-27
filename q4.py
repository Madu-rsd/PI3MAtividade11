n = int(input("Digite um número inteiro: "))

def numero_perfeito(n):
    soma = 0

    for i in range(1, n):
        if (n % i == 0):
            soma += i

    if (soma == n):
        return True
    else:
        return False

resultado = numero_perfeito(n)

if (resultado):
    print("O número é perfeito!")
else:
    print("O número não é perfeito!")