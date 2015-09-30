# Program to find if a string is a palindrome or not
check = raw_input("Enter a string: ")

#reverse the input from the user
reverse = reversed(check)

#check to see if the reverse equals the original input
if list(check) == list(reverse):
