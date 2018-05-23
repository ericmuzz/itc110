def main():
    sum_of_values = 0.0
    count = 0

    x = input('Enter number in list to avg. ("q" to exit) ')
    while 'q' not in x.lower():
        sum_of_values = sum_of_values + float(x)
        count += 1
        x = input('Enter the number in list to avg. ("q" to exit) ')

    print("The average of {0} values is {1}".format(
        count,
        sum_of_values / count))

if __name__ == '__main__':
    main()
