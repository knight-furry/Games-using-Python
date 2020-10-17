import random

n = random.randrange(1,100)
count = 6
while(count != 0) :
    choice = int(input("Enter your Guass number : "))
    count = count - 1
    if choice == n:
        print("Congrates...! you are win.")
        exit()
    elif choice < n :
        print("Sorry number is Greater than", choice, "Try again you left only", count, "chances")
    else:
        print("Sorry number is Lesser than", choice, "Try again you left only", count, "chances")
    if count == 0:
        print(" Game over ! You Loss the Game...!")

print("The nuber is:",n)
