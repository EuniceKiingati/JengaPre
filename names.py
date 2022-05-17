
def search_name(file_name):
    valid_names=[]
    for line in open(file_name, 'r'):
        if line.startswith("A"):
            words=line.split()
            valid_names.append(words)
            
    print(valid_names)
search_name("names.txt")    

    
    
