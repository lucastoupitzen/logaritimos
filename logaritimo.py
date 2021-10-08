#!/usr/local/bin/python3


def entrada_usuario():
    # input do usuário com a base, logaritimando e as casas decimais do \
    # resultado
    controle_logaritimando = False  # chave de controle para não quebrar
    # o código no input
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
            print("Valor da base fora da condição de existencência! A base \
                 deve ser um número positivo diferente de 1!")
    casas_decimais = casas_dec()  # recebe o valor de casas decimais
    return [logaritimando, base, casas_decimais]


def casas_dec():  # recebe e analisa o número de casas decimais
    controle_cd = False
    while controle_cd == False:
        casas_decimais = int(
            input("Com quantas casas decimais você deseja (Recomendado: 6 \
                casas decimais)? "))
        if casas_decimais <= 0:
            print("Erro na quantidade de casas decimais")
        elif casas_decimais > 6:
            print(
                "Alerta: Muitas casas decimais tornam o cálculo mais lento. É \
                    recomendado o uso de até 6 casas.")
            resposta = str(input(
                f"Deseja continuar (sim ou não) o cálculo com {casas_decimais} \
                    casas decimais? "))
            resposta.lower
            if resposta == "sim":
                controle_cd = True
        else:
            controle_cd = True
    return casas_decimais


def condição_logaritimando(logaritimando):  # condição de existência
    if logaritimando > 0:
        return True


def condição_base(base):  # condição de existência
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


def testa_decimais(base, logaritimando, expoente, casas_decimais):
    decimais_estatico = 10**(- (casas_decimais + 1))  # +1 evita imprecisões
    # realizará testes com decimais até a 7º casa
    exp = expoente  # valor que será retornado
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
    resultado = testa_decimais(base, logaritimando, expoente, casas_decimais)
    print(f"O resultado é {resultado: .{casas_decimais}f}")


main()

