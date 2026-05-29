# WRITING TO A FILE
# When a file is opened in write mode, all the content that was previously in the file gets wiped
# If the file did not exist previously it will be created

file = open('new.txt', 'w') # This will check if new.txt exists, otherwise it will create it

# You can write data to a file using the write() function. 
# Note however that  write() does not automatically add newlines and instead you need to manually add them

file.write("This is a file \n")
file.write(" I can add\n Multiple Lines\n With write()\n")

# You can also write multiple lines with the writelines() function
# This function will take a list of strings as the argument and write all of them
# NOte that you will have to manually add newline characters here as well

lines= ["First\n", "second\n", "Third\n"]
file.writelines(lines)

file.close()