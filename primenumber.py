

num = int(input("enter your number= "))
if num > 1:
    for i in range (2,num):
        if (num % i) == 0:
            if num:
                print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
               
        
