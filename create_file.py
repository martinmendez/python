#Open file in write mode (an existing file with the same name will be erased)
file = open("newfile.txt", "w")
file.write("hello world in the new file\n")
file.write("and another line\n")
file.write("and another line2\n")
file.close()

#Open and read the created file, luego stdout

file = open('newfile.txt', 'r')
print file.read()

#Open for append data

file = open('newfile.txt', 'a')
file.write("esto lo agregamos al final via append")
file.close

file = open('newfile.txt', 'r')
print file.read()
