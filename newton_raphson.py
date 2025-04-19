import numpy as np


def eq1(x, r, M, q):
    return 1 - (2*M/r) + (3*M*q*2/r3) - x2*r*2

def eq2(x, y, z, r, M, q):
    return (1 - (2*M/r) + (3*M*q*2/r3))-1 - (y2/(x+z*r)*2)

def eq3(x, y, z, r, M, q):
    return -2*M/r*2 + 9*M*q2/r4 - 2*y2*r/(x+z*r)*3

# finding darivative of equations
def d_eq1_dx(x, r, M, q):
    return -2*x*r**2

def d_eq2_dx(x, y, z, r, M, q):
    return 2*y*2(x+z*r)**-3

def d_eq2_dy(x, y, z, r, M, q):
    return -2*y/(x+z*r)**2

def d_eq2_dz(x, y, z, r, M, q):
    return 2*y*2*r(x+z*r)**-3

# Implement the Newton-Raphson method
def newton_raphson(Xo, Yo, Zo, tol):
    M = float(input("Enter the value for M: "))
    q = float(input("Enter the value for q: "))
    r = float(input("Enter the value for r: "))

    x = Xo
    y = Yo
    z = Zo
    while abs(eq1(x, r, M, q)) > tol and abs(eq2(x, y, z, r, M, q)) > tol and abs(eq3(x, y, z, r, M, q)) > tol:
        x = x - eq1(x, r, M, q) / d_eq1_dx(x, r, M, q)
        y = y - eq2(x, y, z, r, M, q) / d_eq2_dy(x, y, z, r, M, q)
        z = z - eq2(x, y, z, r, M, q) / d_eq2_dz(x, y, z, r, M, q)
    return x, y, z

# Initialize variables
# Initial values of X, Y, Z
Xo = 0.1
Yo = 0.1
Zo = 0.1
tol = 1e-6  # Tolerance for the root approximation

x, y, z = newton_raphson(Xo, Yo, Zo, tol)
print(f"The solutions are x = {x}, y = {y}, and z = {z}")