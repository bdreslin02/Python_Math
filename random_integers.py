# Brandon Dreslin - SPC ID# 2414755; COP1000 # 4228; Module 7 Preparation Assignment 

# random_integers.py
# Program Description: Given a list of twelve randomly generated integers: (a)create a list that stores these integers, (b) tell the user the fourth element, (c) the number at index 9, (c) the smallest number in the list.
    # Using a second function, (d) slice the middle six numbers, (e) determine the new list's size, and (f) sort this list in ascending order. Display all outputs to the user. 

# Before defining the 'main' function, import the 'random' module as 'ra' ➞ Importing as a different name will increase efficiency when writing this program's code and will make it easier to read when debugging, for example.
# Start program.
    # Print a statement telling the user that a list of random numbers will appear on screen from which the program's executable statements will run.    # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output.
    # Create an empty list for which the twelve random integers will be stored by placing two brackets next to each other. Assign to variable 'nums.'
    # For any number 'n' in the range of twelve numbers:
        # Call the 'append' method for empty list 'nums' and create random integers between fifty and one hundred using the 'randint' function for the 'ra' module.
    # For any number 'n' in list 'nums':
        # Print 'n' on one single line, separated by a single space ➞ This process avoids the so-called 'crude dump,' which is usually not good practice when creating programs, especially ones with numbers.
    # Print a single space in between the previous and following statements ➞ This ensures that the two lines of code are separated and will not appear on the same line.
    # Print a statement telling the user which integer is the fourth element in the randomly generated list by indexing the fourth element (which happens to be index three because indexing always starts at zero for any list).
    # Print a statement telling the user which integer is located at index nine in the randomly generated list by indexing the ninth number (this is NOT an element, so the 'one less' rule does not apply).
    # Print a statement telling the user which integer is the smallest in the randomly generated list by using the 'min' function for list 'nums.'
    # Call the 'change_list' function for the argument 'nums.' Assign to variable 'new_list.'
    # Print a statement telling the user that the 'change_list' function sliced, sorted, and returned a new list ➞ Second function 'change_list is shown.
    # OPTIONAL CODE: Print a visual separating barrier between the previous and following lines of code, so that it is easier for the user to interpret the program's data output.
    # For any number 'n' in list 'new_list':
        # Print 'n' on one single line, separated by a single space ➞ This process avoids the so-called 'crude dump,' which is usually not good practice when creating programs, especially ones with numbers.
# Define second function 'change_list' for parameter 'nums':
    # Slice the middle six numbers of list 'nums' by using the range from index three to index nine. Assign to variable 'middle_six.'
    # Determine the size of new list 'middle_six' by using the 'len' function for this list. Assign to variable 'size.'
    # Print a statement telling the user that the size of the new list is the size which was determined in the previous statement ➞ A size of six might not be true every time - the code can be changed to slice different numbers out.
    # Sort list 'middle_six' in ascending order by calling the 'sort()' method.
    # Return list 'middle_six' to 'main.'
# End program. 
    
# Import the 'random' module as 'ra' ➞ This function is responsible for generating the random integers necessary for this program to run.
import random as ra

def main():
# Display a message to the user telling them that a list of random integers will follow. 
    print('Here is a list of random integers...')
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
    print('------------------------------------')
# Create an empty list that will later store the random integers. 
    nums = []
# Use a 'for' loop with the range function to write 12 random integers into the empty list. 
    for n in range(12):
# Call the 'append' function for the list and write random integers all between 50 and 100. 
        nums.append(ra.randint(50, 100))
# Use a 'for' loop to display the random integers within the list's contents ➞ This flow control statement will avoid 'crude dumping.'
    for n in nums:
# Display each integer on a single line, separated by a single space. 
        print(n, end = ' ')
# Display a space between the previous and following statements so that each get separated and do not appear on the same line together.       
    print()
# Display a statement telling the user which integer in the list is the fourth element. 
    print('The fourth element in this list is', nums[3])
# Display a statement telling the user which integer in the list is located at index 9. 
    print('The element at index 9 is', nums[9])
# Display a statement telling the user which integer in the list is the smallest. 
    print('The smallest element in the list is', min(nums))
# Call the 'change_list' function for argument 'nums' in 'main' by assigning it to a new variable. 
    new_list = change_list(nums)
# Display a statement telling the user that function 'change_list' returned the following list.
    print('change_list returned this sorted list...')
# OPTIONAL: [Display a separating barrier to make the data easier to read for the user.]
    print('------------------------------------')
# Use a 'for' loop to display the 6 random integers within the new list's (shown in 'change_list') contents.
    for n in new_list:
# Display each integer on a single line, separated by a single space. 
        print(n, end = ' ')
# Define a new function called 'change_list' for parameter 'nums.'
def change_list(nums):
# Slice the middle 6 integers from list 'nums' ➞ This will use the range from index 3 to index 9.
    middle_six = nums[3:9]
# Determine the size of this new list by calling the 'len' function to the list. 
    size = len(middle_six)
# Display a statement telling the user what the size of the list was determined to be. 
    print('The size of this list is now', size)
# Sort this list by calling the 'sort()' method for list 'middle_six.'
    middle_six.sort()
# Return this sort to 'main,' which will execute when 'main' reads the 'change_list' contents. 
    return middle_six

# Call the 'main' function to end the program. 
main()
