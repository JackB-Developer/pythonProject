# Lists
friends = [['Brad', 43], ['Perry', 44], ['Scott', 46]]
friends.append(['Chris', 45])

print(friends[0])
print(friends[1])

print(len(friends))
# [0]= first item
print(friends[0][0])
print(friends)

# Tuples ()
# A variable with multiple values the () or , indicate a tuple. You cannot use .append use var = var + (new_elements,)
# Tuples are not meant for changing but can be changed by reassigning the nw value to the var
short_tuples = 'Brad', 'Perry'
long_tuples = ('Brad', 'Perry')

friends  = ('Brad', 'Perry')
print(friends)
friends = friends + ('Jenn',)
print(friends)

# Sets {} - Like lists and tuples but they don't hold order or duplicate elements
# Easy to compare one to another

art_friends = {'Brad', 'Perry', 'Scott'}
science_friends = {'Jenn', 'Chris'}

art_friends.add('Jenn')
print(art_friends)
# Now Jenn has been added it cannot be added again

# Comparing Sets {}
art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

# Combining sets {} - Notice Jenn will only appear once
all_friends = art_friends.union(science_friends)
print(all_friends)