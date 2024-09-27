# Função que define a equação a ser resolvida
def f(i):
    P = 35000  # Valor do veículo
    A = 8500   # Pagamento anual
    n = 7      # Número de anos
   
    return P * (i * (1 + i)**n) / ((1 + i)**n - 1) - A

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
a = 0.01  # Limite inferior do intervalo 
b = 0.2   # Limite superior do intervalo 
tolerancia = 1e-5  # Critério de parada
max_iteracoes = 100  # Número máximo de iterações

# Chamando o método
taxa_juros = bisseccao(a, b, tolerancia, max_iteracoes)
if taxa_juros is not None:
    print(f"A taxa de juros aproximada é: {taxa_juros * 100:.4f}% ao ano")
