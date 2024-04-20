PROKR = []
ON = []
EP = []
failed = 0

for i in range(80): 
    flag = False
    counter = 0
    name = raw_input("Onoma mathitrias: ")
    ON.append(name)
    while counter < 2  and not flag:
        prosp = float(input("Epidosh: "))
        if prosp >= 9.5:
            flag = True
            EP.append(prosp)
            PROKR.append(name)
        else:
            counter += 1
    if counter == 2:
        failed += 1
    
print "To plithos twn mathitriwn pou prokrithike einai: ", len(PROKR)
print "Autes einai: "
for surname in (PROKR):
    print surname
print "O arithmos ton mathitriwn pou den prokrithike einai: ",failed 

