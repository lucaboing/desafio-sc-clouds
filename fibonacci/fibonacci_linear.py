mensagem_erro = "A entrada deve ser um número inteiro maior ou igual a zero."

def fib(n):
    # se for negativo, mostra o erro e para a funcao
    if n < 0:
        print(mensagem_erro)
        return

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
    resultado = fib(numero)
    
    # so imprime o resultado se ele nao for none (se nao deu erro)
    if resultado is not None:
        print(f"fib({numero}) = {resultado}")

except ValueError:
    print(mensagem_erro)
