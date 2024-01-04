def addAnimal(myName):
    animal = {}
    found = False

    for i in zoo:
        if myName in i.keys():
            i[myName] += 1
            found = True

    if not found:
        animal[myName] = 1
        zoo.append(animal)


zoo = [{"kecske": 1}]
animal = dict()

print('Ez egy állatkert.')
print('Állat hozzáadása (1) - elétele (2) - kilépés (0)')

select = None

while select != '0':
    select = input('Mit szeretne tenni? ')    
    
    if select != '0':
        if select == '1':
            name = input('Az állat neve: ')
            addAnimal(name)
                   
                
print(zoo)
