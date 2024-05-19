def sorting(list1,list2):
    N = len(list1)
    flag = False
    while N-1 > 0 and not flag:
        flag = True
        for j in range(N-1, 0, -1):
            if list1[j] > list1[j-1]:
                list1[j], list1[j-1] = list1[j-1], list1[j]
                list2[j], list2[j-1] = list2[j-1], list2[j]
                flag = False
    
    return [list1, list2]


NAMES = []
VATHMOS = []

for diag in range(150): #150 end
    onoma = raw_input("Onoma diagonizomenou: ")
    NAMES.append(onoma)
    total = 0
    for judge in range(1,4):
        print "Vathmos krith ", judge,":"
        score = float(input(""))
        total += score
    VATHMOS.append(total)

x = sorting(VATHMOS, NAMES)
VATHMOS = x[0]
NAMES = x[1]

print "Oi diagwnizomenoi pou prokrithikan einai:"
for i in range(len(VATHMOS)):
    if i < 20 or VATHMOS[i] == VATHMOS[19]:
        print "Onoma: ", NAMES[i],"Vathmologia: ", VATHMOS[i] 



