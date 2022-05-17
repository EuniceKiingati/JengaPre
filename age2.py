def search_age(file_name):
    user_age=input("enter the age (s): ")
    valid_ages=[]
    
    for line in open(file_name, 'r'):
        if  str(user_age) in line:
            ages=line.split()
            valid_ages.append(ages)
            
    print(valid_ages)
search_age("names.txt") 