#List Methods #1
basket = [1,2,3,4,5]

#adding
basket.append(100) #append changes list in place, does not produce a value, just appends a value to the variable.
print(basket)
new_list = basket
print(new_list)

#insert
basket.insert(4, 100)
print(basket)


#extend
basket.extend([100,101])
print(basket)

#remove
basket.pop() #pop removes value at end of list
basket.pop()
basket.pop()
basket.pop(0)
basket.remove(4)
print(basket)

basket.clear()
print(basket)



#side note on this, I could see this being useful to edit a lot of excel entries or really any sorta of data entry that has some common values that need to removed, 
# Throw it in a for loop and run this

