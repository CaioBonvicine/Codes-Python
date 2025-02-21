L: int
C: int

L = int(input("Digite o numero de linhas: "))
C = int(input("Digite o numero de colunas: "))

mat: [str] = [[0 for x in range(C)] for x in range(L)]

for i in range(0, L):
    for j in range(0, C):
        mat[i][j] = input(f"Digite o nome da posicao {i},{j}: ")


print()
print("Matriz Gerada: ")
print()

for i in range(0, L):
    for j in range(0, C):
        print(f"{mat[i][j]}", end=" ")
    print()
