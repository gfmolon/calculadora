import op

while True:
    a = float(input("Valor 1:"))
    b = float(input("Valor 2:"))
    menu = op.opcao()

    if menu == 1:
        print(f"Soma: {a} + {b} = {op.soma(a=a, b=b):.2f}")

    elif menu == 2:
        print(f"Subtração: {a} - {b} = {op.subtracao(a=a, b=b):.2f}")

    elif menu == 3:
        print(f"Multiplicação: {a} * {b} = {op.multiplicacao(a=a, b=b):.2f}")

    elif menu == 4:
        print(f"Divisão {a} / {b} = {op.divisao(a=a, b=b):.2f}")

    else:
        print("Opção inválida.")

    if not op.continuar():
        break
        print("Programa encerrado.")
