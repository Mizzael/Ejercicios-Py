# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.
# Note: The function accepts an integer and returns an integer

# My Code
def square_digits(num):
    my_num = str(num)
    for i in my_num:
        i**2
    return i


square_digits(34)
