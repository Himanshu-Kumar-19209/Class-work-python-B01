# import tkinter as tk #GUI
# #from file_organizer import organize_files

# root = tk.Tk()
# root.title("File Organizer")
# root.geometry("400*250")

# def show_input():
#     user_input =entry.get()
#     print("user input:", user_input)

# leble =tk.leble(root, text="Enter Folder address")
# leble.pack(pady=10)

# entry =tk.Entry(root, width=100)
# entry.pack(pady=5)

# button =tk.Button(root, text="Submit")
# button.pack(pady=10)

# root.mainloop()
# filename = "example.txt"
# file = open (filename, "w")
# dataString = "Some dummy text data\n newline \t after tab".split()
# fileContent =file.writelines(dataString)
# print(fileContent)
# file.close()


###wap to read a csv file and store 2d


#program to read csv file and return a list of list 
fileName ="data.csv"
#function to read csv file and return list
def read_csv(file_name):
   #ext =file_name.split(".")[-1].lower() 
   #assert ext == "csv","Indvalid file type"
    fileHandle = open(file_name,"r")
    data = fileHandle.read()
    fileHandle.close()

    # rows = data,split("\n")
    # print("\n")

    # print(rows)
    # for i in range(0,len (rows)):
    #     row = rows[i]
    #     rows[i] = row.split(",")
#your logic 

    op =data
    return op  #it should return list list 
receivedData = read_csv(fileName)
print(receivedData)
#print(receivedData[9][2])
