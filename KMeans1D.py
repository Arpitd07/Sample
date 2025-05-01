# 1D K-means function
def k_means_1d(data, mean1, mean2):
    step = 1
    while True:
        data1 = []
        data2 = []
        for i in data:
            if abs(i - mean1) < abs(i - mean2):
                data1.append(i)
            else:
                data2.append(i)

        new_mean1 = sum(data1) / len(data1) if data1 else mean1
        new_mean2 = sum(data2) / len(data2) if data2 else mean2

        print(f'\nStep {step}')
        print(f'Cluster 1: {data1}')
        print(f'Cluster 2: {data2}')
        print(f'Mean 1: {new_mean1}')
        print(f'Mean 2: {new_mean2}')

        if new_mean1 == mean1 and new_mean2 == mean2:
            break

        mean1 = new_mean1
        mean2 = new_mean2
        step += 1

    return data1, data2, mean1, mean2



data = []
n = int(input("Enter number of data points: "))
for _ in range(n):
    points = float(input("Enter data: "))
    data.append(points)

# Instead of asking user, pick initial means automatically
data_sorted = sorted(data)
mean1 = data_sorted[0]  # Smallest point
mean2 = data_sorted[-1] # Largest point

print(f"\nAutomatically chosen initial means: {mean1} and {mean2}")

cluster1, cluster2, final_mean1, final_mean2 = k_means_1d(data, mean1, mean2)

print("\nFinal Solution:")
print("Cluster 1:", cluster1)
print("Cluster 2:", cluster2)
print("Final Mean 1:", final_mean1)
print("Final Mean 2:", final_mean2)



