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

omadaA = []
xronosA = []
omadaB = []
xronosB = []

for i in range(10):
    name = raw_input("Onoma omadas: ")
    time = float(input("Xronos omadas: "))
    while time <= 0:
        print "dwste thetiko xrono."
        time = float(input("Xronos omadas: "))
    if i < 5:
        omadaA.append(name)
        xronosA.append(time)
    else:
        omadaB.append(name)
        xronosB.append(time)

print "Taxyteros omadas A:"
x = sorting(xronosA, omadaA)
print "Onoma:", x[-1][-1], "Xronos: ", x[0][-1]


omadaAB = omadaA+omadaB
xronosAB = xronosA+xronosB

y = sorting(xronosAB, omadaAB)
l1 = y[0]
l2 = y[1]

print "Taxyteroi 10 apo to sunolo twn omadwn:"
for apot in range(len(l1)/2, len(l1)):
    print "Onoma:", l2[apot], "Xronos:", l1[apot]    

