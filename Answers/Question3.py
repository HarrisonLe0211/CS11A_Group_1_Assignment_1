# Question 3: Write a program to accept user input, convert into an integer find the factorial using both 'for' and 'while' loops in the same program. (2 methods)
#             The program should continue to promt the user for a new number and print the factorial output until the user hits a vulae of 0, 
#             in which case the program should exit the while loop and terminate execution.

def factorialCheck(num):
    factorial = 1
    if num >=0:
        if num == 0:
            return 1
        else:
            for i in range(1, num+1):
                factorial = factorial * i
    else:
        factorial = "Not available"
    return factorial

def run():
    runCheck = True

    def numIn():
        num_in = int(input("Please enter the number:"))
        print(factorialCheck(num_in))
    
    numIn()

    while runCheck:   
        cont_in = input(("Do you want to continue? (Y/N)"))
        if cont_in == "N":
            print("The program will now be terminated. Have a great day!")
            runCheck = False
        elif cont_in != "Y":
            print("Please try again")
        else:
            numIn()

run()
        



