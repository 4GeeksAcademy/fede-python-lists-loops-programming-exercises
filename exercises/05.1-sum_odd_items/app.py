my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(list):
    total = 0
    for i in range(len(list)):
        if (list[i] % 2 != 0):
            total += list[i]
    print(total)

""" OTRA FORMA PODRIA SER 

def sum_odds(list)
    total = 0
    for num in list:
        if num % 2 != 0:
            total += num
    print(total) 
"""

print(sum_odds(my_list))