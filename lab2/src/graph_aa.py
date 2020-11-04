a = [-3, -4, -7, 1, 4, 7, 3]
n = len(a)
ans = a[0]
ans_l = 0
ans_r = 0
sum = 0
min_sum = 0
min_pos = -1

for r in range(n):
    sum += a[r]

    cur = sum - min_sum
    if cur > ans:
        ans = cur
        ans_l = min_pos + 1
        ans_r = r

    if sum < min_sum:
        min_sum = sum
        min_pos = r

print(ans, ans_l, ans_r)
