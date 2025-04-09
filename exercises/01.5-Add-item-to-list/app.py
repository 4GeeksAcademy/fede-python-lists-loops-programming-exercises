# Remember to import random function here
import random

my_list = [4, 5, 734, 43, 45]

# The magic goes below
def random_numebers():
    
    for i in range(10):
        ten_random = random.randint(0,100)
        my_list.append(ten_random)
    print(my_list)
        


print(random_numebers())
