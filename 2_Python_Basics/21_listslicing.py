# List slicing
amazon_cart= [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart[0::1])
amazon_cart[0] = 'laptop' #lists are mutable, and can be changed unlike strings
print(amazon_cart[1:3])
print(amazon_cart)

new_cart = amazon_cart[0:3]
print(new_cart)