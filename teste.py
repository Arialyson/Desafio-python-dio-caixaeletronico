import os
import platform

def limpar_tela():
    """Limpa o console (funciona em Windows, Linux e macOS)."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def menu():
    """Exibe o menu de opções."""
    print('''
    ========= MENU =========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    ========================
    ''')

# ... Variáveis Iniciais ...
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
contador_depositos = 0
contador_saques = 0

while True:
    limpar_tela()  # <--- LIMPA A TELA ANTES DE EXIBIR O MENU
    menu()
    
    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("\n❌ Operação inválida! Por favor, digite o número da opção desejada.")
        input("Pressione Enter para continuar...")
        continue

    # Limpa a tela antes de mostrar o resultado da operação
    limpar_tela()

    match opcao:
        
        case 1:
            try:
                deposito = float(input("Valor a ser depositado R$: "))
            # ... resto da lógica de depósito ...
            # ... (código omitido por brevidade, mas você manteria a lógica anterior)
                if deposito > 0:
                    saldo += deposito
                    extrato += f"Depósito: R$ {deposito:.2f}\n"
                    contador_depositos += 1
                    print(f"\n✅ Depósito de R$ **{deposito:.2f}** realizado com sucesso!")
                else:
                    print("\n❌ Operação falhou! O valor do depósito deve ser positivo.")

            except ValueError:
                print("\n❌ Operação falhou! Valor informado é inválido.")
        
        case 2:
            # ... lógica de saque ...
            try:
                saque = float(input("Quanto quer sacar? R$: "))
                
                excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES
                excedeu_limite = saque > limite
                excedeu_saldo = saque > saldo
                
                if excedeu_saldo:
                    print("\n❌ Operação falhou! Você não tem saldo suficiente.")
                elif excedeu_limite:
                    print(f"\n❌ Operação falhou! O valor máximo de saque é de R$ **{limite:.2f}**.")
                elif excedeu_saques:
                    print(f"\n❌ Operação falhou! Limite diário de **{LIMITE_DE_SAQUES}** saques excedido.")
                elif saque > 0:
                    saldo -= saque
                    extrato += f"Saque:    R$ -{saque:.2f}\n"
                    numero_de_saques += 1 
                    contador_saques += 1 
                    print(f"\n✅ Saque de R$ **{saque:.2f}** realizado com sucesso!")
                else:
                    print("\n❌ Operação falhou! O valor do saque deve ser positivo.")
            except ValueError:
                print("\n❌ Operação falhou! Valor informado é inválido.")

        case 3:
            print("\n================ EXTRATO ================")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                print(extrato)
            
            print(f"Saldo atual: R$ **{saldo:.2f}**")
            saques_restantes = LIMITE_DE_SAQUES - numero_de_saques
            print("--- Contagem de Operações ---")
            print(f"Total de depósitos realizados: **{contador_depositos}**")
            print(f"Total de saques realizados: **{contador_saques}**")
            print("-----------------------------")
            print(f"Saques realizados hoje (limite): **{numero_de_saques}**")
            print(f"Saques restantes hoje: **{saques_restantes}**")
            print("=========================================")

        case 4:
            print("\n👋 Obrigado por usar nosso sistema! Encerrando...")
            break

        case _:
            print("\n❌ Opção inválida! Por favor, selecione novamente a opção desejada.")

    if opcao != 4:
        # Pausa o programa após a operação para que o usuário possa ler o resultado
        input("\nPressione Enter para voltar ao menu...")