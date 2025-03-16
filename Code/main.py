import locale as lo
lo.setlocale(lo.LC_ALL, 'pt_BR.UTF-8')

menu = """
====================

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

====================
"""

saldo = 0
limite = 500
extrato = [] #Mudei para guardar as operações em uma lista
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        print("Depósito\n")
        valor_deposito = float(input("Informe o valor do depósito: "))
        if valor_deposito >= 0:
            saldo += valor_deposito
            extrato.append({
                'Tipo': "Depósito",
                'Valor': valor_deposito,
                'Saldo': saldo
                })
            print (f"\nUm valor de {lo.currency(valor_deposito, grouping=True)} foi depósitado na sua conta, ficando com um total de {lo.currency(saldo, grouping=True)}")
        else:
            print(f"""\nO valor {lo.currency(valor_deposito, grouping=True)} não é válido!.""")
    
    elif opcao == "2":
        print("\nSaque")
        valor_saque = float(input("\nValor que você deseja sacar: "))
        if valor_saque <= limite and saldo >= valor_saque:
            if numero_saques < LIMITE_SAQUES:
                numero_saques+=1
                saldo -= valor_saque
                extrato.append({
                    'Tipo': 'Saque',
                    'Valor': valor_saque,
                    'Saldo': saldo
                })
                print(f'\nVocê sacou um total de {lo.currency(valor_saque, grouping=True)} e agora possui {lo.currency(saldo,grouping=True)} na conta!')
            else:
                print(f'''\nVocê excedeu seu limite de saque diário!\nVocê sacou {numero_saques} de {LIMITE_SAQUES} saques hoje.''')
    elif opcao == '3':
        print("==================Extrato==================")
        if not extrato:
            print('''Não foi realizado nenhum movimento na sua conta.''')
        else:
            for operacoes in extrato:
                print(f'\nTipo: {operacoes['Tipo']}')
                print(f'Valor: {lo.currency(operacoes['Valor'], grouping=True)}')
            print(f'\nSaldo atual: {lo.currency(operacoes['Saldo'], grouping=True)}')
        print("===========================================")
    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("\nOpção inválida")