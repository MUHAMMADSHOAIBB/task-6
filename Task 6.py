print('===============Task6.1================')
# Design a calculator that takes two values from user
x=(int(input('Please sir enter your first value')))
y=(int(input('please sir enter your second value')))
print(x+y,x-y,x*y,x/y,x//y)
print('================TAsk6.2============')
# #takes two values whether they are equal or not
a=5
b=7
print(a==b)
print(a!=b)
print('==============task6.3==============')
#calculate the area of plot
a = int(input('enter the length of a plot'))
b = int(input('enter the width of a plot'))
c = int(input('enter the height of a plot'))
print("area of a plot",a*b*c)
print('===============task6.4==============')
#Design a BMI system in US
w = float(input('please enter your weight in kgs'))
h = float(input('please enter your height in feet'))
print('your body mass index is',(w/(h**2)*703))
# Design a BMI system in metric
weight = float(input('enter your weight in kgs'))
height = float(input('enter your height in cm'))
print('your body mass index is ',(weight/(height**2)))
print('===================Task6.5===================')
a= int(float(input('enter your weight in kgs')))
print('your weight in pounds is ',a*2.205)
#Height into inches
h = int(float(input('enter your height')))
print('your height in inches is',h*2.54)
#radian into degree
r = int(float(input('enter the value of radian')))
print('your radian in degree is ',r*(180/3.14))

print('=================task6.6=================')
#Area of trapezoid54
a= int(input('enter the length of a'))
b= int(input('enter the length of b'))
h= int(input('enter the height of traphezoid'))
print('area of traphzoid',(a+b)/2*h)
print('===================Area of a parallelogrm==============')
b = int(input('enter the base of parallelogram'))
h = int(input('enter the height of parallelogram'))
print('The area of aparallelogram is',b*h)
#surface volume and area of a cylinder
a = float(input('3.14'))
r = int(input('enter the value of radius'))
h = int(input('enter the value of height'))
print('The surface area of a cylinder is',2*3.14*r*h+2*3.14*r**2)



