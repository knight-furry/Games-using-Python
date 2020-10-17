print("\n\n***************************** FLAMES GAME ************************")
name1 = input("Enter first name : ")
name2 = input("Enter second name : ")
n1 = name1 = name1.lower()
n2 = name2 = name2.lower()
name1 = name1.replace(" ", "")
name2 = name2.replace(" ", "")
for i in name1:
	for j in name2:
		if i==j :
			name1 = name1.replace(i,"",1)
			name2 = name2.replace(j,"",1)
			break
count = len(name1+name2)
if count > 0:
	list1 = ["Friends","Lovers","Affectionate","Marrige","Enemies","Siblings"]
	while len(list1) > 1 :
		c = count % len(list1)
		index = c - 1
		if index >= 0:
			left = list1[:index]
			right = list1[index+1:]
			list1 = right + left
		else:
			list1 = list1[:len(list1)-1]
	print("\nThe Relationship between ",n1," and ",n2," is : ",list1[0])
	print()
else:
	print("There is no relationship between these names....!")
