# 1.
# Return the letter grade as a string ("A", "B", "C", etc.)
# for the corresponding float parameter.

def letter_grade(grade):
    if grade >= 90:
        return("A")
    elif grade >= 80 and grade <= 89.9:
        return("B")
    elif grade >= 70 and grade <= 79.9:
        return("C")
    elif grade >= 60 and grade <= 69.9:
        return("D")
    elif grade <= 59.9:
        return("F")

# Test it
print(letter_grade(88.5))

# 2.
# Create a "safe" version of the above function that
# can handle invalid input. See description >>

def safe_letter_grade(grade):
    try:
        grade = float(grade) #return letter_grade(grade)
    except ValueError:
        return("Please enter a valid number.")
    if grade >= 90:
        return("A")
    elif grade >= 80 and grade <= 89.9:
        return("B")
    elif grade >= 70 and grade <= 79.9:
        return("C")
    elif grade >= 60 and grade <= 69.9:
        return("D")
    elif grade <= 59.9:
        return("F")

# Test it
print(safe_letter_grade(88.5))
print(safe_letter_grade("88.5"))
print(safe_letter_grade("eighty five"))
