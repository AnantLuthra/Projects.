
def receipt_generator():
    items = []
    prices = []
    print("Enter the name of item and price seperating each other by a '-' eg- 'Tomato-56'")
    print("Enter 'q' at the place of items to stop item adding in receipt")
    try:
        while True:
            a = input()
            if a == 'q':
                break
            else:
                items.append(a)

        print("Anant Kirana Store\n")
        for item in items:
            b = item.split("-")
            item = b[0]
            price = b[1]
            prices.append(price)
            print(f"Item = {item}, {price}")
        n = 0
        for item in prices:
            item = int(item)
            n += item
        print(f"Total = {n}\n")
        if n > 0:
            print("Thanks for doing shopping from our shop :)")
    except Exception as e:
       print("Oops! Something went wrong !!")


print("Welcome to Receipt Generator.")
receipt_generator()
