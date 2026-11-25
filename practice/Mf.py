# Integers "25, -25, all integers"
# name1 = "sk" or name2 ='sk' (strings)
# Float = Decimal values " 3.99, 2.5, etc"
# Boolean = TRUE and FALSE (write the capital letters)
# None data type = stores no value "example a=none"
# a=None
# age=24.5
# print(type(age))
# print(type(a))
# # A reserved word is a word that python has already claimed for its own use. You cannot use it as a name for your variables, types, functions and classes.
# # In words ko, koi variables se define nahi kar sakthe hai
# # and, as, except.else, break, None, class, continue, def, del, elif, finally, False, True, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, with, while, yield.         
# # Python is a case sensitive language, 'A' and 'a' makes a difference 
# # to comment out multiple lines, just press 'Cntrl + /'
# # Types of operators
# # - Arithematic operators (*,+,-,/,%,**) (% is the modular, that returns the value 'reminder', such as, 7 divided by 3, gives the reminder 1. 
# # ** is the power operatoir, that calculates a^b value )
# # - Relational Operators ( ==, !=, >, <, ) (to compare between two values or terms 
# # such as a=b (in mathematical, but in python it is a==b 'remember, = is used for assigning th evalues or for variables, but not for comparing'))
# # and for anot equal to b, in python it is a!=b (generally in programming, ! is the negation)
# a =20
# b= 30
# print (a==b)
# print (a!=b)
# print (a>=b)
# print(a<=b)
# print (a>b)
# print (a<b) # here, all the relational operators, provides us the result as a boolean value (True or False)
# # # - Assignment operators (=, +=, -+, *=, /=, %=, **= . Example a = 20, now for the +=, and -= by the below example|\
# x = 100
# x *= 5
# x %= 20
# print(x) # the output will be 130, since, the x+=50 means x = x+ 50, and ofcourse the code goes line by line
# # # Logical operators work based on boolean operators (and, or, not)
# # print (not True) # output as false
# # print (not False) # output as True
# # # "not" operators work for one value, whereas and "and" and "or". 
# val1 = 3
# val2 = 4
# x = val1 == val2
# val3 = 4
# print (x and val3) # meh sach tabi bolunga, jab dhono values true ho. and since both are true here,
# # # it provides the value 4 as the value, when the condition both are TRUE, if not it returns the boolean False
# # # For the Or operator, if something in the comparison is True, even if the other is False, the answer will be True
# # # - Type conversion
# # # when float and integer is added (arithematic operation), python prints the result in terms of float, since, float is a higher data type that int
# # # but when it interprutts between string and float, it is not allowed (and pops error). In that case, you have to type cast the str to int
# a = int("2") # this is type casting, since "2" is a string although 2 is an int. and you type cast it by int"2
# b = 4.25
# sum = a+b
# print(sum)
# print (True+1)
# # Type conversion and type casting - Python does the type conversion automatically, which are doable. And which are not doable, then that has to be type casted by you manually
# # Such as the string with the integer, cannot be combined, but you can type cast the string as shown above example and then add it with the integer
# a = 3.14
# a = str(a)
# print(type(a)) # although 3.14 is a float, after type casting it manuallky, it is a string as a out put now (a)
# # In python, the input is taken using the function 'input()'
# name = input("enter")
# print ("Welcome", name) # but the thing is, when ever we are using the input fucntion, then the input 
# # (whether value, name, interger, float, whatever u give as input) the input function treats it as a string "" (by default)
# # Henceforth, in order to treat it as the original data type input, we have to use the type casting
# val = float(input("ENter: ")) # this gives the output as float, even if you enter an integer (25 will be 25.0)
# print (type(val), val)
# val1 = int(input("Enter the first number: "))
# val2 = int(input("Enter the secound number: "))
# b = int((val1+val2))
# print(b)
# # WAP to input side of a square and print its area
# Side = float(input("Enter the value of the side: "))
# print("b: ", Side**2)
# CHAPTER 2
# str1 = "I am sai vignesh"
# # concatination: basically to add two strings 
# str1="sai"
# str2="\tvignesh" # \t is the tab space 
# print(str1+str2)
# print(len(str1)) # length of the string
# # Indexing concept is somewhere, where we can access the string character, but not manipulate of modify it.
# #Slicing concpet : Accessing the parts of the string (String ko parts meh thod the hai (break))
# str = "apnacollege"
# print(str[1:4]) # we get the characters 1, 2, and 3..but not 4
# print(str[5:len(str)]) # 5th character se end of the character thak. Aur end ko empty rakhne se bhi, python thinks end thak.(eg.[5:])
# # Negative indexing meh (APPLE) (-5, -4, -3, -2, -1) - this is the sequence of the value, is meh bhi, [-5:-1] so, Appl itna hi, E ko skip kardega
# #STRING FUNCTIONS
# str = "i am studying python from utube"
# print(str.endswith("ube")) # you can check if any string ends with particular syubstring, then you can use this (str.endswith())
# str = "I am studying python from utube"
# str = str.capitalize() # If you have to capitalize the sentence, (here, I becomes capitalized)
# print(str)
# str = "I am studying python"
# print(str.replace("python", "javascript")) # this replaces the word in the sentence or any letter if you want to replace in the sentence
# # you can also which, in which position the character is using the function (str.find())
# str = "I am studying python"
# print(str.find("o")) # it tells, where it is present for the 1st time in the sentence. Also, 
# # when there is nothing present on the sentence that you are entering for searching, then the output will be (-1 (which is not a valid index))
# # now, if you want to find if any character that hpow much times it is present in the word, then you have to use the string count function (str.count())
# print(str.count("n")) # here, in the sentence 2 times 
# # # WAP to input user's first name and print its length 
# # First_name = input("Enter your First Name: ")
# # print(len(First_name))
# # #WAP to find the occurance of S in a string
# # str = First_name
# # print(str.find("S"))
# # print(str.count("S"))
# # CONDITIONAL STATEMENTS - if, elif, else (SYNTAX)
# Traffic_light = "green"
# if (Traffic_light =="green"):
#     print("go")
# elif(Traffic_light =="Red"):
#     print("stop")
# elif(Traffic_light =="yellow"):
#     print("wait")
# else: 
#     print("you can do what eveer you want") # remeber: for everything the semi colon is compulsary. since, the print and the statement should not be on the same alignment
# # grading system example
# marks = int(input("Enter the marks: "))
# if (marks >=90):
#     print("Grade = A")
# elif (marks >= 50):
#     print ("Grade = B")
# else:
#     print("FAIL BITCH")
# # Nesting if ke andar if (ek statement ke andar doosri statement ko lena hai)
# age = int(input("Enter your age"))
# if (age >= 18):
#     if (age >=80):
#         print("Cannot drive")
#     else:
#         print("can drive")
# else:
#     print ("Cannot drive")
# # lists are built in data type, that stores the set of values
# # imagine there are 5 students, and each student's marks you are defining as a variable. 
# m1 = 94.5
# m2 = 87.3
# m3 = 66.5
# m4 = 70.3
# m5 = 71.2
# Now only 5 students so, 5 different variables to define them, in case if there are more students and we have to define them many variables, which will be difficult while tracking back.
# Thats y this built in data type, that stores into single list
# m = [94.5, 87.3, 66.3] # multiple types of datas can be stored in a single list
# print(type(m), m)
# # Strings are immutable (unchangeable), and the lists are mutable (changeable)
marks  = [85, 64, 33, 95, 76] # this is a list
print(marks) 
x = "23" # this is a string
print(x[0])
# x[0] = "1" # here, it will be an error, since, strings are immutable
# # write a program if a number entered by the user is odd or even 
# x = int(input("Enter the number"))
# rem = x % 2
# if (rem == 0):
#     print("User has entered an Even number")
# else:
#     print ("User has enetered a odd number")
#write a program to find the greatest of the entered 3 numbers provided by the user
# x = int(input("Entre number 1: "))
# y = int(input("Entre number 2: "))
# z = int(input("Entre number 2: "))
# if (x>y and x>z):
#     print ("x is the greatest number",x)
# if (x >=y and y !=z):
#     print("both x and y are same numbers")
# if (x != y and y >=z):
#     print("y and z are same")
# if (x >=z and y != z):
#     print("x and z are same")
# elif(y>z):
#     print ("y is the greatest number", y)
# else:
#     print("z is the greatest nuber", z)
# Continuation:Lists and tuples:is a built in data type, that stores eet of values
# student  = ["karan", 95.4, 1]
# In python, strings can access the index values, but were not able to mutate, whereas, the lists can also access the index and also mutate in that
student = ["karan", 59, 17, "Delhi"] # here, in the list, 0 is the student name, but not the letter k, 1 is the 59, 2 is the 17, 3 is Delhi
print(student[0])
student[2] = 21
print(student)
# List slicing: list_name[starting_idx : ending_idx] and here, ending index will not be included
print(marks[1:4])
print(student[0:2]) # and same, if you want upto end, leave the end empty (student[1:])
# List methods or functions other than print(), len(). But these functions are list specific
x = [4, 3, 1] # x is the list 
x.append(2) # adds on one element (specified) at the end
print(x)
x.sort() # sorts the list into ascending order
print(x)
x.reverse() # sorts the list into reverese order of the list sequence
print(x)
x.insert(1, 5) # Inserts an element as the specific indiex position (list.insert(idx, element))
print(x) #[4, 5, 3, 2, 1]
M =[1, 2, 3, 4]
M.sort(reverse=True) # in this function, M.sort() is where you are telling the function to go to the memory and sort, so, if you directly eneter print(M.sort()), it returns value as none.
print(M) # henceforth, it is better to first write the function and then use the print function
# it is also possible to sort the string characters 
x.remove(2) #removes first occurance of the element # and here, since, in final x list, there is no 2, so, it pops x as it is
print(x)
x.remove(4)
print(x) # now here, since 4 is present in X, 4 will be removed when it comes 1st time
x.pop(1) # this respective index elelmet will be removed 
print(x) # if you anna see more functions, use AI, or x.(search)
# New data type: Tuples (a built in data type, that lets us create immutable sequence of values) # Lists are mutable, whereas, Tuples are Immutable sequences of values
# and TUples are replica of Lists without changable character # to convert a list to tuple, then instead of [], use ()
M=(2, 1, 3, 4) # this is a tuple
# print(M[2]) # tuple can access the index, but cannot chnage the values. So, if I mention, print(M[2]=3), this pops error
# print(type(M))
# # a good example
# M =(20, 1, 3, 4) # here, python considers (since, only one value, without the comma), as integer or whatever data type you write. and if you write it with comma (M=(20, )), it will be considered as a tupple
# print(type(M))
# Slicing under tuple print(M[1:4]), same concept of how we did before
#tuple.index(el) - returns index of first occurance
print(M.index(2)) # this is the function used for checking the index number of the value 2, so the values return's would be 0
print(type(M))
print(M.count(2)) # how many times the value 2 is coming in the tuple
#WAP to ask the user to enter names of their 3 fav. movies and store them in a list
# A = input("Enter your 1st fav movie: ")
# B = input("Enter your 2nd fav movie: ")
# C = input("Enter your 3rd fav movie: ")
#WAP to check if a list contains a palindrome of elements. Palindroms: RACECAR (iska ulta be same hai)
#NOTE: Dictonary and sets (New chapter): Dictionaries are used to store data values in key:value pairs (Meaning, there will be a key and then its value, as such) - "key": valuei
info = {
    "key" : "value", # only strings with double quotes (so, this is the column of keys and column of values respectively)
    "name": "Sai vignesh",
    "age": 35, # integer without double quotes
    "is that true" : True,
    "marks" : 95.3,
    "subjects": ["English", "Physics", "Maths", "Biology"],
    "What are the page numbers" : (32, 24, 44, 50)
}
print(type(info), info)
# output: <class 'dict'>  {'key': 'value', 'name': 'Sai vignesh', 'age': 35, 'is that true': True, 'marks': 95.3, 'subjects': ['English', 'Physics', 'Maths', 'Biology'], 'What are the page numbers': (32, 24, 44, 50)}
# even dictionaries are mutable, and can be changed. 
# NOTE: IN DICTIONARIES, THE "VALUE" SIDE CAN BE ANY DATA TYPES (MUTABLE AND IMMUTABLE), WHEREAS, THE "kEY" SIDE, SHOULD BE JUST THAT DATA TYPE, THAT ARE IMMUTABLE (NOT CHNAGING), SUCH AS LISTS CANNOT BE ON "KEY" SIDE
# Also, duplicate "keys" cannot be created
print(info["name"])
print(info["age"])
print(info["marks"]) # why you access some keys, that are not inside the dictonary (you have not provided), then it pops error
info["age"] = 28 # now the age will be chnaged to 28 in the output when you print
print(info)\
# you can also add null dictonary and then later you can add the keys and values
null_dict = {}
print(null_dict) # Output: {}
null_dict["name"] = "Preethi"
null_dict["country"] = "Afganisthan"
null_dict["Birthplace"] = "Ranibennur"
print(null_dict)
# Nested Dictionaries : Dictoionary ke andar dictionary
student = {
    "name": "Rahul",
    "Subjects": {
        "Maths": 97,
        "Chemistry": 58,
        "Biology": 30,
    },
    "Age": 20,
    "Places visited": {
        "Kanyakumari": 1995,
        "Marthandam": 1996,
        "Pillayar": 2000
    },
    "Rahul end date": "26th April 2026"
    }
