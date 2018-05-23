# Factorials

#500 employees

# Employee ID a,b,c,d
#abc, def
#Invalid abb, cdd

#ABCDE
accumulator = 1
for factor in [6, 5, 4, 3, 2]:
    accumulator = accumulator * factor
    #print("accumulator=", accumulator)

def factorial(starting_value):
    accumulator = 1
    for factor in range(starting_value, 1, -1):
        print("factor is", factor)
        accumulator = accumulator * factor
        print("accumulator= ", accumulator)

    return accumulator

print("The answer is:", factorial(6))
