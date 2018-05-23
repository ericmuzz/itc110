#Solve quadratic equation

import math

def solve_quadratic(a, b, c):
    try:
        discroot = math.sqrt(b * b - 4 * a * c)
        x1 = (-b + discroot) / (2 * a)
        x2 = (-b - discroot) / (2 * a)
    except: ValueError:
        print("The values are out of bounds")
        return False, False
    #print("The solution is: x=", x1, "and x=", x2)
    return x1, x2

cat1, cat2 = solve_quadratic(2, -3, -4.5)

print("x1 =", cat1)
print("x2 =", cat2)
