# You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. Naturally, you would like to find out the house number of the people on the other side of the street. The street looks something like this:
# 1|   |6
# 3|   |4
# 5|   |2

# Evens increase on the right; odds decrease on the left. House numbers start at 1 and increase without gaps. When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.

# Given your house number address and length of street n, give the house number on the opposite side of the street.

# My_Code
def over_the_road(address, n):
    address = 1
    total_house = n*2
    if n == 3:
        print('1|', '|6\n3|', '|4\n5|', '|2', sep='\t')
    else:
        while n < total_house:
            if address % 2 == 0:
                print(str(total_house)+'|', '|'+str(address)+'\n', sep='\t')
                total_house = total_house-1
                address = address+1
            else:
                print(str(address)+'|', '|'+str(total_house)+'\n', sep='\t')
                total_house = total_house-1
                address = address+1


over_the_road(3, 3)
