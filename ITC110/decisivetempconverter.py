def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = 9.0 / 5.0 * celsius + 32

    print("The temperature in Fahrenheit is: ", fahrenheit)

    if fahrenheit >= 90 and fahrenheit < 212:
        print("It's way too hot. Go get ice cream.")
    if fahrenheit <= 32:
        print("It's so cold. Better get the ski gear out.")
    if fahrenheit == 212:
        print("It's boiling in here. Better jump out of the pot.")
    if fahrenheit == 75:
        print("It's perfect weather. Get outside.")

if __name__ == '__main__':
    main()
