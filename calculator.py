print('Welcome to my basic Calculator. ')
print("\t1    -   Addition.")
print("\t2    -   Subtraction.")
print("\t3    -   Multiplication.")
print("\t4    -   Division.")

print("Choose a type what calculation do you want to perform ? ")
choice = int(input("Enter your type for calculation ? "))

if choice == 1:
    n1 = int(input("Enter your first number: "))
    n2 = int(input("Enter your second number: "))
    print(f"Addition is {n1+n2}")
    
elif choice == 2:
    n1 = int(input("Enter your first number: "))
    n2 = int(input("Enter your second number: "))
    print(f"Subtarction is {n1-n2}")

elif choice == 3:
    n1 = int(input("Enter your first number: "))
    n2 = int(input("Enter your second number: "))
    print(f"Miltiplication is {n1*n2}")

elif choice == 4:
    n1 = int(input("Enter your first number: "))
    n2 = int(input("Enter your second number: "))
    print(f"Division is {n1/n2}")

else: 
    print("Invalid selection. Please select correct type.")
