#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value.


#1 answer
user = {
'age': 31,
'username': 'tannerru',
'weapons': ['ak47' , 'rocket launcher'],
'is_active': True,
'clan': 'Dadbods'
}

#2 answer
print(user.keys())

#3 answer
user['weapons'].append ('baseball bat')
print(user)

#4 answer
user.update({'is_banned': False})
print(user)

#5 answer
user['is_banned'] = True
print(user)

#6 answer
user2 = user.copy()
user2.update({'age':40 , 'username': 'Beth'})
print(user2)
