# Q.1.  Write a Python function that takes a list of words and returns the length of the longest one
# words = []
# for i in range(1,5):
#     word = input(f"Enter {i} word: ")
#     words.append(word)
# print(words)
#
# max_length = 0
# longest_word = ""
#
# for i in range(len(words)):
#     current_length = len(words[i])
#     if current_length > max_length:
#         max_length = current_length
#         longest_word = words[i]
#
# print(f"The longest word is: {longest_word}")
# print(f"Its length is: {max_length}")
#
# # ---------------------------------------------------------------------------------------------------
# write a python funciton that takes a list of words and returns the length of the longest one
# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------------------------------------
# SOLUTION 1:
# words = int(input("enter number of items in a list: "))
# items = []
# for item in range(words):
#     word=input(f"Enter {item} word: ")
#     if word in items:
#         continue
#     else:
#         items.append(word)
#
# print(items)
# ---------------------------------------------------------------------------------------------------
# Q.2. Write a Python program to remove duplicates from a list
# words = int(input("enter number of items in a list: "))
# items = []
# for item in range(words):
#     word=input(f"Enter {item+1} word: ")
#     items.append(word)
# print("Original list:", items)
#
# i = len(items) - 1
# while i > 0:
#     j = i - 1
#     while j >= 0:
#         if items[i] == items[j]:
#             del items[j]
#             print("REMOVED")
#             i -= 1
#             break
#         j -= 1
#     i -= 1
#
# print("Final list:", items)

#
# print(items)
# ---------------------------------------------------------------------------------------------------
# Q 3. Create a list of books
# e.g. booklist =[['Java 8', 700], ['Python for Beginners', 500],....]
# ---------------------------------------------------------------------------------------------------
# SOL1
# books=int(input("enter number of total books : "))
# list1=[]
# for i in range(books):
#     book_name=input("enter name of the book: ")
#     book_price=input(f"price of {book_name}: ")
#     new_set = []
#     new_set.append(book_name)
#     new_set.append(book_price)
#     list1.append(new_set)
# print(list1)
# #
# print("1.add a new book with price")
# print("2.Remove entry for a book: ")
# # print("select any option: ")
# # print("select any option: ")
# book=int(input("press any number: "))
# if book==1:
#     book_name = input("enter name of the book: ")
#     book_price = input(f"price of {book_name}: ")
#     new_set = []
#     new_set.append(book_name)
#     new_set.append(book_price)
#     list1.append(new_set)
# elif (book==2):
#     rem=int(input(" which book you want to remove"))
#     list1.remove(list1[rem])

# print(list1)


fruit1={"mango","banana","watermelon","guava","orange"}
fruit2={"mango","banana","watermelon","guava","orange","strawberry"}

# num1=fruit1|fruit2
# print("num1 = ",num1)

# inter1=fruit1.intersection(fruit2)
# print(inter1)
#
# diff1=fruit1.difference(fruit2)
# print(diff1)


# nums = [1,2,3,4,5,6,7,8,9,10]
# mydict = {i:i**2 for i in nums}
# print(mydict)









# # ------------------------------------------------------------------------------------------
# Q 3. Create a list of books
# e.g. booklist =[['Java 8', 700], ['Python for Beginners', 500],....]
#
# Perform following operations on the list
# 1. Add a new book with price
# 2. Remove entry for a book
# 3. update price for a book
# 4. Sort the list by book names
# 5. Sort the list by prices
# 6. Print the book with max and min price [hint : you may use min()/max() functions of python]
books = int(input("enter number of total books : "))
list1 = []
for i in range(books):
    book_name = input("enter name of the book: ")
    book_price = int(input(f"price of {book_name}: "))
    new_set = [book_name, book_price]
    list1.append(new_set)
print("Original list:", list1)

while True:
    print("\n1.Add 2.Remove 3.Update 4.Sort Name 5.Sort Price 6.Max/Min 0.Exit")
    choice = int(input("Choose: "))

    if choice == 0:
        break

    elif choice == 1:
        book_name = input("enter name of the book: ")
        book_price = int(input(f"price of {book_name}: "))
        list1.append([book_name, book_price])
        print("Added!")

    elif choice == 2:
        index = int(input("Enter index to remove: "))
        if 0 <= index < len(list1):
            del list1[index]
            print("Removed!")
        else:
            print("Invalid index!")

    elif choice == 3:
        index = int(input("Enter index to update: "))
        if 0 <= index < len(list1):
            new_price = int(input("New price: "))
            list1[index][1] = new_price
            print("Updated!")
        else:
            print("Invalid index!")

    elif choice == 4:
        i = 0
        while i < len(list1):
            j = i + 1
            while j < len(list1):
                if list1[i][0] > list1[j][0]:
                    list1[i], list1[j] = list1[j], list1[i]
                j += 1
            i += 1
        print("Sorted by name!")

    elif choice == 5:
        i = 0
        while i < len(list1):
            j = i + 1
            while j < len(list1):
                if list1[i][1] > list1[j][1]:
                    list1[i], list1[j] = list1[j], list1[i]
                j += 1
            i += 1
        print("Sorted by price!")

    elif choice == 6:
        max_price = -1
        min_price = 999999
        max_book = ""
        min_book = ""
        i = 0
        while i < len(list1):
            if list1[i][1] > max_price:
                max_price = list1[i][1]
                max_book = list1[i][0]
            if list1[i][1] < min_price:
                min_price = list1[i][1]
                min_book = list1[i][0]
            i += 1
        print(f"Max: {max_book} (${max_price})")
        print(f"Min: {min_book} (${min_price})")

    print("Current:", list1)
'''
Q.4. Write a Python program to compute element-wise sum of given tuples, using “zip()” function
Original tuples:
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Element-wise sum of the said tuples:
(6, 9, 8, 6)
'''

# t1= (1,2,1,4)
# t2= (3,5,1,0)
# t3= (2,2,3,1)
# result = tuple(a+b+c for a,b,c in zip(t1,t2,t3))
# print(result)

# '''Q.5 Write a Python program to find the repeated items of a tuple.'''
#
# tup = (2, 4, 5, 6, 2, 3, 4, 4, 7, 8, 4, 3, 2)
# print("Original tuple:", tup)
# repeated = ()
# for i in tup:
#     if tup.count(i)> 1 and i not in repeated:
#         repeated += (i,)
# print("Repeated Items", repeated)


