N: int
N = int(input("Por favor, digite o tamanho do vetor: "))
vetor: [int] = [0 for x in range(N)]

for i in range(0, N):
    vetor[i] = int(input(f"Digite o {i+1}º elemento: "))


for i in range(0, N):
    print("Elemento", i+1, ":", vetor[i])
