# Challenge_1

squares = [1, 4, 9, 16, 25]
# print(squares[-3]:)
# What is the output of this code?

# My_Solution
# What is the output of this code?
# Answer=9
# Checks
print(squares[-3:])

# Explain
# Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type. Like strings (and all other built-in sequence type), lists can be indexed and sliced.

# Challenge_2


def srange(x):
    return range(x-3, x)


s = 0
for i in srange(2):
    s += i
print(s)
