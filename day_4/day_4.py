with open('input_4.txt') as file:
    lines = file.read().splitlines()

def parser(string):
    string = string.replace("-",",")
    array = string.split(",")
    array = [int(i) for i in array]
    return array
        
def check_full(string):
    array = parser(string)
    if array[0] <= array[2] and array[1] >= array[3]:
        return True
    elif array[0] >= array[2] and array[1] <= array[3]:
        return True
    else:
        return False
    
def check_part(string):
    array = parser(string)
    list1 = [i for i in range(array[0],array[1]+1)]
    list2 = [i for i in range(array[2],array[3]+1)]
    
    for i in list1:
        if i in list2:
            return True
    return False
    
counter1 = 0
counter2 = 0
for line in lines:
    if check_full(line) == True:
        counter1 += 1
    if check_part(line) == True:
        counter2 += 1  
        
print(counter1, counter2)