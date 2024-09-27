import numpy as np

# Função f(x)
def f(x):
    return x**3 - x - 2  # Altere essa função para a equação

# Derivada da função f(x)
def f_derivada(x):
    return 3*x**2 - 1  # Altere essa função para a derivada da sua equação

# Implementação do método de Newton-Raphson
def newton_raphson(x0, tolerancia, max_iteracoes):
    iteracoes = 0
    x = x0

    while iteracoes < max_iteracoes:
        fx = f(x)
        fpx = f_derivada(x)

        # Condição de parada
        if abs(fx) < tolerancia:
            return x

        # Verificação para evitar divisão por zero
        if fpx == 0:
            print("Derivada zero. O método não pode continuar.")
            return None

        # Atualização de x usando o método de Newton-Raphson
        x = x - fx / fpx
        iteracoes += 1

    print("Número máximo de iterações atingido.")
    return x  # Aproximação da raiz

# Parâmetros do método
x0 = 1.5  # Chute inicial
tolerancia = 1e-6  # Critério de parada
max_iteracoes = 100  # Número máximo de iterações

# Chamando o método
raiz = newton_raphson(x0, tolerancia, max_iteracoes)
if raiz is not None:
    print(f"A raiz aproximada é: {raiz}")
