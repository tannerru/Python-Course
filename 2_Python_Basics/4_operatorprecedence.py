# operator precedence
print(20 - 3 * 4)  # multiply first than add

# Actual order of precedence
# ()
# **
# * /
# + -


# Excerse
print((5 + 4) * 10 / 2)  # 45

print(((5 + 4) * 10) / 2)  # 45

print((5 + 4) * (10 / 2))  # 45

print(5 + (4 * 10) / 2)  # 25

print(5 + 4 * 10 // 2)  # 25
