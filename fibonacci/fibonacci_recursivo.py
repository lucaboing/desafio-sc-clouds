def fib(n):
    # se for negativo, mostra o erro e para a funcao
    if n < 0:
        raise ValueError("A entrada deve ser um número inteiro maior ou igual a zero.")

    # casos base
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

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
