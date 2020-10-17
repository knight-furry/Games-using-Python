import random
count = 10
(point1, point2, point3) = (0, 0, 0)
lst = ["snake", "water", "gun"]
print("\n**************** Welcome to Snake_Water_Gun Game *****************")
print("There only 10 matches to play")
name = input("Please enter your name : ")
while(count != 0):
    choice = random.choice(lst)
    print("\nYour choices are: ", lst)
    user = input("Enter your choice from given list :")
    user = user.lower()
    if user in lst :
        if choice == user:
            print("This match is draw, Play again....!")
            point3 += 1
        else:
            if (user == "snake" and choice == "water") or (user == "water" and choice == "snake"):
                if user == "snake" and choice == "water":
                    print("The",name,"won the match....!")
                    point1 += 1
                   # print("The score of", name, "is", point1, "and score of computer is", point2)
                else:
                    print("The Copmuter won the match....!")
                    point2 += 1
                   # print("The score of", name, "is", point1, "and score of computer is", point2)
            elif (user == "gun" and choice == "water") or (user == "water" and choice == "gun"):
                if user == "water" and choice == "gun":
                    print("The",name,"won the match....!")
                    point1 += 1
                   # print("The score of", name, "is", point1, "and score of computer is", point2)
                else:
                    print("The Copmuter won the match....!")
                    point2 += 1
                   # print("The score of", name, "is", point1, "and score of computer is", point2)
            else:
                if user == "gun" and choice == "snake":
                    print("The",name,"won the match....!")
                    point1 += 1
                   # print("The score of", name, "is", point1, "and score of computer is", point2)
                else:
                    print("The Copmuter won the match....!")
                    point2 += 1
                   # print("The score of", name, "is", point1, "and score of computer is", point2)
        count -= 1
        print("You left only", count,"chances.....!")
    else:
        print("Invalid input, Try again.....!")
print("\n\nThe score board is:")
print("Computer :", point2)
print(name, " :", point1)
print("Draw matches :", point3)
if point1 > point2:
    print("The winner is : ", name)
elif point1 < point2:
    print("The Computer is winnwr....!")
else:
    print("Result is NOT found...!")