def fib(n):
    # se for negativo, mostra o erro e para a funcao
    if n < 0:
        raise ValueError("A entrada deve ser um número inteiro maior ou igual a zero.")

    # casos especiais
    if n == 0:
        return 0
    if n == 1:
        return 1

    # casos base
    anterior = 0
    atual = 1
    # para n >= 2, vai somando passo a passo
    for i in range(2, n + 1):
        proximo = anterior + atual
        anterior = atual
        atual = proximo

    return atual

# --- entrada e saida ---
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("A entrada deve ser um número inteiro maior ou igual a zero.")
else:
    try:
        resultado = fib(numero)
        print(f"fib({numero}) = {resultado}")
    except ValueError as erro:
        print(erro)
