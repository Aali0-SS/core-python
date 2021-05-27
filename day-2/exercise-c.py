# Three is a Crowd
# Throwing error need to fix
def crowd_test(crowd, val):
    for i in crowd:
        if val>= i:
            return False
    return True

crowd = ['Ahmed', 'Jessica', 'Yasin', 'Isa']
val = 3
if(crowd_test(crowd, val)):
    print('The room is not too full')
else:
    print('The room is getting crowded')
