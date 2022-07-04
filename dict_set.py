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