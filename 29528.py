smarket = []
price = []
n = 30

for i in range(10): 
    name = raw_input("Onoma market: ")
    smarket.append(name)
    sunolo = 0
    for timh in range(n): 
        productA = float(input("Timh hmeras proiontos: "))
        sunolo += productA
    meshtimh = sunolo / n
    price.append(meshtimh)


euros = len(price)
flag = False

while euros-1 > 0 and not flag:
    flag = True
    for j in range(euros-1, 0, -1):
        if price[j] < price[j-1]:
            price[j], price[j-1] = price[j-1], price[j]
            smarket[j], smarket[j-1] = smarket[j-1], smarket[j]
            flag = False

print "Ta 3 market me tin xamhloterh mesh timh einai: "
for k in range(3):
    print smarket[k]
    print price[k]
    
