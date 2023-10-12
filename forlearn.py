# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)
print('\n')
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)
print('\n')

s = [value ** 2 for value in range(1, 11)]
print(s)

a = (1,2)
print(a)
a = (1,23,4)
print(a)
a = 3
print(a)
a = "h"
print(a)