# num =int(input("Enter your number:"))
# for i in range (1,num):
#     if num %  i == 0:
#         print("this is not prime number") 
#     else:
#         print("this is prime number")    
            
            
            
        


Num= int(input("enter your number: "))
        if Num > 1:
            for i in range(2, Num):
                if (Num % i) ==0:
                    break
                if Num:
                    
                    print(Num, "is not a prime number")
                    
                else:
                    print(Num, "is a prime number")