#==> countdown
def countdown(n):
    result = []
    for i in range(n, -1, -1):
        result.append(i)
    return result


output = countdown(5)
print(output)

#==> print and return 

def Print_and_Return(numbers):
    if len(numbers) == 2:
        print(numbers[0])
        return(numbers[1])
    else: 
        return "numbers must contain only two numbers"
result = Print_and_Return(1,2)
print(result)    

# ===> First Plus Length 
def First_and_return(numbers):
    sum = 0
    new_list = []
    for i in range(0,numbers, 1):
        new_list.append(i) 
        
        sum = len(new_list) + new_list[0]

            
    return sum

result = First_and_return(5)
print(result)

# ====> values freater than second 

def Values_Greater_than_Second(numbers):
    if len(numbers) < 2:
        return False

    our_list = []
    for i in range(0,len(numbers)):
        if numbers[i] > numbers[1]:
            our_list.append(numbers[i])
        
            
    return our_list
    
result = Values_Greater_than_Second([5, 2, 3, 2, 1, 4])
print(result) 

#====> This Length, That Value 
def This_Length_That_Value(size,value):
    list =[]
    return  [value]*size
result = This_Length_That_Value(3,6)
print(result)