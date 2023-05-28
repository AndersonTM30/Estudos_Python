thisList = ['apple', 'banana', 'cherry']
print(thisList)
print(thisList[1])
print(f'Esta lista tem {len(thisList)} itens')

thisList.append('orange')
print(thisList)
print(thisList[-1])

print(thisList[1:3])

if 'banana' in thisList:
    print('tem banana')