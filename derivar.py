import sympy as sp

# Definir a variável simbólica
x = sp.symbols('x')

# Definir a função
f = x**3 - x - 2

# Calcular a derivada
f_derivada = sp.diff(f, x)

print(f"Derivada de f(x): {f_derivada}")
