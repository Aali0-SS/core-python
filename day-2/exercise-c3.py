# Six is a Mob
def mob_test():
    name_list = ['Bob', 'Tim', 'Sam', 'Jill', 'George', 'Sarah']
    three_name  = ['a', 'b', 'c', 'd', 'e']
    
    if three_name > name_list:
        print('There is a mob in the room!')
    elif three_name < name_list:
        print('The room is getting crowded')
    else:
        print('The room is not crowded')

mob_test()