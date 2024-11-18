def can_destroy_all_targets(n, m, k, x, target_hp):
    remaining_hp = target_hp.copy()
    arrows_used = 0
    
    i = 0
    while i < n and arrows_used < k:
        if remaining_hp[i] <= 0:
            i += 1
            continue
        
        arrows_used += 1

        for j in range(i, n):
            damage = max(0, m * x - (j - i) * (j - i))
            remaining_hp[j] -= damage
            
        if remaining_hp[i] > 0:
            i -= 1
        i += 1
    
    return all(hp <= 0 for hp in remaining_hp)

def find_min_x(n, m, k, target_hp):
    left = 0
    right = (max(target_hp) // m + 1) * 2
    
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if can_destroy_all_targets(n, m, k, mid, target_hp):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result if result > 0 else 1

def main():
    with open('input.txt', 'r') as f:
        n, m, k = map(int, f.readline().strip().split())
        target_hp = list(map(int, f.readline().strip().split()))
    
    
    result = find_min_x(n, m, k, target_hp)
    print(result)
    
    with open('output.txt', 'w') as f:
        f.write(str(result))

if __name__ == '__main__':
    main()