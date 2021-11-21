# concatenate strings
name = input("Name: ")
print("Hello, " + name)

# formatting strings
name = input("Name: ")
print(f"Hello, {name}")

# Conditions
num = int(input("Number: "))      #Note: input automatically returns a string. Need to cast to int.
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")