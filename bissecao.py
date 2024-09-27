import numpy as np
# np.sqrt(a) Raiz quadrada np.sin(a) Seno np.cos(a) Cosseno

# Função f(x) (x) o que eu quero encontrar 
def f(x):
    return x**3 - x - 2  # Altere essa função para a equação

# Implementação do método da bissecção
def bisseccao(a, b, tolerancia, max_iteracoes):
    if f(a) * f(b) >= 0:
        print("Não há garantia de uma raiz neste intervalo.")
        return None
    
    iteracoes = 0
    while iteracoes < max_iteracoes:
        c = (a + b) / 2.0  # Ponto médio

        # Condição de parada
        if abs(f(c)) < tolerancia:
            return c

        # Decidir qual lado continuar a pesquisa
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        iteracoes += 1

    print("Número máximo de iterações atingido.")
    return (a + b) / 2.0  # Aproximação da raiz

# Parâmetros do método
a = 1  # Início do intervalo
b = 2  # Fim do intervalo
tolerancia = 1e-6  # Critério de parada
max_iteracoes = 100  # Número máximo de iterações

# Chamando o método
raiz = bisseccao(a, b, tolerancia, max_iteracoes)
if raiz is not None:
    print(f"A raiz aproximada é: {raiz}")
