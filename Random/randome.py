from random import sample
from random import random
import random


list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

random.seed(5)
print(random.random())
print(random.random())

r1 = random.randint(5, 15)
print("Random number between 5 and 15 is % s" % (r1))
r2 = random.randint(-10, -2)
print("Random number between -10 and -2 is % d" % (r2))

# print(random())

list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
string = "geeks"
print(random.choice(string))
tuple1 = (1, 2, 3, 4, 5)
print(random.choice(tuple1))


list1 = [1, 2, 3, 4, 5]

print(sample(list1, 3))
list2 = (4, 5, 6, 7, 8)

print(sample(list2, 3))
list3 = "45678"

print(sample(list3, 3))


sample_list = [1, 2, 3, 4, 5]

print("Original list : ")
print(sample_list)
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)
