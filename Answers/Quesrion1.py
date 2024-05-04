# Question 1: Write a program to accept user input, convert into an integer and check whether it is a leap year

def leapYearCheck(x):
    result = ["Is not a leap year", "Is a leap year"]
    if x % 4 == 0:
        if (x % 100 == 0) and (x % 400 != 0):
            return result[0]
        else:
            return result[1]
    else:
        return result[0]

def run():
    runCheck = True
    def yearIn():
        year_in = int(input("Please enter the year:"))
        print("The year \"",year_in,"\":",leapYearCheck(year_in))
    yearIn()
    while runCheck:
        cont_in = input("Do you want to continue? (Y/N)")
        if cont_in == "N":
            runCheck = False
            print("Have a great day!")
        elif cont_in != "Y":
            print("Invalid input! Please try again.")
        else:
            yearIn()
        
run()
        