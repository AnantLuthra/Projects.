import datetime
print("Hi! I am you Water Assistant !")
clear = input("Starting new day press enter for clearing old stuff.. and not then press 1: ")
anticlear = ''
if clear == '':
    with open("Waterdate.txt", "w") as f:
        f.write(anticlear)
    with open("waterdetail.txt", "w") as f:
        f.write(anticlear)
    print("Data cleared now start you newly fresh day...:))")
else:
    pass
def time():
    """to get date and time """
    date = datetime.datetime.now()
    return date

with open("waterdetail.txt", "r") as f:
    # just for printing previous value
    content = f.read()
with open("waterdate.txt", "r") as f:
    date1 = f.read()
    # pahaile se hi number of glasses and date print karva di
    print(f"Previous info..\nNumber of glasses of water = {content}\nTime = {date1}\n")

order = input("Press enter to log to close press 1: ")
if order == '':
    units = int(input("Enter the number of units of water you have consumed: "))
    with open("waterdetail.txt", "r+") as f:
        # for taking older value to do + with new one
        content1 = f.read()
    if content1 == '':
        with open("waterdetail.txt", "w") as f:
            f.write(str(units))
        with open("waterdate.txt", "w") as f:
            # ye wale with open me datetime write karne ke liye
            f.write(str([str(time())]))
            print("Successfully written!!")
    else:
        with open("waterdetail.txt", "w") as f:
            # value jodkar dubara se usi file me overwrite kar diya:))
            main = int(content1) + units
            f.write(str(main))
        with open("waterdate.txt", "w") as f:
            # ye wale with open me datetime write karne ke liye
            f.write(str([str(time())]))
            print("Successfully written!!")
        with open("waterdetail.txt", "r") as f:
            # just for printing previous value
            content = f.read()
            print(f"\nTotal unit consumed--{content}")
else:
    print("Ok closing...")