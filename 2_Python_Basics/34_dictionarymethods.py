user  = {
    'basket': [1,2,3],
    'greet': 'hello'
    'age': 20
}



user2 = dict(name = 'tanner') # not commone way to write dictionaries.


print(user.get('age', 'NA'))  #get will avoid errors when key not exist

print(user2)