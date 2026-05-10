A, B = map(int, input().split())

roots = []
for x in range(-1000, 1001):
    if x * x + 2 * A * x + B == 0:
        roots.append(x)

if len(roots) == 1:
    print(roots[0])
else:
    print(roots[0], roots[1])