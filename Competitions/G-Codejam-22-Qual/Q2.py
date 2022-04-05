import sys

num_cases = int(sys.stdin.readline())

for n in range(num_cases):
    # [C, Y, M, K]
    p1 = [int(x) for x in sys.stdin.readline().split()]
    p2 = [int(x) for x in sys.stdin.readline().split()]
    p3 = [int(x) for x in sys.stdin.readline().split()]

    minC = min([p[0] for p in [p1,p2,p3]])
    minY = min([p[1] for p in [p1,p2,p3]])
    minM = min([p[2] for p in [p1,p2,p3]])
    minK = min([p[3] for p in [p1,p2,p3]])

    storage = 1000000
    C = min(storage, minC)
    storage -= C
    Y = min(storage, minY)
    storage -= Y
    M = min(storage, minM)
    storage -= M
    K = min(storage, minK)
    storage -= K
    
    if storage > 0:
        print(f"Case #{n+1}: IMPOSSIBLE")
    else:
        print(f"Case #{n+1}: {C} {Y} {M} {K}")
