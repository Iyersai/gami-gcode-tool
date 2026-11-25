print("helloworld")
print('printme') # you can enter both single appostropfy, and double qutation for the print function
#Variable is a container for a value (string, interger, float, and boolean)
#Float is a number that contains decimal point succh as 3.14, 0.0, -27.25
#Real world float value inclued 
#weitght = 14.65kg
#temperature = 13.5 deg c
#A boolean is a data types that can have only two values (true or false)
#a bloolean is a logic state
# A string (str) is a data type, that is used to represent the text. even this is written inside the qutation mark.
# in the print function, the word inside the qutation mark is the string
first_name = "Sai Vignesh" #here, the equal to mark is the assignment operator, and Sai Vignesh is the variable (string(str))
print("first_name")
#print(f"{first_name}bro") #f-string is a cleanest way to insert variables, calculation and numbers inside the text string
first_name = "Sai Vignesh Iyer" #this is a string
number_of_apples = "45" # this is not an integer, and it is a string, since, it is inside the quoatation
print(f"{first_name} ate {number_of_apples}")
food = "pizza" #this is a string
f = print(f"{first_name} bro, do you like {food}?")
email = "saivigneshiyer1234@gmail.com" #this is a string
print(f"{email}")
# basically, string is a series of character, that can have any values, texts etc
#Interger are pure number, without decimals. Integers, should not be inside the quates
age = 25
item = "apples"
quantity = 12
num_of_students = 30 
g = print(f"{first_name} is of {age} years old, ate {quantity} {item} without giving to {num_of_students} students")
#float consits integres with decimal points
#boolean (true or false)
name_stududent = "Sai Vignesh" #name_student is the variable, and the sai vignesh inside the quotation is the string


if name_stududent:

    print(f"{item} are none")
else:
    print(f"{item} is not none")
#Typecasting which is used to convert from one data type to another data type
name = "bro"
age = 21
gpa = 1.9
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))
age = float(age)
print(type(age))
gpa = int(round(gpa))
print(gpa)
student = str(student) # this is the built_in variable conversion function (type casting) 
print(student) # now for this output, True is treated as a string, rather than a boolean
# whent it is simply \\student = TRUE, print(type(student))//, the output will be a 'boolean'
# now lets check if the True output from last is string?
print(type(student)) #boom it is a string
age = bool((age))
print(age) 
print(type(age)) # here age is a boolean instead of integer, since we changd it using the variable changing function
# so, for the boolean, every number or integer will be TRUE, unless it is 0(ZERO)
name = bool((name))
print(name) 
print(type(name)) # even here, name is consodered as TRUE and boolean, since there is something
# that is filling up the space, even a space inside the quatation mark will be TRUe, and if it is not
# there it is FALSE.
# until here, we saw explicit typecasting, while now llets see implicit type casting
#Explicit is manually converting the data types by using the casting keywords
# Implicit type casting is where a datat type is converted to another data type automatically
x = 2
y = 2.0
x = x-y
print(x)# here, x(the output) is the float (since, x is integer, and y is float, the output takes as a float)
# this happens during performing arithematic operations
# next topic: User Input accepting using the function input()
name = input("Enter your name:") # when we accept any input, it will always be on the string data type
age = input("Enter your age")
print(f"Hello {name}")
print(f"you are {age} years old")
print("Thank you for letting me know your age")

