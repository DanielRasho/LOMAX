# LOGIC:
# If you take one vertex of an square there other 3 points will always follow the same rule of 
#   - 2 points are away a distance L
#   - 1 point is a away a distance sqrt(2) * L

# ALGORITHM
# 1. Will take the first point and check its distances from the rest.
# 2. If the three points follow the rule, then do the same for point that is sqrt(2) * L
# 3. If conditions fullfill again, its a square

import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def is_square(p1, p2, p3, p4):
    points = [p1, p2, p3, p4]
    
    # Calculate all posible distances
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            distances.append(dist)
    
    distances.sort()
    
    side_length = distances[0]      # EDGES
    diagonal_length = distances[4]  # DIAGONALS
    
    # Check if the diagonals are sqrt(2) * side length
    if math.isclose(diagonal_length, math.sqrt(2) * side_length, rel_tol=1e-9) \
        and distances[0] == distances[1] == distances[2] == distances[3]:
        return True
    return False

# INPUTS
print("INPUT THE POINTS, separed by comma. \n Ex: \n \t2,3\n\t63,2")
p1 = tuple(map(float, input("Enter the coordinates of point 1. (x,y): ").split(",")))
p2 = tuple(map(float, input("Enter the coordinates of point 2. (x,y): ").split(",")))
p3 = tuple(map(float, input("Enter the coordinates of point 3. (x,y): ").split(",")))
p4 = tuple(map(float, input("Enter the coordinates of point 4. (x,y): ").split(",")))

# CONCLUSION
if is_square(p1, p2, p3, p4):
    print("The points form a square.")
else:
    print("The points do NOT form a square.")