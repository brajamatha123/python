# a = "this is python class"
# print(a)

# b =(10*2)
# print(b)


# c =(80/6)
# print(c)

# d = (80%7)
# print(d)


# e =(80-30)
# print(e)

# f =(80+60)
# print(f)




num = int(input("Enter a number: "))

# define a flag variable
# flag = False
# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
     if (num % i) == 0:
         # if factor is found, set flag to True
         # flag = True
         # break out of loop
         break

# check if flag is True
if num:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")