# 1.
numbs = []
for i in range(1500, 2700):
    if (i%7==0) and (i%5==0):
        numbs.append(str(i))
print(','.join(numbs))

# 2.
fahrenheit = int(input('Enter a temp in Fahrenheit:'))
celsius = (fahrenheit - 32) * 5.0/9.0

print('Temp:', fahrenheit, celsius)

# 3.
from random import randint as rint
numbs = rint(1, 9)

while True:
    user_guess = int(input('Guess a number between 1 and 9:'))
    if numbs == user_guess:
        print('Great Guess!')
        break
    else:
        print('Wrong number try again..')


# 4 & 5.
def star_pattern(t, b):
    starList = []
    for i in range(1, t+1):
        starList.append('*'*i)
    print('\n'.join(starList))

t = 5
b  = 4
star_pattern(t, b)

# 6.
# Taking user input and reversing using join method
user_word = input('Enter a word:')
reverse_word = ''.join(reversed(user_word))
print(reverse_word)

# 7.
number_list = [1, 2, 3, 4, 5, 6, 7, 8]

even, odd = 0, 0

for num in number_list:
    if num % 2 == 0:
        even += 1

    else:
        odd += 1

print('Even numbers in the list:', even)
print('Odd numbers in the list:', odd)

# 8.
datalist = ([1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}])
for data in datalist:
    print(type(data))

# 9.

def number_printer():
    for numbs in range(0,6):
        if numbs != 3 and 6:
            print(numbs)

number_printer()