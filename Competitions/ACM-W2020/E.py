import sys

line = sys.stdin.readline()
line2 = sys.stdin.readline()
perscribed = int(line.split()[1])
inputs = [int(a) for a in line2.split()]

def quickMedian(lis, dis):
	pivot = lis[-1]
	less = [a for a in lis if a < pivot]
	great = [a for a in lis if a > pivot]
	# print(less)
	# print(great)
	# print(dis)
	if len(less) == dis:
		return pivot
	elif len(less) < dis:
		return quickMedian(great, dis-len(less)-1) 
	else:
		return quickMedian(less, dis)

def sumCons(n):
	return n*(n+1)/2

median = quickMedian(inputs, int(len(inputs)/2))

# print(median)

halfSize = int(len(inputs)/2)
if len(inputs)%2 == 0:
	# one side is greater
	size = (perscribed)*sumCons(halfSize) + (perscribed)*sumCons(halfSize-1)
else:
	size = (perscribed)*2*(sumCons(halfSize))

# print(size)

sumOfNonMedian = 0
for i in inputs:
	# print("{} - {} = {}".format(i, median, abs(i-median)))
	sumOfNonMedian += abs(i - median)

# print(sumOfNonMedian)
result = int(sumOfNonMedian - size)
print(abs(result))
