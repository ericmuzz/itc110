
def show_content():
    filename = input("Enter a filename to view its content:")

    file = open(filename, 'r')
    #print(file.read())

    for line in file:
        print(line)

    file.close()

#show_content()

def write_diary():
    filename = input("Enter diary journal name: ")
    file = open(filename, 'w')
    journal_entry = ''

    while journal_entry != 'x':
        journal_entry = input("Enter note, or type 'x' to exit: ")

    file.close()

#write_diary()
from tkinter.filedialog import askopenfilename, asksavefilename

def batch_processing():
    print("Process temperature records.")

    input_filename = askopenfilename()
    output_filename = asksavefilename()

    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')

    #input_file.readline()
    for line in input_file:
        content_list = line.split(',')
        try:
            for temp in content_list
                temp_sum = temp_sum + float(temp)
                temp_count += 1
        except ValueError:
            continue

    input_file.close()

    avg_temp = temp_sum / temp_count
    print("The average temperature is: {0}F".format(avg_temp), file = output_file)

    output_file.close()
    return avg_temp

print("The average temperature is: {0}F".format(batch_processing())
