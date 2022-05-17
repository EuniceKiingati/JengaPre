def search_name():
    fletter=input("enter the letter (s): ")
    valid_names=[]
    for line in open("names.txt", 'r'):
        if line.lower().startswith(fletter.lower()):
            words=line.split()
            valid_names.append(words)
            
    print(valid_names)
#search_name("names.txt")    

def search_age():
    user_age=input("enter the age (s): ")
    valid_ages=[]
    
    for line in open("names.txt", 'r'):
        if  str(user_age) in line:
            ages=line.split()
            valid_ages.append(ages)
            
    print(valid_ages)#3search_age("names.txt") 


if __name__=="__main__":
    choice=int(input("press 1 to search for name or 2 to search for age: "))
    if choice==1:
        search_name()
    elif choice==2:
        search_age()
    else:
        print("invalid choice ")

