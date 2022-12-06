import re

with open('input_5.txt') as file:
    lines = file.read().splitlines()

def stack_height(array):
    output = 0
    for line in array:
        if line[1] == '1':
            break
        output += 1
    return output
    
def stack_parser(array):
    stacks = []
    line_len = len(array[0])
    for n in range(1,line_len,4):
        stacks.append([])

    count = 0
    for line in array[:stack_height(array)]:
        for i in range(1,line_len,4):
            if line[i] != ' ':
                stacks[count].append(line[i])
            count += 1 
        count = 0

    for stack in stacks:
        stack.reverse()
        
    return stacks

def num_parser(string):
    return [int(s) for s in re.findall(r'\b\d+\b', string)]  

def rearrange(array):
    stacks = stack_parser(array)
    print(stacks)

    for line in array[stack_height(array)+2::]:
        nums = num_parser(line)
        for move in range(nums[0]):
            stacks[nums[2]-1].append(stacks[nums[1]-1].pop())

    output = ""  
    for i in stacks:
        output += i[-1]
    
    return output

def rearrange2(array):
    stacks = stack_parser(array)

    for line in array[stack_height(array)+2::]:
        nums = num_parser(line)
        if nums[0] == 1:
            stacks[nums[2]-1].append(stacks[nums[1]-1].pop())
        else:
            temp = []
            for i in range(nums[0]):
                temp.append(stacks[nums[1]-1].pop())
                
            for i in range(len(temp)):
                stacks[nums[2]-1].append(temp.pop())

    output = ""       
    for i in stacks:
        output += i[-1]

    return output

print(rearrange(lines), rearrange2(lines))