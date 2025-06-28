'''
Using Basic Operators
    Task: Manage a shopping budget.
    Challenge: You have a budget of $100. Subtract the cost of items worth 
               $25, $15, and $30 and display how much of the budget remains.
'''

# define variables
budget = 100
item1 = 25
item2 = 15
item3 = 30

# calculation
remaining_budget = budget - (item1 + item2 + item3)

# calculation 2 (cleaner)
budget -= 25
budget -= 15
budget -= 30

# print the result
print(f'The remaining amount is: ${remaining_budget}')
print(f'The remaining amount is: ${budget}')