import random
import math

# Function to calculate Euclidean distance between two 2D points
def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to compute mean of a cluster of 2D points
def mean_point(cluster):
    x_total = sum(point[0] for point in cluster)
    y_total = sum(point[1] for point in cluster)
    return [round(x_total / len(cluster), 2), round(y_total / len(cluster), 2)]

# Step 1: Take input one point at a time
arr = []
print("Enter 2D points one by one (format: x y). Type 'done' to finish:")

while True:
    entry = input("Enter point: ")
    if entry.strip().lower() == "done":
        break
    try:
        x, y = map(float, entry.strip().split())
        arr.append([x, y])
    except:
        print("Invalid format. Please enter as: x y")

# Step 2: Randomly select 2 distinct starting centroids
k1, k2 = random.sample(arr, 2)

print("\nInitial centroids:")
print("k1:", k1)
print("k2:", k2)
print()

# Step 3: K-means loop
while True:
    k1new = []
    k2new = []

    for point in arr:
        d1 = euclidean(point, k1)
        d2 = euclidean(point, k2)

        if d1 <= d2:
            k1new.append(point)
        else:
            k2new.append(point)

    print("Cluster 1:", k1new)
    print("Cluster 2:", k2new)

    m1 = mean_point(k1new)
    m2 = mean_point(k2new)

    print("Centroids:")
    print("m1:", m1)
    print("m2:", m2)
    print()

    if m1 == k1 and m2 == k2:
        print("Final Cluster 1:", k1new)
        print("Final Cluster 2:", k2new)
        print("Final Centroids:")
        print("m1:", m1)
        print("m2:", m2)
        break

    k1 = m1
    k2 = m2
