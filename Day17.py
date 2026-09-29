#exception handling basically says that if the first block of code of fails the second runs as a "grateful exit" for errors. Differs from selection/iteration cause that's more of a loop that gives different paths for user input.
#Standard examples
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e) #unsupported operand type(s) for -: 'int' and 'str' is the print out


try:
    print(10 + int('5'))
except:
    print('Something is worng.')

try:
    print(10 + '5')
except:
    print('Error! Something is wrong.') 

#Ex including else & fin
try:
    name = input('What is your name? ')
    year = int(input('What year where you born? '))
    age = 2026 - year
    print(f'Hello {name}, You are {age} years old.')
except:
    print('Error! Something is wrong')   
else: 
    print('It ususally runs with the try block')
finally:
    print('I always run')

#Ex excluding print from first block to be subbed on the else block
try:
    name = input('What is your name? ')
    year = int(input('What year where you born? '))
    age = 2026 - year
except:
    print('Error! Something is wrong')   
else: 
    print(f'Hello {name}, You are {age} years old.')  #It works so you don't need a print in the try block and can input that in the else code 
finally:
    print('I always run')    

#Ex that produces error
try:
    name = input('What is your name? ')
    year = input('What year where you born? ')
    age = 2026 - year
    print(f'Hello {name}, You are {age} years old.')
except:
    print('Error! Something is wrong') 

#Ex that gives type error
try:
    name = input('What is your name? ')
    year = input('What year where you born? ')
    age = 2026 - year
    print(f'Hello {name}, You are {age} years old.')
except TypeError:
    print('There is a Type error! Something is wrong') 
except ValueError:
    print('There is a Value error! Something is wrong')

# for unpacking this is *list, **dictionaries
def sum_of_f(a,b,c,d,e):
    return a + b + c + d + e
lst=[1,2,3,4,5]
print(sum_of_f(*lst))


args = [2, 7]
print(range(*args))      #not unpacking?

#so you can type it and then the * are still left in the list but displayed(unpacked) by the computer
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

#dictionaries
def unpack(name,country,city,age):
    return f'Hello {name}. We know you live in {city}, {country} and you are {age} years old. The Order is watching.'
info = {'name':'Kemi', 'country':'Nigeria', 'city':'Lagos', 'age':'19'}
print(unpack(**info))

#packing
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

#spreading = basically ining lists 
one = [1,2,3]
two = [4,5,6]
lstt = [0, *one, *two]
print(lstt)

wa = ['Africa', 'Kenya']
ea = ['Libya', 'Guinea']
a = ['Nigeria', *wa, *ea]

#enumerate
for index, item in enumerate([20, 30, 40]):
    print(index, item)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

#zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

#Exercises
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(nordic_countries)  
print(es)  # Estonia
print(ru)  # Russia