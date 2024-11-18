def simple_game(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    n = int(lines[0])  #
    pairs = []
    
    for i in range(1, n + 1):
        a, b = map(int, lines[i].split())
        pairs.append((a, b))
    

    pairs.sort(key=lambda x: x[0] + x[1], reverse=True)
    
    evirir_score = 0
    rhae_score = 0
    
    for i in range(n):
        if i % 2 == 0: 
            evirir_score += pairs[i][0]
        else: 
            rhae_score += pairs[i][1]
    
    result = evirir_score - rhae_score
    return result


input_file = "input.txt"  

print(simple_game(input_file))
