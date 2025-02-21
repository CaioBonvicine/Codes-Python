nome: str
idade: int
salario: float
saque: float
deposito: float
tempo: int
rep: str

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
tempo = int(input("Digite o tempo de cadastro nesse banco (em meses): "))

deposito = salario * tempo

while True:
    saque = float(input("Digite o valor que deseja sacar: "))
    if saque <= deposito:
        print("Saque realizado com sucesso!")
        deposito -= saque
        print(f"Saldo atual: R${deposito:.2f}")
    elif saque > deposito:
        print("Saldo insuficiente para realizar o saque.")
    else:
        print("Valor inválido.")
    print("Deseja continuar? (S/N)")
    rep = input()
    if rep == "S" or rep == "s":
        continue
    elif rep == "N" or rep == "n":
        break
    else:
        print("Opção inválida.")

print("Obrigado por utilizar nossos serviços!")
