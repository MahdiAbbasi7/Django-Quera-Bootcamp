"""
Generators in python.
"""
"""Without generators and memory errors is raised."""
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

"""By generators in python and without memory error."""
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row


"""Create infinite functions by generators and without memory error."""
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

"""
Palindrome functions by generators and without memory error.
Palindrome is number such as : 121 , 11 , 33, 101101
"""

def is_palindrome(num):
    # for every single-digit number.
    if num //10  == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
    
    if num == reversed_num:
        return num
    return False

for i in infinite_sequence():
    pal = is_palindrome(i)
    if pal:
        # print(i)
        pass

"""Generator comprehension."""
even = (x for x in range(10) if x%2 == 0) # Lazy Evalations
print(list(even))