with open('input_2.txt') as file:
    lines = file.read().splitlines()
    
def WDL(string):
    elf = string[0]
    you = string[2]
    
    if elf == "A" and you == "X":
        return 3 + 1
    elif elf == "A" and you == "Y":
        return 6 + 2
    elif elf == "A" and you == "Z":
        return 0 + 3
    
    elif elf == "B" and you == "X":
        return 0 + 1
    elif elf == "B" and you == "Y":
        return 3 + 2
    elif elf == "B" and you == "Z":
        return 6 + 3
    
    elif elf == "C" and you == "X":
        return 6 + 1
    elif elf == "C" and you == "Y":
        return 0 + 2
    elif elf == "C" and you == "Z":
        return 3 + 3

def WDL2(string):
    elf = string[0]
    you = string[2]
    
    if elf == "A" and you == "X":
        return 0 + 3
    elif elf == "A" and you == "Y":
        return 3 + 1
    elif elf == "A" and you == "Z":
        return 6 + 2
    
    elif elf == "B" and you == "X":
        return 0 + 1
    elif elf == "B" and you == "Y":
        return 3 + 2
    elif elf == "B" and you == "Z":
        return 6 + 3
    
    elif elf == "C" and you == "X":
        return 0 + 2
    elif elf == "C" and you == "Y":
        return 3 + 3
    elif elf == "C" and you == "Z":
        return 6 + 1
    
total = 0
for line in lines:
    total += WDL(line)
    
total2 = 0
for line in lines:
    total2 += WDL2(line)
    
print(total, total2)