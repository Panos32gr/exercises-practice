def sorting(a, b):
    N = len(a)
    flag = False
    while 0 < N-1 and not flag:
        flag = True
        for j in range(N-1, 0, -1):
                if a[j] < a[j-1]:
                    a[j], a[j-1] = a[j-1], a[j]
                    b[j], b[j-1] = b[j-1], b[j]
                    flag = False
    return a, b

omadaA = []
xronosA = []
omadaB = []
xronosB = []
omadaAB = []
xronosAB = []


for i in range(1,11):
    if i <= 5:
        name = raw_input("onoma omadas: ")
        time = float(input("Xronos se deuterolepta: "))
        while time < 0:
            print "parakalw dwste thetikh timh xronou."
            time = float(input("Xronos se deuterolepta: "))
        omadaA.append(name)
        xronosA.append(time)
    else:
        name = raw_input("onoma omadas: ")
        time = float(input("Xronos se deuterolepta: "))
        while time < 0:
            print "parakalw dwste thetikh timh xronou."
            time = float(input("Xronos se deuterolepta: "))
        omadaB.append(name)
        xronosB.append(time)

print omadaA, xronosA
print omadaB, xronosB


taksinomhshA = sorting(xronosA, omadaA)
newA = taksinomhshA[0]
newtimesA = taksinomhshA[1]

print "Taxyterh omada group A:"
print newA[0]
print newtimesA[0]


taksinomhshB = sorting(xronosB, omadaB)
newB = taksinomhshB[0]
newtimesB = taksinomhshB[1]

print "Taxyterh omada group B:"
print newB[0]
print newtimesB[0]

temp = newA + newB
temp2 = newtimesA + newtimesB
for k in temp:
    omadaAB.append(k)
for h in temp2:
    xronosAB.append(h)


taksinomhshOlwn = sorting(xronosAB, omadaAB)

resultsAB = taksinomhshOlwn[0]
resultsTimesAB = taksinomhshOlwn[1]
print resultsAB
print resultsTimesAB

print "Oi 10 omades me tous kaluterous xronous einai:"
for i in range(3):
    print resultsAB[i], "me xrono: ", resultsTimesAB[i]
    
