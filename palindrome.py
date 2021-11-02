list2 = []
n = int(input("Enter number of cases: "))
for i in range(n):
	x = int(input("Enter number after closest palindrome value you want: "))
	list2.append(x)
list1 = []
for i in list2:
	while True:
		i = str(i)
		b = i[::-1]
		if i == b:
			list1.append(b)
			break
		i = int(i)
		i += 1

# for i in list2,list1:
# 	print(f"Next palindrome for {list2[i]} is {list1[i]}")
w = 0
for i in list2:
	print(f"Next palindrom for {list2[w]} is ", end="")
	k = 0
	for i in list1:
		print(list1[k])
		k += 1
	w += 1