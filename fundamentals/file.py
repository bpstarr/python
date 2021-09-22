num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
#<type 'tuple'>
print(pizza_toppings[1])
#sausage
pizza_toppings.append('Mushrooms')
print(person['name'])
#John
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])
#banana

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

    #It's lower

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

    #Just right

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1
#0,1,2,3,4 2,3,4 2,5,8 0,1,2,3,4
pizza_toppings.pop()
#['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese','olives']
pizza_toppings.pop(1)
[#'Pepperoni', 'Jalepenos', 'Cheese','olives']

print(person)
#{eye_color':'blue','name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
person.pop('eye_color')
print(person)
##{'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
    #After 1st if statement,After 1st if statement,After 1st if statement

def print_hello_ten_times():
    for num in range(10):
        print('Hello')
        #hello x 10times

print_hello_ten_times()
#hello x 10times

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


print_hello_x_times(4)
#hello,hello,hello,hello

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
#hello x 10times
print_hello_x_or_ten_times(4)
#hello,hello,hello,hello


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
# print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)