# print("hello world") # Print statement

# # Variable assignments (Correct Syntax)
# a = 30
# b = 20
# c = True        # Boolean type
# d = 3 + 5j      # Complex type
# e = (1, 2, 30)  # Tuple type
# f = [1, 23, 3, 4] # List type

# # Basic operations and type checks
# print(a + b)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# # Corrected Function Definition
# def app():
#    # Variables local to the function
#    a = 20
#    b = 30
#    print(a + b)  # Calculation 1
#    c = 40
#    d = 50
#    print(c * d) 
#    e = 66
#    f = 77
#    print(e / f)  
# app()
# temp = int(input("enter your temperature: "))
# if(temp < 32):
#     print("it is cold temp")
# elif temp == 32:
#     print("it is normal temp")
# else:
#     print("it is warm temp")
# student = ["ram", "shyam", "hari"]
# for i in student:
#     if(i == "ram"):
#          print("found the name")
#     else:
#          print("name not found")
# teacher = ["anil", "sunil", "rahul"]
# teacher = ["anil", "sunil", "rahul"]
# for i in teacher:
#     if(i == "sunil" or i == "rahul" or i == "anil"):
#          print("found the name")
#     else:
#          print("name not found")
# 1. Get user input (The input is a string, so we don't convert it to int)
search_text = input("Enter the name of a company to check: ")

# 2. Define the tuple of companies
company_names = ("wipro", "philips", "halonix", "crompton", "havels", "panasonic")

# 3. Check if the user's input is *in* the tuple
if search_text in company_names:
    print(f" Found the name: '{search_text}' is in the list of companies.")
else:
    print(f" Name not found: '{search_text}' is NOT in the list of companies.")
