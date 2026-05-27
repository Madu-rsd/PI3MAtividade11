palavra = input("Digite uma palavra: ")

def verificar_palindromo(palavra):
    if (palavra == palavra[::-1]):
        return True
    else:
        return False

resultado = verificar_palindromo(palavra)

print("Resultado:", resultado)

