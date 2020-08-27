import os


def prdir(arr):
    arr_len = len(arr)
    for i in range(0, arr_len):
        print(arr[i],"\n")

def saveintofile(arr):
    file_name = input("Enter the file name to be saved : ")
    filenm = file_name + ".txt"
    print("Files will be stored in ", filenm)
    arr_len = len(arr)
    with open (filenm,'a') as f:
        for i in range(0, arr_len):
            f.write(arr[i]+'\n')
        
    



if __name__ == "__main__":
    path = input("Enter the directory : ")
    arr = os.listdir(path)
    option = int(input("Choice: \n 1. Print Directory \n 2. Save list in file \n Your Choice: "))
    if(option == 1):
        prdir(arr)
    else:
        saveintofile(arr)
