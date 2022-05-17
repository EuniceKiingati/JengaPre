
def search_age(file_name):
    valid_ages=[]
    num=5
    for line in open(file_name, 'r'):
        if  str(num) in line:
            ages=line.split()
            valid_ages.append(ages)
            
    print(valid_ages)
search_age("names.txt")   
    
    
    
