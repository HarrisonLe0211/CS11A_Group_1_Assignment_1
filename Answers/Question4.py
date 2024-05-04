lis = [1, 3, 5, 6, 2, 1, 3]

print("The list in ???? is : ")
for i in sorted('lis'):
    print(i, end=" ")

print("\r")

print("The list in ???????? is : ")
for i in sorted(set('lis')):
    print(i, end=" ")

print("\r")

#The first line initializes a listed named 'list' with some integers values
#3rd Print line is printing a message that indicates that the list is going to be printed a specific order.
#4th for i line iterates through characters  in the sting 'lis' after sorting them meaning is sorts character 'l', 'i', and 's'
#The 5th line prints each character from the sorted string foolwed by a space, due to the 'end=' argument in the print function. The results print characters in alphabetical order.
#The 7th line after a loop prints a carriage return at the end of the loop, effectively moving the cursor to the beginning of the current line setting it up for a subsequent output.
#The 9th line prints a messsage that indicates that the list is goint to be printed in a certain order.
#The 10th line is a loop that first creates a set of characters in the string, removing duplicates that sort the characters within  a set.
#The 11th line is inside the loop which prints each character obtained throu gh the sorted set followed by a space.
#The 13th line prints a carriage return after the loop.

#The end result is that the code prints the characters in the string 'lis' in alphabetical order first, and then prints the unique characters from the same string alphabetical order.  