X = print("X=", len(student), student) # len() specifies the number of global "keys" of the dict
print(student["Subjects"])
print(student["Places visited"]), 
# When you are printing the "keys" of the students, the nested "keys" would not come
print(student.keys()) #output: dict_keys(['name', 'Subjects', 'Age', 'Places visited', 'Rahul end date'])
print(student.values())#output: dict_values(['Rahul', {'Maths': 97, 'Chemistry': 58, 'Biology': 30}, 20, {'Kanyakumari': 1995, 'Marthandam': 1996, 'Pillayar': 2000}, '26th April 2026'])
# you can also typecast the output as list
print(list(student.values())) #output: ['Rahul', {'Maths': 97, 'Chemistry': 58, 'Biology': 30}, 20, {'Kanyakumari': 1995, 'Marthandam': 1996, 'Pillayar': 2000}, '26th April 2026']
# in the above output, dictionaries such as "subjects", and "places visited" are stored inside a list
# pp = list(student.values())
# print("pp =", pp)
# NOTE: Dictionary methods, (dict.keys()) - provides the output of as the dictionary of keys, similarly, the (dict.values()) for the values dictionary output
# NOTE: for the dictionary's (keys, values) pairs as tuples to be returned: dict.items()
pairs = student.items()#output: dict_items([('name', 'Rahul'), ('Subjects', {'Maths': 97, 'Chemistry': 58, 'Biology': 30}), ('Age', 20), ('Places visited', {'Kanyakumari': 1995, 'Marthandam': 1996, 'Pillayar': 2000}), ('Rahul end date', '26th April 2026')])
# to return the value of that particular key, then ; dict.get("key")
Programming_languages = ["java", "python", "CSS"] # this is a list
print(type(Programming_languages[0]))
print(Programming_languages[0])
Programming_languages.append("SaiVignesh")
print(Programming_languages)
print(student['name']) # this already gives the output Rahul, but in case, if i write name2, instead of name, it throws a error
# print(student['name2']) # output as #Error
print(student.get('name2')) # remember x.get(), and here it gives the output as "None"
pair2 = list(pairs)
print(pair2[0]) #now this is a pair of tuple, and it can just be accessed, but not changed. If you have to change in this, you have to convert pair2[0] as a list, and then chnage it, and then convert back to the tuple
print(type(pair2)) # this is a list
print(type(pair2[0])) # this is a tuple
# X.update(new parameter to update) - inserts the specified items to the dictionary
# NOTE: Sets in python: set is a collection of unordered items. Each element in the set must be unique and immutable
# if there is a nums = {1, 2, 2, 2}
print(student["name"])
print(student.get("name")) # method, so even if I change the string which does not exist in the dictionary, then it will not show error, but simply will show None
#myDict.update(newDict) - inserts the specified items to the dictionary
student.update({"city":"Delhi", "terminator": "2"}) 
print(student) #Output : {'name': 'Rahul', 'Subjects': {'Maths': 97, 'Chemistry': 58, 'Biology': 30}, 'Age': 20, 'Places visited': {'Kanyakumari': 1995, 'Marthandam': 1996, 'Pillayar': 2000}, 'Rahul end date': '26th April 2026', 'city': 'Delhi', 'terminator': '2'}
#Set is a collection of unordered items. Each element is a set and must be unique and mutable. You can store anything inside the set - int, boolean, float, str, tuple. since these are immutable. But you cannot store 
# lists and dictionaries, since they are mutable. also, set is written inside {} as dictionary, which is written inside {}
# difference between dictionary and the sets are: Dictionaries has keys and values, while sets can be a set of different data types stored inside the flower bracket 
collection1 = {1, 2, "Hello", "data", "data", "hello", 2, 1}
print(type(collection1), collection1) # sets ignore the duplicate (ignore repetetion, while printing the sets) # output:<class 'set'> {1, 2, 'hello', 'data', 'Hello'}
# how to create a empty set
collection = {} # this is a empty dictionary, not a empty set. For empty set, you have to write collection1 = set()
collection = set() # this is a empty set
# Methods of sets
# set.add() # sets are mutable (elements can be added and removed), but the elements of the sets are immutable.
collection.add("3")
# collection.remove("hello")
# collection.remove("3")
# print(collection)

