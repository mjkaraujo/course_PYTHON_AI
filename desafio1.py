
menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

"""

saldo = 0
limite = 500
extrato = ""
n_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == '0':
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não realizada! Valor inválido.")

    elif opcao == '1':
        valor = float(input("Digite o valor do saque: "))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = n_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print('Operação não realizada! Você não tem saldo suficiente.')

        elif limite_excedido:
            print('Operação não realizada! O valor do saque excedeu o limite.')

        elif saque_excedido:
            print('Operação não realizada! Quantidade de saques excedidos.')

        elif valor > 0:
            saldo -= valor
            extrato = f"Saque: R$ {valor:.2f}\n"
            n_saques += 1

        else:
            print("Operação não realizada! Valor inválido.")

    elif opcao == '2':
        print('\n============================= EXTRATO==========================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f2}')
        print('================================================================')

    elif opcao == '3':
        break

    else:
        print("Operação não realizada! Por favor selecione novamente a operação desejada.")
