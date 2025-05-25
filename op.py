def soma(a: float, b: float) -> float:
    return a + b


def subtracao(a: float, b: float) -> float:
    return a - b


def multiplicacao(a: float, b: float) -> float:
    return a * b


def divisao(a: float, b: float) -> float:
    if b > 0:
        return a / b
    else:
        return 0


def opcao() -> int:
    print("CALCULADORA")
    print("_" * 6)
    print("1-SOMA")
    print("2-SUBTRAÇÃO")
    print("3-MULTIPLICAÇÃO")
    print("4-DIVISÃO")

    selecao = int(input("Opção:"))

    while selecao < 1 or selecao > 4:
        selecao = int(input("Opção:"))
    return selecao


def continuar() -> bool:
    while True:
        escolha = input("Continuar? (S/N)").upper()

        if escolha == "S":
            return True
        elif escolha == "N":
            return False
        else:
            continue
