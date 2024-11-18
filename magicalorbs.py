MOD = 10**9 + 7

def max_magical_power(orbs):
    while len(orbs) > 1:
        orbs.sort()
        
        x = orbs[-2]
        y = orbs[-1]
        
        new_orb = (x + 2 * y) 
        
        orbs.pop()
        orbs.pop()
        
        orbs.append(new_orb)
    return orbs[0]% MOD

input_file = 'input.txt'

with open(input_file, 'r') as file:
    T = int(file.readline().strip())
    results = []
    
    for _ in range(T):
        n = int(file.readline().strip())
        orbs = list(map(int, file.readline().strip().split()))
        result = max_magical_power(orbs)
        results.append(result)

for result in results:
    print(result)

with open('output.txt', 'w') as file:
    for result in results:
        file.write(f"{result}\n")


