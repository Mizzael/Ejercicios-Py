# Challenge_1

squares = [1, 4, 9, 16, 25]
# print(squares[-3]:)
# What is the output of this code?

# My_Solution
# What is the output of this code?
# My_Answer=9

# Checks
print('Challenge_1')
print(squares[-3:], '\n')

# Explanation
# Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type. Like strings (and all other built-in sequence type), lists can be indexed and sliced.

# Challenge_2


def srange(x):
    return range(x-3, x)


s = 0
for i in srange(2):
    s += i

print('Challenge_2')
print(s, '\n')

# What is the output of this code?
# My_Answer=[1,2,3,4]

# Checks
# Answer=0
# Explanation
# In the puzzle we define our own range function srange(x).
# It creates a range object using the built-in range() function.
# Calling range(start, stop) returns a range object with range-values from start to stop-1.
# Therefore srange(x) returns a range from x-3 to x-1.
# When we call the function srange() with x=2 it returns a range object with the values -1, 0, 1.
# In the loop we sum up these values and get the output 0.


# Challenge_3

x = 50//11

print('Challenge_3')
print(x)
