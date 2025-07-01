import random

tabuleiro = [[" " for _ in range(5)] for _ in range(5)]
barcos = [(1, 1), (3, 4), (4, 0)]  # posições dos barcos

def mostrar_tabuleiro():
    for linha in tabuleiro:
        print(" ".join(linha))

def jogar():
    print("Batalha Naval - tabuleiro 5x5")
    while True:
        mostrar_tabuleiro()
        tentativa = input("Digite linha e coluna para atacar (ex: 1 2): ")
        linha, col = map(int, tentativa.split())
        if (linha, col) in barcos:
            print("Acertou o barco!")
            barcos.remove((linha, col))
            tabuleiro[linha][col] = "X"
            if not barcos:
                print("Todos os barcos foram afundados! Você ganhou!")
                break
        else:
            print("Errou!")
            tabuleiro[linha][col] = "O"

if __name__ == "__main__":
    jogar()