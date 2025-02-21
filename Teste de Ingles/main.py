print("Vamos ver se o seu inglês está em dia! (Obs: todas as respostas devem ser escritas em minúsculo)")
acertos: int = 0
erros: int = 0
print("Qual é a tradução da palavra 'cachorro' em inglês?")
resposta: str = input()
if resposta == "dog":
    print("Correto!")
    acertos += 1
else:
    print("Errado! A resposta correta é 'dog'.")
    erros += 1

print("Qual é a tradução da frase 'tema o urso' em inglês?")
resposta2: str = input()
if resposta2 == "fear the bear":
    print("Correto!")
    acertos += 1
else:
    print("Errado! A resposta correta é 'fear the bear'.")
    erros += 1

print("Qual é a tradução da frase 'Lutar contra você' em inglês?")
resposta3: str = input()
if resposta3 == "fight against you":
    print("Correto!")
    acertos += 1
else:
    print("Errado! A resposta correta é 'fight against you'.")
    erros += 1

print("Qual é a tradução da palavra 'ornitorrinco' em inglês?")
resposta4: str = input()
if resposta4 == "platypus":
    print("Correto!")
    acertos += 1
else:
    print("Errado! A resposta correta é 'platypus'.")
    erros += 1

print("Qual é a tradução da frase 'Você é o melhor' em inglês?")
resposta5: str = input()
if resposta5 == "you are the best":
    print("Correto!")
    acertos += 1
else:
    print("Errado! A resposta correta é 'you are the best'.")
    erros += 1

if acertos > erros:
    print("Parabéns! Você passou!")
else:
    print("Você não passou! Estude mais!")
