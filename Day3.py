import math
height = 167.64
num = 5j
#ignore
base = input('Enter base of triangle: ')
t_height = input('Enter height of triangle: ')
area = 0.5 * int(base) * int(t_height)
print(f'The area of the triangle is: {area}')
#ignore
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter = int(side_a) + int(side_b) + int(side_c)
print(f'The perimeter of the triangle is: {perimeter}')
#ignore
length = input('Enter length: ')
width = input('Enter width: ')
area = int(length) * int(width)
perimeter = (2 * (int(length) + int(width)))
print(f'The perimeter of the rectangle is: {perimeter}')
#ignore
r = input('Enter radius: ')
pi = 3.14
area = int(pi)* int(r) * int(r)
circ = 2 * int(pi) * r
print(f'The area and circumference of the circle is: {area} and {circ}')
#ignore
# equation is y = 2x - 2
m = 2
b = -2
y1 = 2
y2 = 10
x1 = 2
x2 = 6
y_int = (0, b)
x_int = (-b/m, 0)
slope = (y2 - y1) / (x2 - x1)
euclidian = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'The y-intercept is: {y_int}, the x-intercept is: {x_int}, the slope is: {slope}, and the euclidian distance is: {euclidian}')
print(f'We compared the two slope and the result is {m==slope}')
#lmao, ignoring fucking number 11 cause when was that taught, fuckking pricks
python = "python"
dragon = "dragon"
len_p = len(python)
len_d = len(dragon)
print(f'The length of python and dragon are equal, so anything otherwise is {len_p!=len_d}')
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('There is no' 'on' in 'python' and 'on' in 'dragon' '.' f'It is {not("on" in "python" and "on" in "dragon")}')
print(str(float(len_p)))
#ignoring 7 cause mf didn't teach if and or else statements
f_d = 7 // 3
it = 2.7
eq = f_d == int(it)
print(f'The floor division of 7 by 3 is {eq}')
#hmm
l = '10'
t = 10
print(f'The type of 10 is {type(t)} and the type of "10" is {type(l)}. So anything otherwise is {type(t)==type(l)}')
l = 9.8
print(f'The rounded value of 9.8 is {round(l)} and anything otherwise is {round(l)!=t}')
#ignoring 21 - 22 cause fuck that fr