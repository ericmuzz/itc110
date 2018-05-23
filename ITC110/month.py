print("Enter a date formatted as: YYYY-MM-DD")

#print it out like June 23, 2018

date_input = input("Enter the date to format: ")

year = date_input[0:4]
month = int(date_input[5:7])
day = date_input[-2:]

months_list = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
     "Sep", "Oct", "Nov", "Dec",
]

print ("The formatted date is {0} {1}, {2}".format(
    months_list[month - 1], day, year))
