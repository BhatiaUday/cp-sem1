# Write a Python program to append text to a file and display the text. 
def file_edit(fname):
    txt = open(fname)
    print("Orignal file: ")
    print(txt.read())
    txt.close()
    with open(fname, "a") as myfile:
        myfile.write("Test data \n")
    txt = open(fname)
    print("Edited file: ")
    print(txt.read())
    txt.close()
file_edit('test.txt')