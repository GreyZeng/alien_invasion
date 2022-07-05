classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)

print(len(classmates))

print(classmates[-1])

classmates.append("Adam")

print(classmates)

classmates.insert(0,"Mike")
print(classmates)

print(classmates.pop(1))
print(classmates)

classmates[1] = "Lucy"
print(classmates)

classmates[1] = ['Lucy','Lily']
print(classmates)
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 这样会报错：classmates[1] = "SS"
t = ()
print(len(t))