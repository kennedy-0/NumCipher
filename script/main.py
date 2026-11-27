import sys
#sistema simpre de criptografia

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
"o": "12",
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

traducao = {v: k for k,v in dicionario.items()}

def menu():
        print("""[1] falar
[2] Traduzir
[3] Sair
""")


def fala():
        msg = input("Digite sua mensagem: "). lower()
        resultado = ""
        for letra in msg:
                resultado += dicionario.get(letra, letra)
        print(resultado)


def traduzir():
    trz = input("Tradução da msg: ")
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

    print("Mensagem:", resultado1)

def exit():
        sys.exit()
while True:
        menu()
        opcao = int(input("O que você quer fazer: "))

        if opcao == 1:
                fala()
        elif opcao == 2:
                traduzir()
        elif opcao ==3:
                exit()
