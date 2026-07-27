def todos_primos(n):
    # verificar se eh inteiro e maior que 1
    if not isinstance(n, int) or n <= 1:
        raise ValueError("A entrada deve ser um inteiro maior que 1.")

    #  verifica recursivamente se "num" tem algum divisor entre "divisor" e sua raiz quadrada
    def verifica_divisor(num, divisor):
        if divisor > int(num ** 0.5):
            return True
        if num % divisor == 0:
            return False
        return verifica_divisor(num, divisor + 1)

    # caso base
    if n == 2:
        return [2]
    
    # constroi a lista de primos ate n-1 recursivamente
    primos = todos_primos(n - 1)
    
    # testa se n tambem eh primo
    if verifica_divisor(n, 2):
        primos.append(n)

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
