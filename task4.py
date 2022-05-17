for num in range(1, 100):
    sum_num=0

    string_number = str(num)
    for i in string_number:
        sum_num+=int(i)
    

    if num%sum_num ==0:
        print(num)
    