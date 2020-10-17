while(True):
    print("Welcome to calculator created by Datta Katkhade...!\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n6.Reminder\n.7.Exit\n")
    op = int(input("Enter your choice :"))
    if op > 0 and op < 7 :
        num1 = int(input("Enter First number : "))
        num2 = int(input("Enter Second number : "))
        if op == 1:
            print("The Addition of",num1,"and",num2,"is : ",num1+num2)
        elif op == 2:
            print("The Subtraction of", num1, "and", num2, "is : ", num1 - num2)
        elif op == 3:
            print("The Multiplication of", num1, "and", num2, "is : ", num1 * num2)
        elif op == 4:
            print("The Division of", num1, "and", num2, "is : ", num1 / num2)
        elif op == 5:
            print("The Power of", num1, "is", num2, "is equal to : ", num1 ** num2)
        elif op == 6:
            print("The Reminder of", num1, "and", num2, "is : ", num1 % num2)
    elif op == 7:
        break
    else:
        print("Invalid Option. Please enter correct option..!")
    choice = input("Do you want to continue (y/n) : ")
    if choice == 'n':
        break