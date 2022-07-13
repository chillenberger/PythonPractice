tuples = [('Hi','Hello-World', 'Earth'), ('Hello-World', 'Hi'), ('Te-st', 'Te-st2')]

new_tuples = list(map(lambda tup: tuple(item.replace('-', ' ') for item in tup), tuples))
print(new_tuples)

# new_tuples = list(filter(lambda x: True if 'Hi' not in x else False, tuples))
new_tuples = [tup for tup in tuples if 'Hi' not in tup]
print(new_tuples)

