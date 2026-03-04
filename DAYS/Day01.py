# i = (10,11,12)
# j = (10,11,12)
# k = {10:"vijay",11:"pratiksha",12:"ashish"}

# print(i==j)
# print(i is j)
# print(k[11])

# Python code to test that
# tuples are immutable

# tuple1 = (0, 1, 2, 3)
# tuple1[0] = 4
# print(tuple1)

# print("---------------------------------------------------------")
# list1 = [0, 1, 2, 3]
# list1[0] = 4
# print(list1)
# k1 = {10:"vijay",11:"pratiksha",12:"ashish"}
# k2 = {10:"vijay",11:"pratiksha",12:"ashish"}
# print(k1==k2)
# print(k1 is k2)

# j1= input("enter you name: ")
# j2= int(input("Enter age: "))
# print(f"entered name is {j1} and age is {j2}")

# no=4e6
# print(no)
# num=78000
# print("num: ",num)
# print(f'{num:.5f}')
# print(f'{num:<10}')
# print(f'{num:>10}')
# print(f'{num:^10}')
# print(f'{num:10}')
# print(f'{num:019}')
# print(f'{num:,.2f}')

# marks = 0.65
# print(f'{marks:0%}')
# print(f'{marks:.0%}')
# print(f'{marks:.02%}')

# -----------------------------------------------------------------------------------------------
# Conditional Loops
# -----------------------------------------------------------------------------------------------

# a=int(input("Enter Your age: "))
# if (a>51 and a<100):
#     print("senior citizen")
# elif (a>25 and a<50):
#     print("youngster")
# elif (a>0 and a<25):
#     print("child")
# else:
#     print("abnormal")

#FOR LOOP
# for i in range(10,0,-1):
#     print(i)

# for i in range(0,10):
#     if i == 6:
#         continue
#     print(i)

# for i in range(0,10):
#     if i == 6:
#         break
#     print(i)

# i=0
# while i!=10:
#     print(i)
#     i+=1

# Input: x = 3
# Output: 3 2 1 0
# Explanation:
# Numbers in decreasing order from 3 are 3, 2, 1, 0

# num=int(input("enter number"))
# while(num >0):
#     print(num)
#     num-=1

# Input:
# N = 5
# Output:
# 5 10 15 20 25 30 35 40 45 50

# num=5
# for i in range(1,11):
#     print(num*i)

# num=int(input("enter your number"))
# for i in range(1,11):
#     print(num*i)

# Q1
# num=int(input("enter number"))
# fact=1
# for i in range(num,0,-1):
#     print(fact,"*",i)
#     fact=fact*i
# print (fact)

# 2
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Last Number: "))
# for i in range(num1,num2):
#     for j in range(2,i//2):
#         if i%j == 0:
#             break
#     else:
#         print(i,end=" ")


# input =321
# output = 123

# num=input("enter number")
# print(num[::-1])

# 3.
# input=654
# num=int(input("enter number: "))
# a=num%10                          4
# b=num//10 %10                     5
# c=num//100                        6
# sum = a*100+b*10+c
# print(sum)

# Q 4)
# num = 23456
# output = 5
# num=int(input("enter number: "))
# digits = 0
# total = 0
# even_count = 0
# odd_count = 0
# while (num>0):
#     sum = num % 10
#     # print("SINGLE DIGIT ", sum)
#     if sum%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
#     total = total + sum
#     num=num//10
#     digits+=1
# print("TOTAL DIGITS",digits)
# print("sum of every number",total)
# print("TOTAL EVEN = ",even_count)
# print("TOTAL ODD = ",odd_count)


# Q5)
