import sys
# read from stdin
#for line in sys.stdin:

# print to stdout
# print

vertex = dict() #idx, visited
edges = dict() #start, (end, weight)
# edgesByWeight = dict() #weight, dict(start, end)
stackOfPeople = list()

minLen = -1
def getAllPaths(start, end, current, len):
	v = current
	for e in edges[v]:
		
	#forward if possitive weight or poping stack

def buildGraph():
	n_cases = int(sys.stdin.readline())
	for i in n_cases:
		inp = sys.stdin.readline().split()
		n_edges = int(inp[0])
		n_queries = int(inp[2])
		for j in n_edges:
			direc = sys.stdin.readline().split()
			if int(direc[0]) in edges:
				edges[int(direc[0])].append((int(direc[1]), int(direc[2])))
			else:
				edges[int(direc[0])] = [(int(direc[1]), int(direc[2]))]
		for k in n_queries:
			t_in = sys.stdin.readline().split()
			start = t_in[0]
			end = t_in[1]
			minLen = 0
			allPaths = calculateAllPaths(start, end, start, 0)
			print(minLen if minLen != -1 else "impossible")
