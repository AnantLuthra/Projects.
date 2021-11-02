'''
Author: Anant
Date: 2/11/21
Purpose: Practice of python..
'''
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

for i in range(n):
    print(f"Next palindrom for {list2[i]} is {list1[i]}")
