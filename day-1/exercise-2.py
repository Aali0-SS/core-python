# 1.
a = 50 + 50
b = 100 - 10
print(a, b)

# 2,
c= 30+6*6^6*6**6*6+6+6+6+6+6
print(c)

# 3.
print('Hello World', 'Hello World: 10')

# 4. I have a better solution in mind using a function, this is the basic calculation I used
p = 800000
r = 0.06
l = 103

mortgage_payment = p * (r * (1 + r) ** l / ((1 + r) ** l -1 ) * 2)
print(round(mortgage_payment))