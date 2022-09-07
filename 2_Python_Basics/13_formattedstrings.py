# formatted strings
# f is used to state the string is going to be formatted.

name = 'Johnny'
age = 55

print(f'hi ' + name + '. You are ' + str(age) + ' years old')  # long manual way

print(f'hi {name}. You are {age} years old')  # only in python 3

print('hi {}. You are {} years old'.format('Johnny', '55'))  # python 2/3

print('hi {}. You are {} years old'.format(
    name, age))  # python 2/3 with variable


# TLDR, let's use the 'f' avaliable in python 3 for future formatted strings.
