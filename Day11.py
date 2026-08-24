#EXE LV1
def two_num(num1, num2):
    return num1 + num2
print(two_num(5,6))

def area_of_circle(r):
    pi = 3.142
    area = pi * r * r
    return area
print(area_of_circle(4))

def add_all_nums(*args):
    total = 0
    for i in args:
        if type(i) == int or type(i) == float:
         total += i
        return total
    else:
       return 'Input is invalid'
print(add_all_nums(2, 3, 4, 5))

def convert_celsius_to_fahrenheit(c):
   f = (c * 9/5) + 32
   return f
print(convert_celsius_to_fahrenheit(37))

def check_season(m):
   if m in ['March', 'April', 'May']:
      return 'Spring'
   elif m in ['June', 'July', 'August']:
       return 'Summer'
   elif m in ['September', 'October', 'November']:
      return 'Autumn'
   else:
      return 'winter'
print(check_season('March'))   

def calculate_slope(x1,y1,x2,y2):
   slope = (y2 - y1) / (x2 - x1)
   return slope
print(f'The slope is {calculate_slope(x1 = 2, y2 = 5, y1 = 6, x2 = 3)}')

def solve_quadratic_eqn(a,b,c):
   quad = (-b + (b**2 - 4*a*c)**0.5) / (2*a), (-b - (b**2 - 4*a*c)**0.5) / (2*a)
   return quad
print(solve_quadratic_eqn(2, 3, -5))    

def print_list(lst):
   for i in lst:
      print(i) 
num = [1, 2, 3, 4, 5]
print_list(num)     

def reverse_list(lst):
   return lst[::-1]
print(reverse_list(num))

def capitalize_list_items(lst):
    return [i.capitalize() for i in lst]
name = ['kemi', 'tolu', 'ayo']
print(capitalize_list_items(name))

def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item(name, 'bola'))

def remove_item(lst,item):
   lst.remove(item)
   return lst
print(remove_item(name, 'tolu'))

def sum_of_numbers(n):
   total = 0
   for i in range(n + 1):
      total += i
   return total
print(sum_of_numbers(10))  

def sum_of_odds(n):
   total = 0
   for i in range(n + 1):
      if i%2 != 0:
         total += i
   return total
print(sum_of_odds(10))   

def sum_of_even(n):
   total = 0
   for i in range(n + 1):
      if i%2 == 0:
         total += i
   return total
print(sum_of_even(10))   


#EXE LV2
def evens_and_odds(n):
   count_even = 0
   count_odd = 0
   for i in range (n + 1):
      if i%2 == 0:
            count_even += 1
      else:
       count_odd += 1
   return f'The number of odds are {count_odd}. The number of even are {count_even}.'
print(evens_and_odds(100))

def factorial(n):
   result = 1
   for i in range(1, n+1):
      result *= i
   return result
   
print(factorial(4))

def is_empty(n=""):
   if n == "":
    return 'Parameter is empty'
   else:
      return 'Paramter is not empty'

print(is_empty()) 

def greet(g = "Hello, Guest!"):
   return g
print(greet())

def show_args(**args):
   return args
print(show_args(name="Bob", pet="Fluffy, the bunny"))

def is_prime(n):
   if n <= 1:
      return False
   for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
         return False
   return True
print(is_prime(7))





#  def end_message (name):
#  return  f'{name}, Congrats on completing the program'
#  print (end_message('Kemi'))

#  def sqr_num(num):
#      return f'{num ** 2} is the square of {num}'
#  print(sqr_num(2))

#  def circle_area(radius):
 #     pi = 3.142
 #     area = pi * radius ** 2
 #     return area
# print(circle_area(5))

#  ef sum_of_numbers(n):
  #    total = 0
 #     for i in range(n+1):
 #         total+=i
  #    return total
#  print(sum_of_numbers(10))
#  print(sum_of_numbers(100)) #  

#  def print_fullname(firstname, lastname):
#      space = ' '
#      full_name = firstname  + space + lastname
#      return full_name
# print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

#  def find_even_numbers(n):
 #     evens = []
  #    for i in range(n + 1):
  #        if i % 2 == 0:
  #            evens.append(i)
  #    return evens
#  print(find_even_numbers(10))

#  ef generate_groups (team,*args):
 #  #     print(team)
 #     for i in args:
 #         print(i) 
#  enerate_groups('Team-1','Asabeneh','Brook','David','Eyob')

#  def#   greet(name, location):
    #  print("Hi there", name, "how is the weather in", location)
#  
#  t(name="Alice", location="New York")

#  def#   greet(name, location):
#      return f"Hi there {name}, how is the weather in {location}?"

#  kemi_dict = {"name": "Kemi", "location": "New York"}
#  print(greet(**kemi_dict))

#You can pass functions around as parameters
#  def square_number (n):
 #     return n ** n
#  def do_something(f, x):
#      return f(x)
#  print(do_something(square_number, 3)) # 27