megisto_name = ""
megisto_arithmos = 0
elaxisto_name = ""
elaxisto_arithmos = 0
sunolo = 0
counter = 0


school = raw_input("Onoma sxoleiou: ")
while school != "TELOS":
    students = int(input("Arithmos mathitwn: "))
    while students < 0 or students > 700:
        print "O arithmos mathitwn prepei na einai 0-200."
        students = int(input("Arithmos mathitwn: "))
    counter += 1
    sunolo += students
    if students > megisto_arithmos:
        megisto_arithmos = students
        megisto_name = school
    if elaxisto_arithmos == 0:
        elaxisto_arithmos = megisto_arithmos
    elif students < elaxisto_arithmos:
        elaxisto_arithmos = students
        elaxisto_name = school
    school = raw_input("Onoma sxoleiou: ")

print "To sxoleio me tous perissoterous mathites einai to ", megisto_name, "me arithmo mathitwn", megisto_arithmos
print "To sxoleio me tous ligoterous mathites einai to", elaxisto_name, "me arithmo mathitwn", elaxisto_arithmos