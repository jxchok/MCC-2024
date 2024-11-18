def solve_detailed(n, k, s):
    MOD = 998244353
    
    def get_beauty(pair, k):
        if pair == '00':
            return pow(2, k, MOD) 
        elif pair == '11':
            term1 = 2 * pow(-1, k, MOD) 
            term2 = pow(2, k, MOD)  
            return ((term1 + term2) * pow(3, MOD-2, MOD)) % MOD
        else:
            term1 = pow(-1, k + 1, MOD) 
            term2 = pow(2, k, MOD)  
            return ((term1 + term2) * pow(3, MOD-2, MOD)) % MOD

    result = 0
    
    for i in range(n-1):
        pair = s[i:i+2]
        left_choices = i + 1
        right_choices = n - (i + 1)
        occurrences = left_choices * right_choices
        
        beauty = get_beauty(pair, k)
        contribution = (beauty * occurrences) % MOD
        
        # print(f"\nPair '{pair}' starting at position {i}:")
        # print(f"- Can start at {left_choices} position(s)")
        # print(f"- Can end at {right_choices} position(s)")
        # print(f"- Appears in {occurrences} substrings")
        # print(f"- Beauty after {k} transformations: {beauty}")
        # print(f"- Total contribution: {contribution}")
        
        
        result = (result + contribution) % MOD
    
    return result

def main():
    input_file = "input.txt"
    with open(input_file, 'r') as file:
        n, k = map(int, file.readline().strip().split())
        s = file.readline().strip()
    
    
    result = solve_detailed(n, k, s)
    print(result)

if __name__ == "__main__":
    main()
