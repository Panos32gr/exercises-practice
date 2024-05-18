prokrithikan = 0
megisth = 0
sunolo = 0



for i in range(5): #32
    tries = 3
    flag = False
    name = raw_input("Onoma athlitrias: ")
    attempt = float(input("Bolh athlitrias: "))
    while not flag:
        tries -= 1
        if attempt > 70:
            flag = True
            print "H", name, "Prokrithike ston epomeno guro"
            prokrithikan += 1
            if attempt > megisth:
                megisth = attempt
        elif tries > 0:
            attempt = float(input("Bolh athlitrias: "))
        else:
            flag = True
            print "MH PROKRISH"
    sunolo += attempt

print "To plithos to athlitriwn pou prokrithikan einai: ", prokrithikan
mesosoros = sunolo / prokrithikan
print "O mesos oros ton athlitriwn pou exoun prokrithei einai: ", mesosoros