def fibonacci(n):
    # Inicializa a sequência com os dois primeiros números
    fib_sequence = [0, 1]
    
    # Gera a sequência de Fibonacci até atingir ou ultrapassar o número informado
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def verificar_fibonacci(n):
    # Chama a função fibonacci para gerar a sequência até o número informado
    fib_sequence = fibonacci(n)
    
    # Verifica se o número informado está na sequência
    if n in fib_sequence:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")

# Entrada do usuário
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
verificar_fibonacci(numero)
