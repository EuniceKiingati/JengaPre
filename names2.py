#program to print out names from user input

def search_name(file_name):
    fletter=input("enter the letter (s): ")
    valid_names=[]
    for line in open(file_name, 'r'):
        if line.startswith(fletter):
            words=line.split()
            valid_names.append(words)
            
    print(valid_names)
search_name("names.txt")    
