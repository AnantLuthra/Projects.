
def main_function():
    """This function basically add and remove your task from a list.."""
    to_do_list = []
    while(True):
        a = input("What you want to do?\n1- Adding elements in to do list.\n2- Have completed a task in to do list..\n3- To show to do list.\n")
        if a == '1':
            while(True):
                element = input("Enter the task which you want to add in to do list: ")
                to_do_list.append(element)
                opinion = input("Wanna add one more task then press enter otherwise enter 1: ")
                if opinion == '':
                    continue
                else:
                    break
        elif a == '2':
            while(True):
                print(to_do_list)
                remove_element = int(input("Enter the index of your task you have completed from the list: "))
                k = remove_element - 1
                l = to_do_list[k]
                to_do_list.remove(l)
                opinion2 = input("Have done one more task then press enter otherwise enter 1: ")
                if opinion2 == '':
                    continue
                else:
                    break
                
        elif a == '3':
            print(to_do_list)
        else:
            print("Invalid input try again !!")
        last = input("Wanna exit press enter otherwise enter 1: ")
        if last == '':
            break
        else:
            continue


print("Welcome to you to do list system.")
main_function()
