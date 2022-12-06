from toolz import sliding_window

with open('input_6.txt') as file:
    lines = file.read().splitlines()
    
line = lines[0]

def marker(string, n):
    lists = list(sliding_window(n,string))

    for i in range(len(lists)):
        if len(set(lists[i])) == n:
            return i + n

print(marker(line, 4), marker(line, 14))
