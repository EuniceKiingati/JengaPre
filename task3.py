#odd numbers divisible by 7 and not 3
for number in range(100):
    if (number%2!=0) and (number%7==0) and (number%3!=0):
        print(number)
