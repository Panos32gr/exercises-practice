def kostos(enhlikes, paidia):
    plirwmh = (enhlikes * 7) + (paidia * 4)
    return plirwmh

theseis = 200
esoda = 0
while theseis > 0:
    teliko = 0
    print " diathesimes theseis:", theseis
    enhl = int(input("Enhlikes: "))
    paid = int(input("paidia: "))
    if theseis - (enhl + paid) <= 0 or enhl == -1:
        print -1
    teliko = kostos(enhl, paid)
    print "Sunoliko kostos eishthriwn: ", teliko
    esoda += teliko
    theseis -= (enhl+paid)
print "sunolika esoda: ", esoda