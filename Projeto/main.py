import os
print("Bem-vindo ao Caixa Eletrônico!\n")

def login():
    while True:
            senha = "Brenda1234$"
            senha_usuario = input("Digite sua senha de acesso: ")

            if senha_usuario == senha:
                print("Acesso permitido!, seja bem vindo(a).\n")
                break
                
            else:
                print("Senha Incorreta, Tente novamente\n")
                continue

def menu():
    while True:
            print("Escolha uma opção: ")
            print("1 - Ver saldo ")
            print("2 - Depositar ")
            print("3 - Sacar ")
            print("4 - Sair")

            entrada = input('>> ')
            return entrada

def operacoes(entrada, saldo):
        if entrada == '1':
            os.system('cls')
            saldo
            print(f'Saldo - R$ {saldo:.2f}')
            
        elif entrada == '2':
            os.system('cls')
            try:
                deposito = float(input('Digite o valor a depositar: '))
                if deposito > 0:
                     print('Depósito realizado com sucesso.')
                     saldo += deposito
                elif deposito == 0:
                    print('Por favor digite um valor valido para deposito.')
                else:
                    print('Valor para deposito obrigatoriamente tem que ser positivo.')

            except ValueError:
                print('Valor inválido para deposito.')
                
        elif entrada == '3':
            os.system('cls')
            try:
                saque = float(input('Digite o valor a sacar: '))
                if saque >= 2 and saque <= saldo:
                    saldo -= saque
                    print('Saque realizado com sucesso. Aguarde as notas.')
                elif saque > saldo:
                    print("Saldo insuficiente.")
                elif saque < 2:
                    print("Saque somente acima de valores de R$ 2.00")

            except ValueError:
                print('Digite um valor valido para saque.')
    
        elif entrada == "4":
            os.system('cls')
            print("Obrigado por usar o Caixa Eletrônico!")
            return saldo, True
            

        else:
            print("Valor invalido, Valores permitidos [1 - Ver saldo],[2 - Depositar], [3 - Sacar], [4 - Sair] ")
            
        return saldo, False

saldo = 0.00
login()

sair = False
while not sair:
    entrada = menu()
    saldo, sair = operacoes(entrada, saldo)
    
