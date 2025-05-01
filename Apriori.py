from itertools import combinations
import matplotlib.pyplot as plt

# Function to get frequent 1-itemsets
def get_frequent_itemsets(transactions, min_support):
    itemsets = {}
    for transaction in transactions:
        for item in transaction:
            if item in itemsets:
                itemsets[item] += 1
            else:
                itemsets[item] = 1
    frequent_itemsets = {item: support for item, support in itemsets.items() if support >= min_support}
    return frequent_itemsets

# Function to generate candidate k-itemsets
def get_candidate_itemsets(frequent_itemsets, k):
    candidates = []
    frequent_items = list(frequent_itemsets.keys())
    for combination in combinations(frequent_items, k):
        candidates.append(combination)
    return candidates

# Apriori algorithm implementation
def apriori(transactions, min_support):
    k = 1
    frequent_itemsets = get_frequent_itemsets(transactions, min_support)
    all_frequent_itemsets = [frequent_itemsets]
    
    while frequent_itemsets:
        k += 1
        candidates = get_candidate_itemsets(frequent_itemsets, k)
        candidate_supports = {candidate: 0 for candidate in candidates}
        
        for transaction in transactions:
            for candidate in candidates:
                if set(candidate).issubset(set(transaction)):
                    candidate_supports[candidate] += 1
                    
        frequent_itemsets = {
            itemset: support for itemset, support in candidate_supports.items()
            if support >= min_support
        }
        
        if frequent_itemsets:
            all_frequent_itemsets.append(frequent_itemsets)
    
    return all_frequent_itemsets

# Sample transactions
transactions = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'butter'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter']
]

# Minimum support count
min_support = 2

# Run Apriori algorithm
frequent_itemsets = apriori(transactions, min_support)

# Print results
for level, itemsets in enumerate(frequent_itemsets, start=1):
    print(f"\nFrequent {level}-itemsets:")
    for itemset, support in itemsets.items():
        print(f"{itemset}: {support}")

# Prepare data for bar plot
support_data = []
labels = []
for itemsets in frequent_itemsets:
    for itemset, support in itemsets.items():
        support_data.append(support)
        labels.append(str(itemset))

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(labels, support_data, color='skyblue')
plt.xlabel('Frequent Itemsets')
plt.ylabel('Support Count')
plt.title('Support Count of Frequent Itemsets')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
