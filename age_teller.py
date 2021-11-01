
def particular_year_age_teller(year_of_born, particular_year):
    if year_of_born > particular_year:
        return "You were born in that year.."
    final_year_age = particular_year - year_of_born
    return final_year_age

def want_particular_year_age():
    opinion = input("Do you want to know your age in a particular year?\nEnter 'y' for yes and 'n' for no: ")
    if opinion == "y":
        year = input("\nSo enter that particular year: ")
        if year.isnumeric() == False:
            raise ValueError("String is not allowed !!")
        else:
            year = int(year)
            return year
    else:
        print("Ok sir...")
        return None

def age_tell(age):

    present_year = 2021
    age = int(age)
    if age < 0:
        print("You seems to be unborn yet..")

    elif age > 0 and age <= 150:
        year_of_born = present_year - age
        after_hundred_year = year_of_born + 100
        print(f"You will be of hundred years in year {after_hundred_year}\n")
        particular_year = want_particular_year_age()
        if particular_year == None:
            pass
        else:
            print(particular_year_age_teller(year_of_born, particular_year))

    elif age > 150 and age < 1900:
        print("It seems that you endless life.. ")
    
    elif age > 1900 and age < present_year:
        age += 100
        print(f"You will be of hundred years in year {age}\n")
        particular_year = want_particular_year_age()
        year_of_born = age - 100
        if particular_year == None:
            pass
        else:
            print(particular_year_age_teller(year_of_born, particular_year))

    elif age >= present_year:
        print("It seems you are unborn.. or have endless life..")

    else:
        pass
    
if __name__ == '__main__':
    age = input("Enter your age in years or number..\n")
    if age.isnumeric() == False:
        raise ValueError("String is not allowed !!")
    age_tell(age)
    