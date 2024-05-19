def charge(volume):
    cost = 0
    if volume <= 50:
        cost = volume * 0.58
    if volume <= 90:
        cost = (50 * 0.58) + (volume - 50) * 0.94
    if volume > 90:
        cost = (50 * 0.58) + (40 * 0.94) + (volume - 90) * 0.12
    
    return cost



ogkos = float(input("ogkos nerou pou katanalwthike: "))

xrewsi = charge(ogkos)
ekptwsh = 0
if xrewsi >= 60:
    ekptwsh = xrewsi * 0.03
    print "O pelaths dikaioutai ekptwsh aksias: ", ekptwsh, "Euro."
else:
    "O pelaths den dikaioutai ekptwsh"
