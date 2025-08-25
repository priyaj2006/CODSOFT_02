def add(A,B):
    return A+B
def subtract(A,B):
    return A-B
def multiply(A,B):
    return A*B
def divide(A,B):
    if B == 0:
        return "Error! Division by zero."
    return A/B

print("\n---Calculator---")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("Divide")
print("Exit")
choice=input("Enter your choice:")
if choice == '5':
    print("Exiting Calculator")
    'break'

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if choice == '1':
  print("Result:", add(num1,num2))
elif choice == '2' :
  print("Result:", subtract(num1,num2))
elif choice == '3':
  print("Result:", multiply(num1,num2))
elif choice == '4':
  print("Result:", divide(num1,num2))  
else:
  print("Invalid input,please try again.")    
    

  