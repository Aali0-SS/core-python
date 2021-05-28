# Three is a Crowd - Part 2
def crowd_test():
    name_list = ['Bob', 'Tim', 'Sam', 'Jill' ]
    three_name  = ['a', 'b', 'c']
    name_list.remove('Tim')
    if three_name > name_list:
        print('The room is getting crowded')
    else:
        print('The room is not too crowded')

crowd_test()