# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove('Banana')  # 1. Remove the Banana from the list

basket.pop('Blueberries')  # 2. Remove "Blueberries" from the list.

basket.append('Kiwi')  # 3. Put "Kiwi" at the end of the list.

basket.insert(0, "Apples")  # 4. Add "Apples" at the beginning of the list

print(basket.count('Apples'))  # 5. Count how many apples in the basket

basket.clear()  # 6. empty the basket

print(basket)
