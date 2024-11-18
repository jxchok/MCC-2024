with open("input.txt", "r") as file:
    n, m = map(int, file.readline().strip().split())
    tiers = list(map(int, file.readline().strip().split()))


guests = [(index, tier) for index, tier in enumerate(tiers)]
guests.sort(key=lambda x: (x[1], x[0]))
gifts = [0] * n

for i in range(m):
    guest_index = guests[i][0]
    gifts[guest_index] = 1

with open("output.txt", "w") as file:
    file.write(" ".join(map(str, gifts)))
