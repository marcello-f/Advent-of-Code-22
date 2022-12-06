import string

with open("input_3.txt") as file:
    lines = file.read().splitlines()

def alpha_dict():
    priorities = {}
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    count = 1

    for letter in lower:
        priorities[letter] = count
        count += 1
        
    for letter in upper:
        priorities[letter] = count
        count += 1

    return priorities

def find_overlap(string):
    first_half, second_half = string[:len(string)//2], string[len(string)//2:]
    seen = set()
    for char in first_half:
        if char in second_half:
            return char
        else:
            seen.add(char)

def find_overlap_3(string1, string2, string3):
    seen = set()
    for char in string1:
        if char in string2 and char in string3:
            return char
        else:
            seen.add(char)

priorities = alpha_dict()

sum_1 = sum([priorities[find_overlap(line)] for line in lines ])
sum_2 = sum([priorities[find_overlap_3(lines[n],lines[n+1],lines[n+2])] for n in range(0, len(lines), 3)])

print(sum_1, sum_2)