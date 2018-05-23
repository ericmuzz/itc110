def main():

    data_file = open('average.txt', 'r')
    sum_of_values = 0.0
    count = 0

    data_file.readline()
    for line in data_file:
        print('line of file=', line)
        for data_point in line.split(','):
            print("Data point in line: ", data_point)
            sum_of_values = sum_of_values + float(data_point)
            count += 1

    print("The average of {0} values is {1}".format(
        count,
        sum_of_values / count))

if __name__ == '__main__':
    main()
