import sys
import time
VERMELHO = "\033[31m"
VERDE = "\033[92m"
AMARELO = "\033[33m"
ROJO = "\033[91m"
RESET = "\033[0m"

dicionario ={
"a": "26",
"b": "25",
"c": "24",
"d": "23",
"e": "22",
"f": "21",
"g": "20",
"h": "19",
"i": "18",
"j": "17",
"k": "16",
"l": "15",
"m": "14",
"n": "13",
"o": "90",
"p": "11",
"q": "10",
"r": "9",
"s": "8",
"t": "7",
"u": "6",
"v": "5",
"w": "4",
"x": "3",
"y": "2",
"z": "1"
}

def load():
    progress_chars = [
        "[" + "#" * i + " " * (20 - i) + "]"
        for i in range(21)
    ]

    for i, progress in enumerate(progress_chars):
        porcento = int((i + 1) / len(progress_chars) * 100)
        sys.stdout.write(
            "\r" + VERMELHO + progress + f" {porcento}%"
        )
        sys.stdout.flush()
        time.sleep(0.1)

    print(RESET)


traducao = {v: k for k,v in dicionario.items()}

load()
def menu():
        print("""[1] falar
[2] Traduzir
[3] Sair
""")


def fala():
        msg = input(VERMELHO + "Digite sua mensagem: " + RESET). lower()
        resultado = ""
        for letra in msg:
                resultado += dicionario.get(letra, letra)
        time.sleep(1)
        print(VERDE+ resultado + RESET)


def traduzir():
    trz = input(VERMELHO + "Tradução da msg: " + RESET)
    resultado1 = ""
    i = 0

    while i < len(trz):
        if trz[i:i+2] in traducao:
            resultado1 += traducao[trz[i:i+2]]
            i += 2
        elif trz[i] in traducao:
            resultado1 += traducao[trz[i]]
            i += 1
        else:
            resultado1 += trz[i]
            i += 1
    time.sleep(1)
    print(VERDE + "Mensagem:", resultado1 + RESET)

def exit():
        print("Saindo ...")
        time.sleep(0.5)
        sys.exit()
while True:
        menu()
        opcao = int(input(AMARELO + "O que você quer fazer: " + RESET))

        if opcao == 1:
                fala()
        elif opcao == 2:
                traduzir()
        elif opcao ==3:
                exit()

