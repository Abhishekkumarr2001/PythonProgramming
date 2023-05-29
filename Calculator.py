def add(num1,num2):
    return num1+num2

def multiply(num1,num2):
    return num1*num2

def subtract(num1,num2):
    return num1-num2

def divide(num1,num2):
    return num1/num2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

wannago=True
while wannago:
    num1=float(input("enter any number : "))
    operation=input("enter the operation : ")
    num2=float(input("enter another number : "))
    answer1=operations[operation](num1,num2)
    print(answer1)

    choice=(input("Do you wanna \n1.continue with Answer \n2.Restart \n3.exit? : "))
    
    if choice=="1":
        operation=input("enter the operation : ")
        num3=float(input("enter another number : "))
        answer2=operations[operation](answer1,num3)
        print(answer2)
    elif choice=="2":
        continue
    elif choice=="3":
        wannago=False