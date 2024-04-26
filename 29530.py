NAME = []
PRICE = []


for i in range(3): # 10
    onoma = raw_input("Onoma grafeiou: ")
    timh = float(input("Timh grafeiou: "))
    while timh <= 0:
        print "Parakalw dwste thetikh timh  prosforas."
        timh = float(input("Timh grafeiou: "))
    NAME.append(onoma)
    PRICE.append(timh)



N = len(PRICE)
flag = False

while N-1 > 0 and not flag:
    flag = True
    for j in range(N-1, 0, -1):
        if PRICE[j] < PRICE[j-1]:
            PRICE[j],PRICE[j-1] = PRICE[j-1], PRICE[j]
            NAME[j], NAME[j-1] =  NAME[j-1], NAME[j]
            flag = False


zhtoumenoPoso = PRICE[0]
print "To/Ta grafeio/a me tin oikonomikoterh prosfora einai:"
for least in range(len(PRICE)):
    if PRICE[least] == zhtoumenoPoso:
        print NAME[least]
        print PRICE[least]

