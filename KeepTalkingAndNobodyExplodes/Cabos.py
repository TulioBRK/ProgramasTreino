def perguntaserial():
    inputserial = input("Digite o ultimo número do serial da bomba: ")
    try:
        return int(inputserial)
    except ValueError:
        print("Digite um Número inteiro")
    return perguntaserial()


def perguntacabos():
    inputcabos = input("Digite a quantidade de cabos: ")
    try:
        return int(inputcabos)
    except ValueError:
        print("Digite um Número inteiro!")
    return perguntacabos()


def padronizador(listacabos):
    for cabo in listacabos:
        cabos.append(cabo.lower())


def seletordefios(quantidade):
    cabonumero = 1
    testestr = 0
    while cabonumero <= quantidade:
        try:
            lista.append(input("Digite a cor do cabo número {}: ".format(cabonumero)))
            cabonumero += 1
            testestr += 1
        except TypeError as erro:
            print("Insira um str!!: {}".format(erro))
            return seletordefios(quantidade)
        if lista.count("vermelho") == 0 and lista.count("azul") == 0 \
                and lista.count("preto") == 0 and lista.count("branco") == 0 \
                and lista.count("amarelo") == 0:
            lista.pop(0)
            print("Digite cores validas : vermelho,azul,preto,branco,amarelo")
            return seletordefios(quantidade)


QuantidadeCabos = perguntacabos()
while QuantidadeCabos < 3 or QuantidadeCabos > 6:
    print("Digite um valor entre 3 e 6")
    QuantidadeCabos = perguntacabos()

serial = perguntaserial()
if serial % 2 != 0:
    serial = "impar"
else:
    serial = "par"

lista = []
cabos = []
if QuantidadeCabos == 3:
    seletordefios(QuantidadeCabos)
    padronizador(lista)
    if "vermelho" not in cabos:
        print("Corte o segundo cabo")
    elif "branco" in cabos[-1]:
        print("Corte o último cabo.")
    elif cabos.count("azul") >= 2:
        print("Corte o último cabo azul")
    else:
        print("Corte o último cabo")
elif QuantidadeCabos == 4:
    seletordefios(QuantidadeCabos)
    padronizador(lista)
    if cabos.count("vermelho") >= 2 and serial == "impar":
        print("Corte o último cabo vermelho")
    elif cabos[-1] == "amarelo" and cabos.count("vermelho") == 0:
        print("Corte o primeiro cabo")
    elif cabos.count("azul") == 1:
        print("Corte o primeiro cabo")
    elif cabos.count("amarelo") >= 2:
        print("Corte o último cabo")
    else:
        print("Corte o segundo cabo")
elif QuantidadeCabos == 5:
    seletordefios(QuantidadeCabos)
    padronizador(lista)
    if cabos[-1] == "preto" and serial == "impar":
        print("Corte o quarto cabo")
    elif cabos.count("vermelho") == 1 and cabos.count("amarelo") >= 2:
        print("Corte o primeiro cabo")
    elif cabos.count("preto") == 0:
        print("Corte o segundo cabo")
    else:
        print("Corte o primeiro cabo")
elif QuantidadeCabos == 6:
    seletordefios(QuantidadeCabos)
    padronizador(lista)
    if cabos.count("amarelo") == 0 and serial == "impar":
        print("Corte o terceiro cabo")
    elif cabos.count("amarelo") == 1 and cabos.count("branco") >= 2:
        print("Corte o quarto cabo")
    elif cabos.count("vermelho") == 0:
        print("Corte o último cabo")
    else:
        print("Corte o quarto cabo")
else:
    print("Digite uma quantidade valida de cabos")
