# APPENDING TO A FILE
# Opening a file in append mode also lets you write to a file
# Except, instead of erasing the contents of the file, it adds to the file from where it previosuly ended
# If the file already exists, it will add to that file, and if the file doesn't exist, it will create it
file = open('new.txt', 'a')
file.write("This is a file \n")
file.write(" I can add\n Multiple Lines\n With write()\n")
file.close()