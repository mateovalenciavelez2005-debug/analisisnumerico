import numpy as np
import sympy as sp
from scipy.integrate import quad

# --- Entrada del usuario ---
x = sp.Symbol('x')
f_input = input("Ingrese la función f(x): ")
f_sympy = sp.sympify(f_input)

# Convertimos a función evaluable en Python
f = sp.lambdify(x, f_sympy, modules=['numpy'])

# Límites de integración y número de subintervalos
a = float(input("Ingrese el límite inferior a: "))
b = float(input("Ingrese el límite superior b: "))
n = int(input("Ingrese el número de subintervalos (n): "))

# Validaciones
if n % 2 != 0:
    print("Advertencia: Simpson 1/3 requiere n par. Se incrementará en 1.")
    n += 1

if n % 3 != 0:
    print("Advertencia: Simpson 3/8 requiere n múltiplo de 3. Se incrementará a próximo múltiplo.")
    while n % 3 != 0:
        n += 1

h = (b - a) / n
xi = np.linspace(a, b, n + 1)
fi = f(xi)

# --- Trapecio Compuesto ---
trapecio = (h/2) * (fi[0] + 2 * np.sum(fi[1:-1]) + fi[-1])

# --- Simpson 1/3 Compuesto ---
simpson13 = (h/3) * (fi[0] + 4 * np.sum(fi[1:n:2]) + 2 * np.sum(fi[2:n-1:2]) + fi[-1])

# --- Simpson 3/8 Compuesto ---
simpson38 = (3*h/8) * (fi[0] + 3 * np.sum(fi[1:n] [(np.arange(1, n)%3 != 0)]) +
                       2 * np.sum(fi[1:n] [(np.arange(1, n)%3 == 0)]) + fi[-1])

# --- Integral exacta ---
integral_exacta = float(sp.integrate(f_sympy, (x, a, b)).evalf())

# --- Errores absolutos ---
error_trap = abs(integral_exacta - trapecio)
error_simp13 = abs(integral_exacta - simpson13)
error_simp38 = abs(integral_exacta - simpson38)

# --- Resultados ---
print("\n--- Resultados ---")
print(f"Integral exacta: {integral_exacta:.10f}")
print(f"Trapecio compuesto: {trapecio:.10f}  | Error: {error_trap:.2e}")
print(f"Simpson 1/3 compuesto: {simpson13:.10f}  | Error: {error_simp13:.2e}")
print(f"Simpson 3/8 compuesto: {simpson38:.10f}  | Error: {error_simp38:.2e}")
