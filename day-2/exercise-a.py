# 1.
print('Hello World'[8])

# 2.
print('thinker'[2:5])
# Error in syntax, string index not in range. Also best practice to lowercase variable.
S = 'hello'
print(h[1])

# 3.
# Error in syntax, similar to previous
S = 'Sammy'
print(s[2:])

# 4.
print(set('Mississippi'))

# 5.
def palindromeTest(input):
        return input == input[::-1]


input = 'O, a kak Uwakov lil vo kawu kakao!'
answer = palindromeTest(input)
if answer:
    print('Yes')
else:
    print('No')