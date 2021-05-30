# 1.
def func():
    print('Hello World')

func()


# 2.
def func1(name):
    print('Hi My name is' + name)

func1('Google')


# 3.
def func3(x, y, z):
    if z == True:
        return x
    else:
        return y

print(func3('hello', 'goodbye', False))


# 4.
def func4(x, y):
    return x * y

print(func4(7, 6))


# 5.
def is_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False

print(is_even(122220))


# 6.
def lesser_greater(x, y):
    if x > y:
        return True
    
    if y >= x:
        return False

print(lesser_greater(2, 19))


# 7.
def arbitrary(*args):
    return sum(args)

print(arbitrary(3, 5, 1, 6, 7))


# 8.
def arbitrary_list(*args):
    return [x for x in args if x % 2 == 0]

print(arbitrary_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 9.
def str_func(str):
    result = []

    for i in range(len(str)):
        if i % 2 == 0:
            result.append(str[i].upper())
        else:
            result.append(str[i].lower())

    return ''.join(result)

print(str_func('The Final Round Begins!'))


# 10.
def number_fun(x, y):
    if x%2 == 0 and y%2 == 0:
        return min(x, y)
    else:
        return max(x, y)

print(number_fun(2, 4))


# 11.
def str_checker(str):
    first_str, second_str = str.split(' ')
    if first_str[0].upper() == second_str[0].upper():
        return True
    else:
        return False

print(str_checker('Ahmed', 'Ali'))