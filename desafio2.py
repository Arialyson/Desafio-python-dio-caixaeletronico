class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo=0):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def ver_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = {}

    def criar_conta(self, titular, numero_conta):
        if numero_conta in self.contas:
            print("Número de conta já existe!")
        else:
            conta = ContaBancaria(titular, numero_conta)
            self.contas[numero_conta] = conta
            print(f"Conta criada com sucesso para {titular}!")

    def acessar_conta(self, numero_conta):
        conta = self.contas.get(numero_conta)
        if conta:
            return conta
        else:
            print("Conta não encontrada.")
            return None


# -----------------------------
#   SISTEMA PRINCIPAL
# -----------------------------
banco = Banco("Banco Python")

while True:
    print("\n===== SISTEMA BANCÁRIO =====")
    print("1 - Criar conta")
    print("2 - Acessar conta")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do titular: ")
        numero = input("Número da conta: ")
        banco.criar_conta(nome, numero)

    elif opcao == "2":
        numero = input("Número da conta: ")
        conta = banco.acessar_conta(numero)

        if conta:
            while True:
                print("\n--- Menu da Conta ---")
                print("1 - Ver saldo")
                print("2 - Depositar")
                print("3 - Sacar")
                print("4 - Voltar")

                op = input("Escolha: ")

                if op == "1":
                    conta.ver_saldo()
                elif op == "2":
                    valor = float(input("Valor do depósito: R$ "))
                    conta.depositar(valor)
                elif op == "3":
                    valor = float(input("Valor do saque: R$ "))
                    conta.sacar(valor)
                elif op == "4":
                    break
                else:
                    print("Opção inválida!")

    elif opcao == "3":
        print("Saindo... Obrigado por usar o Banco Python!")
        break

    else:
        print("Opção inválida. Tente novamente.")
