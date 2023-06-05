Practice Notebook

my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    my_list.remove(myVal)
    return my_list

print(RemoveValue(27)) #error if run again
     

def RemoveValue(myVal):
    if myVal not in my_list:
        return 'Value must be in the given list'
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))
     

my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    myList.sort()
    return myList

print(OrganizeList(my_word_list))
     

my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list))
#gives Error
     

def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, 'Word list must be a list of strings'
    myList.sort()
    return myList

print(OrganizeList(my_new_list))
     

import random

participants = ['Jack','Jill','Larry','Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False
    
print(Guess(participants))
     

# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except:
        return 'No Larry'
     

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))
     
