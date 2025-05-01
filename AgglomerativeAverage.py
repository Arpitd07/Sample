import math

def euclidean(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def cluster_distance_average(c1, c2):
    return sum(euclidean(p1, p2) for p1 in c1 for p2 in c2) / (len(c1) * len(c2))

def agglomerative_clustering_average(data, k):
    clusters = [[point] for point in data]
    while len(clusters) > k:
        min_dist = float('inf')
        pair_to_merge = (0, 1)
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist = cluster_distance_average(clusters[i], clusters[j])
                if dist < min_dist:
                    min_dist = dist
                    pair_to_merge = (i, j)
        i, j = pair_to_merge
        clusters[i].extend(clusters[j])
        clusters.pop(j)
    return clusters

n = int(input("Enter number of data points: "))
data = []
print("Enter each point (x y):")
for _ in range(n):
    x, y = map(float, input().split())
    data.append([x, y])

k = int(input("Enter number of clusters: "))
clusters = agglomerative_clustering_average(data, k)

print("\nClusters:")
for idx, cluster in enumerate(clusters, 1):
    print(f"Cluster {idx}: {cluster}")
