# Three is a Crowd
def crowd_test():
    name_list = ['Bob', 'Tim', 'Sam', 'Jill' ]
    three_name  = ['a', 'b', 'c']
    name_list.remove('Tim')
    if three_name > name_list:
        print('The room is getting crowded')

crowd_test()