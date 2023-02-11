import random #importar o modulo random

word_list = ["adeus","baboino","camelo","maisie"] #criar uma lista de palavras de onde escolher

fases = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def jogar():
    palavra_escolhida = random.choice(word_list) #escolher uma palavra aleatória para começar o jogo
    tamanho_palavra = len(palavra_escolhida)
    palavra_impressa = []

    for _ in range(tamanho_palavra):
        palavra_impressa += "_"

    numero_de_vidas = 6

    fim_do_jogo = False
    
    print(f"{' '.join(palavra_impressa)}")
    
    while not fim_do_jogo:

        

        letra = input("Advinha a letra:").lower()

        if letra in palavra_impressa:
            print(f"A letra: {letra} já foi escolhida, tenta outra vez")

        for posicao in range(tamanho_palavra):
            letter = palavra_escolhida[posicao]
            if letter == letra:
                palavra_impressa[posicao] = letter
                
        print(f"{' '.join(palavra_impressa)}")

        if letra not in palavra_escolhida:
            print(f"A letra {letra} não está na palavra, perdeste 1 vida")
            numero_de_vidas -= 1
            if numero_de_vidas == 0:
                fim_do_jogo = True
                print("Perdeste :( " )

        if "_" not in palavra_impressa:
            fim_do_jogo = True
            print("Boa gordina!")

        print(fases[numero_de_vidas])
