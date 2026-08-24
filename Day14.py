from functools import reduce

#Ex. 1
#map is used to apply a function to all iterables in the list
#filter is used to screen out the correct iterables based on a given condition
#reduce is used to combine all numbers in an list and rteturn a single figure

#A higher order fn takes and returns a fn as an argument or parameter, A closure can be used to return a fn from another nestedd function within. A decorator allows modification of a function without actually changing it
num2 = [1,2,3,4,5,6]
def pow(x):
    return x ** x

power = map(pow, num2)
print(list(power))

def abs(x):
    if x > 0:
        return False
    return True
power2 = filter(abs,num2)
print(list(power2))

def add(x, y):
    return x + y

addit = reduce(add, num2)
print(addit)

#
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for  country in countries:
 print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)




#Ex. 2
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#
def upperc(x):
     return x.upper()

c_upper = map(upperc, countries)
print(list(c_upper))

#
def numb(x):
    return x ** x

numbsqr = map(numb, numbers)
print(list(numbsqr))

#
def namez (x):
    return x.upper()

n_upper = map(namez, names)
print(list(n_upper))

#
def land(x):
    if 'land' in x:
        return False
    return True

lands = filter(land, countries)    
print(list(lands))

#
def landchar(x):
    if len(x) == 6:
        return True
    return False

countrychar = filter(landchar, countries)
print(list(countrychar))

#
def e(x):
    if x[0] is 'E':
        return False
    return True

e_char = filter(e, countries)
print(list(e_char))

#
def numb(x):
    return x ** x

numbsqr = map(numb, numbers)


def numb3(x):
    if x % 2 == 0:
        return True
    return False

sgq_even = filter(numb3, numbsqr)


def addnum(x, y):
    return x + y

addnumsqq = reduce(addnum,sgq_even)
print(addnumsqq)

#
g = ['TMNT', 1, '36']
def get_string_lists (x):
    if isinstance(x,str):
        return True
    return False

game = filter(get_string_lists, g)
print(list(game))

#
def summ(x, y):
    return x + y

summa = reduce(summ, numbers)
print(summa)


#
def conc(x, y):
     return f'{x}, {y}'

conca = reduce (conc, countries[:-1]) 
print(f'{conca}, and {countries[-1]} are north European countries.') 



###
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

###
choice = input('Enter your type of function: square, cube, absolute = ')
num = int(input('Enter your number = '))

def square(num):          # a square function
    return num ** 2

def cube(num):            # a cube function
    return num ** 3

def absolute(num):        # an absolute value function
    if num >= 0:
        return num
    else:
        return -(num)
    
def number_function(choice): # a higher order function returning a function
    if choice == 'square':
        return square
    elif choice == 'cube':
        return cube
    elif choice == 'absolute':
        return absolute

result = number_function(choice)

print(result(num))  

    
#map = spreads the function to all the elements in the list
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2

n_squared = map(square, numbers)
print(list(n_squared))  


name = ['rose', 'kemi', 'loka']
def cap(x):
    return x.capitalize()

cap_name = map(cap, name)

print(list(cap_name))


#filter = gets element in a list based on a condition
numbers = [3,9,8,2,1,8,4]

def isodd(x):
    if x % 2 != 0:
        return True
    return False

oddnum = filter(isodd, numbers)
print(list(oddnum))


###
names = ['Kemi', 'LACON', 'FIFA', 'nuel']

def uppern(x):
    if x == x.upper():
        return True
    return False

uppernames = filter(uppern, names)
print(list(uppernames))


#reduce = returns value by combining all elements in a list
numbers_str = ['1', '2', '3', '4', '5'] 
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    


###
numbers = [3,4,2,1]
def multiply(x, y):
    return x * y

mult = reduce(multiply, numbers)
print(mult)