# nums = [1, 2, 3, 4]  
# for num in nums:
#  if num == 2:
#     print("found bitch")
#  else:
#     print("loop completed")
# a = [1, 2, 3]
# b = a
# a = a + [5]
# print(b) # output will be [1, 2, 3]
collection.add((1, 2))
# print(type(collection), collection)
# for item in collection:
#     print(type(item))
# collection.add([1, 2, 3]) #TypeError: cannot use 'list' as a set element (unhashable type: 'list') (Inside, we are trying to add the list, which is mutabele)
collection.clear()

print(len(collection)) #0
#NOTE: Loops: for loop and while loop: Repeat of instructions
count = 1 # § the count is a variable called iterators, and the process inside the loop is called iterations
while count <= 5: # The output willb be Hello (5 times) # and this condition is stating that run until count is <=5, but with =out the limit condition below, the action will be true, and it runs infinte times
    print("Hello", count) # infinite Hello. and since its infinite, to reduce it, we provide a value as count
    count = count + 1 # this is the line, that provides the limit. and if it is deleted, then the action (print), will print infinite times
    
# print("loop end hogaya bhai, nikal")
# i = 1 # this task is to print from 1 to 100 
# while i <=100:
#     print(i)
#     i = i + 1
# i = 1
# while i <=100:
#     print(i)
#     i = i + 1
# n = int(input("Enter the number: "))

# i = 1
# while i <= 10:
#     print(n*i)
#     i +=1

# Question 4
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 1
while idx < len(nums):
    print(nums[idx])
    idx += 1

# traverse: going deep into each tupple, Dictionary. # Task: find the specific number from the tupple
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
while i<len(tup):
    if (tup[i] ==x):
        print("found at idx", i)

    else:
        print("finding...") # it keeps on finding even after finding the digit, and finds until the tupples end, unless you break the loop, so, to break the loop, we use the break statement
    i +=1
    