zoo = []

print('Ez egy állatkert.')
print('Állat hozzáadása (1) - elétele (2) - kilépés (0)')

select = None

while select != '0':
    select = input('Mit szeretne tenni? ')    
    
    if select != '0':
        if select == '1':
            animal = {}
            name = input('Az állat neve: ')
            
            if name not in animal.keys():
                animal[name] = 1
                zoo.append(animal)
                
            else:
                for i in zoo:
                    i[name] += 1
            
            animal = {}
                
for i in zoo:
    print(i)
