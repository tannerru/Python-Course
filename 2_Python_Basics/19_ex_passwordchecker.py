
# less code, same results
username = input('username: ')
password = input('password: ')
print(f'hello {username}, your password {len(password)* "*"} is {len(password)} letters long')


# Do people prefer more variables for easy readability vs less code written??
username = input('username: ')
password = input('password: ')
password_length = len(password)
hidden_password = "*" * password_length
print(f'hello {username}, your password {hidden_password} is {password_length} letters long.')
