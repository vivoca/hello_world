mylist = [0] * 100

#examines the conditions
n = 1
while n <= 100:         #körök száma, ennyivel lép
    i = 1
    while i <= 100:     #ajtók száma, ezt vizsgálja
        if i % n == 0:  #ha az ajtó sorszáma osztható a körrel akkor vizsgálni kell
            mylist[i-1] = mylist[i-1] + 1   #ezért hozzáadunk 1-et
        i = i + 1
    n = n + 1

#puts results into a new list
i = 0
n = 0
opened = []
while i < 100:
    if mylist[i] % 2 == 1:  #ha páratlan akkor nyitva van
        opened.append(i+1)  #megoldáslista
        n = n + 1
    i = i + 1

#prints on the screen
i = 0
print("The following doors are open: ")
for i in range(0, 10):
    print(opened[i], end=' ')
    if i==len(range(0, 10)): print()
print('\n')
