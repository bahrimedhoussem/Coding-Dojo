for x in range(151):
    print(x)

for x in range(5, 1000, 5):
    print(x)   
    
for x in range(1,101):
    if x%10 == 0:
        print("coding dojo")
    elif x%5 == 0:
        print("coding")
    else: 
        print(x)    
        
sum = 0
for x in range(0,500000):
    sum += x
    print(x)

        
for num in range(2018, 0, -4):
    print(num)    

lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)

