'''
Practicing with Integer Division and Modulus
    
    Task: Organize a classroom into groups.
    
    Challenge: You have 23 students and need to divide them into groups of four.
    Use integer division to find how many full groups you can form, and the modulus 
    operator to determine how many students will be left without a group. Print both results.
'''

# define variables
students = 23
group_size = 4

# calculations
students_per_group = students // group_size

# print results
print(f'Number of groups: {students_per_group}')
print(f'Number of students remaining: {students % group_size}')
