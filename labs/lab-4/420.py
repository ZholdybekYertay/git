line = input().split()
if line:
    n_commands = int(line[0])
else:
    n_commands = 0
g = 0  
n = 0  

for _ in range(n_commands):
    command_line = input().split()
    if not command_line:
        continue
    
    scope = command_line[0]
    value = int(command_line[1])
    
    if scope == "global":
        g += value
    elif scope == "nonlocal":
        n += value
print(g, n)