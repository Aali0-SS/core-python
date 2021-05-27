# 1.
my_list = [1, 'Hello World', 99.99]
print(my_list)

# 2.
# Receiving type error
nest_list = [1,1[1,2]]
grab_two = nest_list[1][1]
print(str(grab_two))

# 3.
lst = ['a', 'b', 'c']
print(lst[1:])

# 4.
week_days = {'Monday': '01', 'Tuesday': '02', 'Wednsday': '03', 'Thursday': '04', 'Friday': '05', 'Saturday': '06', 'Sunday': '07'}

# 5.
# Syntax error, not properly indexing
d = {'k1': [1, 2, 3]}
print(d[k1][1])

# 6.
# This list now becomes immutable once converted to tuple
my_tuple = ([1,[2,3]])
print(my_tuple)

# 7.
distinct_state = set('Mississippi')

# 8.
distinct_state.add('X')
print(distinct_state)

# 9.
print(set([1, 2, 3]))


# Question 1

numbs = []
for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        numbs.append(str(i))
    
print(','.join(numbs))


# Question 2

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

x = int(input())
print(factorial(x))


# Question 3

numbs = int(input('Enter the number:'))
d = dict()
for i in range(1, numbs + 1):
    d[i] = i * i
print(d)


# Question 4

seq = input('Enter input:')
lst = seq.split(',')
tup = tuple(lst)
print(lst, tup)


# Question 5

class StringMethod(object):
    def __init__(self):
        self.str = ''
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.uppper())

obj = StringMethod()
obj.getString()
obj.printString()