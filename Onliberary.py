import time


def getdate():
    return time.asctime()


class Library:
    # list_of_books = ["S.Sc. All in one", "Maths R.D. Sharma", "D.K.", "Maths N.C.E.R.T."]

    def __init__(self, book_list, library_name):
        self.list_of_books = book_list
        self.library_name = library_name

    def display_book(self):
        print("Displaying...")
        time.sleep(1)
        return f"{self.list_of_books}\n"

    def lend_book(self):
        name = input("Enter your name: ")
        name_of_book = input("Enter the name of book which you want to borrow: ")
        if name_of_book not in self.list_of_books:
            print("Book not available !! or incorrect book name entered !!")
        else:
            print("Borrowing..")
            with open("online_library_log_file.txt", "a") as k:
                k.write("\t\t[Lending book]" + "\n" + name + ", " + name_of_book + ": " + str([str(getdate())]) + "\n" + "------------------------------" + "\n")
            self.list_of_books.remove(name_of_book)
            time.sleep(1)
            return "Successfully borrowed.."
        return ""

    def add_book(self):
        name = input("Enter your name: ")
        name_of_book = input("Enter the name of book which you want to add: ")
        print("Adding...")
        with open("online_library_log_file.txt", "a") as m:
            m.write("\t\t[Book added]" + "\n" + name + ", " + name_of_book + ": " + str([str(getdate())]) + "\n" + "------------------------------" + "\n")
        time.sleep(1)
        self.list_of_books.append(name_of_book)
        return "Successfully added..\n"

    def return_book(self):
        name = input("Enter your name: ")
        name_of_book = input("Enter the name of book which you want to return: ")
        print("Returning...")
        with open("online_library_log_file.txt", "a") as h:
            h.write("\t\t[Book returned]" + "\n" + name + ", " + name_of_book + ": " + str([str(getdate())]) + "\n" + "------------------------------" + "\n")
        time.sleep(1)
        self.list_of_books.append(name_of_book)
        return "Successfully returned.\n"


if __name__ == '__main__':
    print("Welcome to online library system. Create your own online library within seconds.")
    time.sleep(.5)
    list_of_books = ["S.Sc. All in one", "Maths R.D. Sharma", "D.K.", "Maths N.C.E.R.T."]
    a = input("Enter your library name: ")
    school = Library(list_of_books, a)
    while True:
        clear = ''
        print("1: List of all books\n2: Lending book\n3: Adding book\n4: Returning book\n5: History")
        inp1 = input("6: For Exiting\n7: Clear history\n")
        if inp1 == '1':
            print(school.display_book())
        elif inp1 == '2':
            print(school.lend_book())
        elif inp1 == '3':
            print(school.add_book())
        elif inp1 == '4':
            print(school.return_book())
        elif inp1 == '6':
            bye = "Thanks for using our online library..."
            i = 1
            a = 0
            for j in range(2):
                for item in bye:
                    print(bye[a:i], end="")
                    i += 1
                    a += 1
                    time.sleep(.2)
                print()
                i = 1
                a = 0
            print()
            break
        elif inp1 == '5':
            password = input("Enter password: ")
            if password == 'baby likes BASS':
                with open("online_library_log_file.txt", "r") as f:
                    if f.read() == '':
                        print("Log file empty..\n")
                    else:
                        with open("online_library_log_file.txt", "r") as g:
                            print(g.read())
            else:
                print("Incorrect password entered !!!")
        elif inp1 == '7':
            password = input("Enter password: ")
            if password == 'baby likes BASS':
                with open("online_library_log_file.txt", "w") as u:
                    u.write(clear)
                print("Log file cleared..\n")
            else:
                print("Incorrect password entered !!!")

        else:
            print("Invalid input !!! Try again !!\n")

        time.sleep(.5)
