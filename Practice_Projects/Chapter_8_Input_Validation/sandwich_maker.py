# Sandwich Maker Page 198 Chapter 8
import pyinputplus as pyip

# Define the prices for each option
menu_prices = {
    'wheat': 2.00,
    'white': 2.00,
    'sourdough': 2.50,
    'chicken': 3.00,
    'turkey': 3.00,
    'ham': 2.50,
    'tofu': 2.50,
    'cheddar': 1.00,
    'Swiss': 1.50,
    'mozzarella': 1.50,
    'yes': 0.50,
    'no': 0.00,
}

# Initialize total cost
total_cost = 0.0

# Get user input for bread type
bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
total_cost += menu_prices[bread_type]

# Get user input for protein type
protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
total_cost += menu_prices[protein_type]

# Ask if the user wants cheese
want_cheese = pyip.inputYesNo("Do you want cheese? (yes/no): ")
if want_cheese == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
    total_cost += menu_prices[cheese_type]

# Ask if the user wants mayo, mustard, lettuce, or tomato
want_condiments = pyip.inputYesNo("Do you want mayo, mustard, lettuce, or tomato? (yes/no): ")
if want_condiments == 'yes':
    total_cost += pyip.inputInt("How many condiments do you want? (1 or more): ", min=1) * menu_prices['yes']

# Get the number of sandwiches
num_sandwiches = pyip.inputInt("How many sandwiches do you want? (1 or more): ", min=1)
total_cost *= num_sandwiches

# Display the total cost
print(f"Your total cost for {num_sandwiches} sandwich(s) is ${total_cost:.2f}")
