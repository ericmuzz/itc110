#tempconverter.py
# A program to convert Celsius temps to Fahrenheit
# by: Eric Muzzarelli

def main():
    celsius = float(input("Enter the Celsius temperature: "))
    fahr = 9 / 5 * celsius + 32
    print("The temperature in Fahrenheit is: ", fahr)

main()
