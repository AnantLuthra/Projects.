try:
    n = int(input("Enter the number of apples harry have..\n"))
    mn = int(input("Enter the lower value of range: "))
    mx = int(input("Enter the upper value of range: "))
except Exception as e:
    raise ValueError("You haven't entered required values..")

for i in range(mn, mx+1):
    a = n % i
    if a == 0:
        print(f"{i} is divisor of {n}")
    elif a != 0:
        print(f"{i} is not a divisor of {n}")
    else:
        pass
    