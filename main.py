menu = """
==== Menu ====
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==============

Operação desejada: 
  """
saldo = 0
limite_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    # Depósito
    if opcao.lower() == "d":
        deposito = float(input("Valor para depósito: "))
        if(deposito <= 0):
            print("Não é possível fazer um depósito desse valor.")
        else:
            saldo += deposito
            print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso.")
            extrato.append(["Depósito", deposito])
        
    # Saque
    elif opcao.lower() == "s":
        if(numero_saques == LIMITE_SAQUES):
            print("Limite de saque atingido.")
        else:
            saque = float(input("Valor para saque: "))
            if (saque > limite_saque or saque < 0):
                print("Não é possível fazer um saque desse valor.")
            else:
                if(saque > saldo):
                    print("Saldo insuficiente.")
                else:
                    saldo -= saque
                    numero_saques += 1
                    print(f"Saque de R$ {saque:.2f} efetuado com sucesso.")
                    extrato.append(["Saque", saque])

    # Extrato
    elif opcao.lower() == "e":
        print("\n======= EXTRATO =======")
        if (extrato):
            for i in range(len(extrato)):    
                print(f"Operação {i+1}")
                print(f"Tipo: {extrato[i][0]}")
                print(f"Valor: R$ {extrato[i][1]:.2f}\n")
        else:
            print("Não foram realizadas movimentações")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=======================")

    # Sair
    elif opcao.lower() == "q":
        print("Obrigado e volte sempre!")
        break

    # Operação inválida
    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")