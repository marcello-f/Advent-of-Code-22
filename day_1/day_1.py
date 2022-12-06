with open('input_1.txt') as file:
    lines = file.read().splitlines()

def calories(array):
    seen = []
    count = 0
    for line in array:
        if line == "":
            seen.append(count)
            count = 0
        else:
            count += int(line)
    seen.append(count)
    return seen

seen = sorted(calories(lines))
print(max(seen), sum(seen[-3::]))