for x in range(150): 
    print(x)

for y in range(5,1000):
    if y%5 == 0:
        print(y)

for z in range(1,100):
    if z % 5 == 0: 
        print("Coding")
    if z%10 == 0:
        print("Coding Dojo")

sum = 0 
for a in range(500000):
    if a % 2 == 1: 
        sum+=a
print(sum)

for b in range(2018,0,-4):
    if b > 0:
        print(b)

def flexible_counter(lowNum,highNum,mult):
    for c in range(lowNum, highNum):
        if c % mult == 0:
            print (c)

flexible_counter(2,10,3)




