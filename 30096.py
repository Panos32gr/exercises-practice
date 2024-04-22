TEAMS = []
GRADES = []
PROK = []
BATHPROK =[]


for i in range(5):   # na ginei 20 sto telos
    name = raw_input("Onoma omadas: ")
    score = float(input("Bathmologia omadas: "))
    TEAMS.append(name)
    GRADES.append(score)
    if score > 7:
        PROK.append(name)
        BATHPROK.append(score)



N = len(BATHPROK)
flag = False

while N-1 > 0 and not flag:
    flag = True
    for j in range(N-1, 0 , -1):
        if BATHPROK[j]> BATHPROK[j-1]:
            BATHPROK[j],BATHPROK[j-1] = BATHPROK[j-1],BATHPROK[j]
            PROK[j], PROK[j-1] = PROK[j-1], PROK[j]
            flag = False

print BATHPROK
print PROK
print "Oi omades pou prokrithikan einai: "
for omada in range(3):
    print PROK[omada],  "Me bathmologia: ",  BATHPROK[omada]



