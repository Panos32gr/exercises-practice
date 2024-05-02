titlos = []
theates = []

megisto = 0
name = ""
sunolo = 0
counter = 0


movie = raw_input("Titlos tainias: ")
while movie != "TELOS":
    counter += 1
    plithos = int(input("Plithos theaton pou parakolouthisan tin tainia: "))
    
    while plithos <= 0:
        print "Parakalw dwste thetiko arithmo theatwn."
        plithos = int(input("Plithos theaton pou parakolouthisan tin tainia: "))
    
    titlos.append(movie)
    theates.append(plithos)
    sunolo += plithos
    if plithos > megisto:
        megisto = plithos
        name = movie
    movie = raw_input("Titlos tainias: ")





print "H tainia me tis perissoteres provoles einai:", name, "Me arithmo theatwn:", megisto

mesosoros = sunolo / counter

print "O mesos oros provolwn einai:", mesosoros