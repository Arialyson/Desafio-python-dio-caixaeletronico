import os
import platform

def limpar_tela():
    """Limpa o console (funciona em Windows, Linux e macOS)."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def menu():
    print('''
          === ARIBANK ===
          [1] Depositar
          [2] Sacar
          [3] Extrato
          [4] Sair
          ===============
          ''')

saldo = 0
limite= 500
extrato = ""
numero_de_depositos = 0
numero_de_saques = 0
Limite_de_saques = 3

while True:
    limpar_tela()
    menu()
    opcao = int(input("Digite uma opção: "))
    match opcao:
        case 1:
            deposito = float(input("Valor a ser depositado R$"))
            saldo += deposito
            numero_de_depositos += 1
            print(f"\u2714 Você depositou R${deposito:.2f}")
            print()
            input('Pressione ENTER para continuar...')
        case 2:
            saque = float(input("Quanto quer sacar? R$"))
            saldo -= saque
            numero_de_saques += 1
            print(f"\u2714 Você sacou R${saque:.2f}")
            print()
            input('Pressione ENTER para continuar...')
        case 3:
            print("=====EXTRATO=====")
            print()
            print(f"Seu saldo é de R${saldo:.2f}")
            print()
            print(f"Você fez {numero_de_depositos} Depositos")
            print(f"você fez {numero_de_saques} saques")
            print()
            print("=================")
            input('pressione ENTER para continuar...')
        case 4:
            print("Obrigado por usar nosso caixa!")
            print("Até mais")
            break