for number in range(2,100 +1):
    for i in range (2,number):
        if (number%i)==0:
            break   
    else:
        print(number)
