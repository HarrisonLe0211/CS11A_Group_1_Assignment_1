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
        



