# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.
# Note: The function accepts an integer and returns an integer

# My Code
def square_digits(num):
    words = list(str(num))
    for word in words:
        print(int(word)**2, end=" ")


square_digits(12345)

# (list(map(int, str(num))))
