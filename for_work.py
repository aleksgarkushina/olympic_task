t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    line = input()

    if 'B' * k in line:
        print(0)
        continue

    count_for_change = line[:k].count('W')
    min_count = count_for_change
    for r in range(k, n):
        if line[r-k] == 'W':
            count_for_change -= 1
        if line[r] == 'W':
            count_for_change += 1
        if count_for_change < min_count:
            min_count = count_for_change

    print(min_count)





