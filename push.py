import os
if not os.path.exists("data.txt"):  
    file1 = open("data.txt","a") # use "a" to append data to existing file

    fName = "Alex"
    lName = "Gorbachov"
    age = 45
    id_n = "31882222"

    Hello_Message = 'Hello {} {}, {} years old, with ID number: {}.'


    file1.write(Hello_Message.format(fName, lName, age, id_n))
    file1.close()
else:
    print("File exist")
