#!/usr/local/bin/python3


def entrada_usuario():
    # input do usuário com a base, logaritimando e as casas decimais do resultado
    controle_logaritimando = False
    while controle_logaritimando == False:
        logaritimando = float(input("Qual é o logaritimando? "))
        if condição_logaritimando(logaritimando):
            controle_logaritimando = True
        else:
            print("O logaritimando deve ser maior do que 0")
    controle_base = False
    while controle_base == False:
        base = float(input("Qual é a base? "))
        if condição_base(base):
            controle_base = True
        else:
            print("Valor da base fora da condição de existencência! A base deve ser um número positivo diferente de 1!")
    controle_cd = False
    while controle_cd == False:
        casas_decimais = int(
            input("Com quantas casas decimais você deseja (até 6 estão disponíveis)? "))
        if casas_decimais <= 0 or casas_decimais > 6:
            print("Erro na quantidade de casas decimais")
        else:
            controle_cd = True
    return [logaritimando, base, casas_decimais]


def condição_logaritimando(logaritimando):
    if logaritimando > 0:
        return True


def condição_base(base):
    if base > 0 and base != 1:
        return True


def teste_expoente(base, logaritimando):
    # achar o menor expoente inteiro que mais se aproxima do expoente desejado
    memoria_anterior = 0  # guarda o valor do último inteiro testado
    memoria_prox = 0  # guarda o valor do inteiro testado no momento
    expoente = 0  # será o valor retornado
    pause = False
    while pause == False:
        memoria_prox = base**expoente
        if memoria_anterior <= logaritimando < memoria_prox:
            # testa se o logaritimando está entre os valores
            expoente -= 1  # expoente do inteiro anterior
            return expoente
            pause = True
        else:
            memoria_anterior = memoria_prox
            expoente += 1


def testa_decimais(base, logaritimando, expoente):
    decimais_estatico = 10**(-6)
    # realizará testes com decimais até a 6º casa
    exp = expoente + decimais_estatico  # valor que será retornado
    teste = 0
    while teste <= logaritimando:
        teste = base**(exp)
        exp += decimais_estatico
    return exp


def main():
    dados = entrada_usuario()
    logaritimando = dados[0]
    base = dados[1]
    casas_decimais = dados[2]
    expoente = teste_expoente(base, logaritimando)
    resultado = testa_decimais(base, logaritimando, expoente)
    print(f"O resultado é {resultado: .{casas_decimais}f}")


main()
