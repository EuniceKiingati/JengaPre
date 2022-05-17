
for num in range(1, 100):
    sumdigits=0
    n=num
    
    while n>0:
        digit=n%10
        sumdigits=sumdigits+digit
        n=n//10
    sq_sum=sumdigits*sumdigits   
    #print(sum)
    if num==sq_sum:
        print(num)


    
