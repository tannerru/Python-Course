user  = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

# print('basket' in user)
# print('hello' in user.keys())
# print('age' in user.keys())
# print(20 in user.values())
# print(user.items())


# print(user.clear())

print(user.pop('age'))
print(user.update({'age': 55}))
print(user)