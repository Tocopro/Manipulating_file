
file1 = open("C:\\Users\\NEAK\\Downloads\\copy_file.txt", "r")
file2 = open("C:\\Users\\NEAK\\Downloads\\new_file.txt", "w")
for line in file1:
    for element in range(0, len(line)):
        if element == "\t":
            print("yes")
        else:
            print("No")
        print(line[element], end='')

file1.close()
file2.close()
