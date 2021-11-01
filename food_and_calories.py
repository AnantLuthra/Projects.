# You have to reverse a list by the following ways...
# 1: Inbuilt method of python.
# 2: list_name[::-1] slicing trick
# 3: Swapping first element with last one and second element with second last
#    one and so on..

# OUTPUT
# [1,3,4,3]
# [1,3,4,3]
# [1,3,4,3]
# all the three methods give same results...

food = []
print("Enter the elements of list and for quitting enter q")
while True:
    element = input()
    if element == "q":
        break
    food.append(element)

def food_printer(func):
    def mixer():
        print(f"Before {food}")
        func()
        print(f"After {food}")
    return mixer()

@food_printer
def food_reverse_by_inbuilt_module(list):
    list.reverse()

@food_printer
def food_reverse_by_slicing(list):
    list[::-1]
    
# First using inbuilt method..
food_reverse_by_inbuilt_module(food)

# by slicing trick..
food_reverse_by_slicing(food)

# Exchanging first elements with respect to their last one...

