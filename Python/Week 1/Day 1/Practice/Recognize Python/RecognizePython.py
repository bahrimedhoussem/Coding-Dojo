num1 = 42
# - variable declaration
num2 = 2.3
# - variable declaration
boolean = True
#Data Types - Primitive - Boolean
        

string = 'Hello World'
# - variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#composite : list-initialize 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#composite : dict-initialize
fruit = ('blueberry', 'strawberry', 'banana')
#composite : Tuples-initialize
print(type(fruit))
#type-check
print(pizza_toppings[1])
#log statement
pizza_toppings.append('Mushrooms')
#composite : list - add value
print(person['name'])
# log statement
person['name'] = 'George'
#composite : list-change value 
person['eye_color'] = 'blue'
#composite : list-add value
print(fruit[2])
#log statement
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#conditional
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#conditional
for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
#for loop
x = 0
while(x < 5):
    print(x)
    x += 1
#while loop 
pizza_toppings.pop()
pizza_toppings.pop(1)
#composite : list-delete value
print(person)
#log statement 
person.pop('eye_color')
#composite : dict-delete value
print(person)
#log statement
#for loop : start
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    #continue
    print('After 1st if statement')
    #log statement
    if topping == 'Olives':
        break
    #break

def print_hello_ten_times():
    #for loop : start
    for num in range(10):
        print('Hello')
        #log statement
#for loop : stop
print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    #for loop : start
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
#for loop : stop

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'===>#TypeError: 'tuple' object does not support item assignment

# print(person['favorite_team']) ==># KeyError: 'favorite_team'
# print(pizza_toppings[7])==>#- IndexError: list index out of range
# print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)