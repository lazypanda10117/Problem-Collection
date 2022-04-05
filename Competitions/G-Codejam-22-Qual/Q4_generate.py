from random import randint

T = 2
N = 1000


print(T)
for i in range(T):
	F = []
	P = []
	for j in range(N):
		rand_num = randint(0,10**9)
		rand_idx = randint(0, j)
		F.append(str(rand_num))
		P.append(str(rand_idx))
	print(N)
	print(' '.join(F))
	print(' '.join(P))