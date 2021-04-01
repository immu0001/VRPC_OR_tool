from scipy.spatial import distance
import math



def dist(p1,p2):
	return distance.euclidean(p1, p2)



location_data = [
	(40,50), (45,68), (45,70), (42,66), (42,68), (42,65), (40,69), (40,66), (38,68), (38,70), (35,66),
	(35,69), (25,85), (22,75), (22,85), (20,80), (20,85), (18,75), (15,75), (15,80), (30,50),
	(30,52), (28,52), (28,55), (25,50), (25,52)
]


	
	
dist_mat = []

for a in range(26):
	for b in range(26):
		print(dist(location_data[a],location_data[b]))
		#print(a,b)
		if b == 0 :
			dist_mat.append("[")
		if b == 26:
			dist_mat.append("],")
		dist_mat.append(dist(location_data[a],location_data[b]))
		

print(dist_mat)