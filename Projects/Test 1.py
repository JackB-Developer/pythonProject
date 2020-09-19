import math
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.find('B'))
# ('What we are replacing', 'Replacement')
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
print(course.title())

# Math
#Return Float
print(10/3)
#Return Int
print(10//3)

x = 10
x += 3
print(x)

x = 10 + 3 * 2
print(x)

x = 2.9
print(round(x))
#absolute returns positive
print(abs(-2.9))

print(math.ceil(-2.9))

##################################################
# If statements
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day. Drink plenty of water")
elif is_cold:
    print("It's a cold day!")
    print('Wear warm clothes')
else:
    print('Enjoy your day')

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Sorry")

#weight = int(input('Weight: '))
#unit = input('(L)bs or (K)g')
#if unit.upper() == "L":
#    converted = weight * 0.45
#    print(f"You are {converted} kilos")
#else:
#    converted = weight / 0.45
#    print(f"You are {converted} pounds")

#########################################
#LOOPS
i = 1
while i <= 5:
    print(i)
    i += 1
print('Done')

########################################
# For Loops
for item in 'Python':
    print(item)
for item in ['Python']:
    print(item)
for item in range(10):
    print(item)
for item in range(5, 10, 2):
    print(item)

# Add up items in cart
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# Nested Loops - Coordinates
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for x in range(x_count):
        output += 'x'
    print(output)

numbers = [3, 5, 2, 8, 20, 3]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
    print(max)

