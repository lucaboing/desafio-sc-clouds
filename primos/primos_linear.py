def todos_primos(n):
    # verificar se eh inteiro e maior que 1
    if not isinstance(n, int) or n <= 1:
        raise ValueError("A entrada deve ser um inteiro maior que 1.")

    primos = []

    for i in range(2, n + 1):
        eh_primo = True
        # estrutura para procurar divisores de i
        for divisor in range(2, int(i ** 0.5) + 1):
            if i % divisor == 0:
                eh_primo = False
                break

        if eh_primo:
            primos.append(i)

    return primos


# --- entrada e saida ---
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("A entrada deve ser um inteiro maior que 1.")
else:
    try:
        print(todos_primos(numero))
    except ValueError as erro:
        print(erro)


