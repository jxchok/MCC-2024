def can_cover_corners(n, m, A, B):
    if (A <= n and B <= m) or (B <= n and A <= m):
        if A == n or B == m or A == m or B == n:
            return "YES"
    return "NO"


input_file = 'input.txt' 
with open(input_file, 'r') as file:
    T = int(file.readline().strip())  
    results = []

    for _ in range(T):
        n, m, A, B = map(int, file.readline().split())
        result = can_cover_corners(n, m, A, B)
        results.append(result)


print("\n".join(results))

with open("output.txt", "w") as file:
    file.write("\n".join(results))