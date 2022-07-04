d={'A':33,'B':44,'C':445}
#print(d['A'])


d['A']=456

# print(d['A'])

if 'D' in d:
    print(d['D'])
elif 'A' in d:
    print(d.get('D',-1))
else:
    print(d['C'])


s = set([1, 1, 2, 2, 3, 3])

print(s)


s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

help(abs)