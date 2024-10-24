import random
import string

def gerar_senha(comprimento, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiais=True):
    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += string.punctuation

    if not caracteres:
        print("Erro: Nenhum conjunto de caracteres selecionado.")
        return None

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas!")

    comprimento = int(input("Digite o comprimento da senha desejada: "))
    incluir_maiusculas = input("Incluir letras maiúsculas? (S/N): ").lower() == 's'
    incluir_minusculas = input("Incluir letras minúsculas? (S/N): ").lower() == 's'
    incluir_numeros = input("Incluir números? (S/N): ").lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (S/N): ").lower() == 's'

    senha = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)

    if senha:
        print(f"\nSua senha gerada: {senha}")
    else:
        print("Nenhuma senha gerada. Por favor, escolha pelo menos um conjunto de caracteres.")

if __name__ == "__main__":
    main()
        
