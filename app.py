print("hello world") # Print statement

# Variable assignments (Correct Syntax)
a = 30
b = 20
c = True        # Boolean type
d = 3 + 5j      # Complex type
e = (1, 2, 30)  # Tuple type
f = [1, 23, 3, 4] # List type

# Basic operations and type checks
print(a + b)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# Corrected Function Definition
def app():
   # Variables local to the function
   a = 20
   b = 30
   print(a + b)  # Calculation 1
   c = 40
   d = 50
   print(c * d) 
   e = 66
   f = 77
   print(e / f)  
app()
temp = int(input("enter your temperature: "))
if(temp < 32):
    print("it is cold temp")
elif temp == 32:
    print("it is normal temp")
else:
    print("it is warm temp")