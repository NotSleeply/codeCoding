x, y = map(int, input().split())

arr = []
for _ in range(x):
    row = list(map(float, input().split()))
    arr.append(row)

print(arr)