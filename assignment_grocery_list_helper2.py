# Assignment to write a Grocery List Helper. The user will be able to enter their name and a list of grocery items.

# message welcoming the user to the program
print("Welcome to Whole Foods!")

# Asking the user for their first name and storing it in a variable
customer_first_name = input("What is your first name? ")

# Asking the user for their last name and storing it in a variable
print("Welcome, " + customer_first_name + ".")

# Print a message thanking the user that includes their first and last name
customer_last_name = input("May I get your last name as well? ")
print("Thank you "+ customer_first_name + " " + customer_last_name +"?")

# Asking the user for a list of their groceries and storing it in a variable
print ("It is now time to take your order. You must order a minimum of 5 items.")

grocery_item_one = input("Please enter your first item. ")

grocery_item_two = input("Please enter your second item. ")

grocery_item_three = input("Please enter your third item. ")

grocery_item_four = input("Please enter your fourth item. ")

grocery_item_five = input("Please enter your fifth item. ")

grocery_list = grocery_item_one + ", " + grocery_item_two + ", "  + grocery_item_three + ", "  + grocery_item_four + ", "  + grocery_item_five 

print(grocery_list.lower())

output = (customer_first_name + " " + customer_last_name + ": {4} {3} {2} {1} {0}".format(grocery_item_one, grocery_item_two, grocery_item_three, grocery_item_four, grocery_item_five))

print(output)