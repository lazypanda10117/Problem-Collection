import math
import sys

R = 6371009
def calculateDiff():
	n_cases = int(sys.stdin.readline())
	for i in range(n_cases):
		inp = sys.stdin.readline().split()
		originLa = float(inp[0])
		originLo = float(inp[1])
		destLa = float(inp[2])
		destLo = float(inp[3])
		laDiff = calculateProj(originLa, destLa)
		print("LA Diff")
		print(laDiff)
		loDiff = calculateProj(originLo, destLo)
		print("LO Diff")
		print(loDiff)
		E = math.sqrt(R**2 + R**2 - 2*(R**2)*math.cos(degreeToRadian(laDiff)))
		print("E")
		print(E)
		auxAngle = 180-90-abs(min(destLa, originLa))
		print("Aux Angle")
		print(auxAngle)
		K = math.sin(degreeToRadian(auxAngle)) * R/math.sin(degreeToRadian(90))
		print("K")
		print(K)
		newArcSecantOnLang = math.sqrt(K**2 + K**2 - 2*(K**2)*math.cos(degreeToRadian(loDiff)))
		print("New Arc Secant")
		print(newArcSecantOnLang)
		ac = math.acos((R**2 + R**2 - newArcSecantOnLang**2)/(2*R**2))
		print("AC")
		print(ac)
		equatorAngle = radianToDegree(ac)
		print("Equator Ang")
		print(equatorAngle)
		D = math.sqrt(R**2 + R**2 - 2*(R**2)*math.cos(degreeToRadian(equatorAngle)))
		print("D")
		print(D)
		F = math.sqrt(D**2 + E**2)
		print("F")
		print(F)
		angleF = radianToDegree(math.acos((R**2 + R**2 - F**2)/(2*R*R)))
		print("Angle F")
		print(angleF)
		curveF = 2*math.pi*R*(angleF/360)
		print("Curve F")
		print(curveF)
		print("Distance Difference")
		print(int(curveF-F))
	

def calculateProj(angle1, angle2):
	return min(360 - abs(angle1 - angle2), abs(angle1-angle2))

def degreeToRadian(deg):
	return (deg/360)*2*math.pi

def radianToDegree(rad):
	return (rad/(2*math.pi))*360

calculateDiff()


# print(laDiff)
		# loDiff = calculateProj(originLo, destLo)
		# print(loDiff)
		# newAngle = abs(180-90-min(originLa, destLa))
		# print("New Ang")
		# print(newAngle)
		# newLength = math.sin(degreeToRadian(newAngle)) * (RADIUS/math.sin(degreeToRadian(90)))
		# print("New Len")
		# print(newLength)
		# descRatio = newLength/RADIUS
		# print("Desc Ration")
		# print(descRatio)
		# rrLong = math.sqrt(2*(RADIUS**2) * (1 - math.cos(degreeToRadian(loDiff*descRatio))))
		# print("RR Long")
		# print(rrLong)
		# rrLang = math.sqrt(2*(RADIUS**2) * (1 - math.cos(degreeToRadian(laDiff))))
		# print("RR Lang")
		# print(rrLang)
		# directDist = math.sqrt(rrLong**2 + rrLang**2)
		# print("Direct Dist")
		# print(directDist)
		# curveDistAngle = math.acos((2*(RADIUS**2)-(directDist**2))/(2*(RADIUS**2)))
		# print(curveDistAngle)
		# curveDist = 2*math.pi*RADIUS*(curveDistAngle/360)
		# print(int(curveDist-directDist))P

# Sample Input
# 1
# 43.466667 -80.516667 30.058056 31.228889
# Output Specification
# For each test case, output a line containing a single integer, the difference in the distance between the two points following the great circle route around the surface of the earth and following the straight line through the earth, in metres. Round the difference of the distances to the nearest integer number of metres.
# Output for Sample Input
# 802333