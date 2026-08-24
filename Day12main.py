#   exe 1
import os
import random
import string
def random_user_id(n):
    id = ''
    for i in range(n):
        id += random.choice(string.ascii_letters + string.digits)
    return id
print(random_user_id(6))

def user_id_gen_by_user():
    cha = int(input('Enter the number of characters: '))
    id1 = int(input('Enter the number of IDs: '))
    for i in range(id1):
        print(random_user_id(cha))
print(user_id_gen_by_user())        

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r}, {g}, {b})'
print(rgb_color_gen())

# ex 2





import os
import string

import Day12mymodule
print(Day12mymodule.generate_full_name('Kemi', 'Nick-Ibitoye'))

from Day12mymodule import generate_full_name, gravity
print(generate_full_name('Kemi', 'Nick-Ibitoye'))

from Day12mymodule import generate_full_name as fn
print(fn('Kemi', 'Nick-Ibitoye'))

from Day12mymodule import gravity as g
weight = 50 * g
print(weight)


#sys module
 #import os
#Create a folder
 #os.mkdir("Projects")
#Change folder
 #os.chdir("Projects")
#See your current location
 #print(os.getcwd())

#statmodule
import statistics
data = [2.75, 1.75, 1.25, 0]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))

from statistics import mean, median, mode
data = [2.75, 1.75, 1.25, 0]
print(mean(data))
print(median(data))
print(mode(data))

#math module
from math import pi, sqrt, pow, floor, ceil
print(pi)
print(sqrt(16))
print(pow(2, 3))
print(floor(2.75))
print(ceil(2.75))

import math
print(math.pi)
print(math.sqrt(16))
print(math.pow(2, 3))
print(math.floor(2.75))
print(math.ceil(2.75))

#string module
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

#random module
import random
print(random.random())
print(random.randint(1, 10))