print("Digite os nome dos passageiros e o codigos dos aeroportos das cidades")
print("Os codigos são: FCO, LIS, MAD, CDG, DUB, BRU, LHR")
nome1 = input("Primeiro nome: ")
nome2 = input("Segundo nome: ")
nome3 = input("Terceiro nome: ")
nome4 = input("Quarto nome: ")
nome5 = input("Quinto nome: ")
nome6 = input("Sexto nome: ")
codigo1 = input("Primeiro codigo: ")
codigo2 = input("Segundo codigo: ")
codigo3 = input("Terceiro codigo: ")
codigo4 = input("Quarto codigo: ")
codigo5 = input("Quinto codigo: ")
codigo6 = input("Sexto codigo: ")


viagems = [(nome1, codigo1),
           (nome2, codigo2),
           (nome3, codigo3),
           (nome4, codigo4),
           (nome5, codigo5),
           (nome6, codigo6)]

destino = input("Digite o codigo do destino: ")


def ler_arquivo_voos(caminho_arquivo):
    # Lê o arquivo de voos e retorna um dicionário com os dados.
    voos = {}
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                origem, destino, saida, chegada, preco = linha.strip().split(",")
                voos.setdefault((origem, destino), [])
                voos[(origem, destino)].append((saida, chegada, int(preco)))
        return voos
    except FileNotFoundError:
        print("Erro: arquivo de dados não encontrado.")
        return None


def saida_voos(voos):
    # saída dos dados dos voos para melhor visualização.
    if voos:
        for (origem, destino), lista_voos in voos.items():
            print(f"Voos de {origem} para {destino}:")
            for saida, chegada, preco in lista_voos:
                print(
                    f"  Saída: {saida}, Chegada: {chegada}, Preço: R${preco:.2f}")


def imprimir_voos(agenda):
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        nome = viagems[i][0]
        origem = viagems[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                    volta[0], volta[1], volta[2]))
    print('Preço total: ', total_preco)


caminho_arquivo = r"C:\Codes-Python\CalendarioDeVooAdpatado\flights.txt"

voos = ler_arquivo_voos(caminho_arquivo)

print("Gostaria de ver as viagems disponiveis?")
resposta = input("(S) OU (N)")
if resposta == "S":
    saida_voos(voos)


vetor: int = [0 for x in range(12)]
for i in range(12):
    vetor[i] = int(input(
        "Digite qual das viagems disponiveis vc deseja (digite 2(ida e volta) para cada pessoa): "))

agenda = [vetor[0], vetor[1], vetor[2], vetor[3], vetor[4], vetor[5],
          vetor[6], vetor[7], vetor[8], vetor[9], vetor[10], vetor[11]]
imprimir_voos(agenda)
