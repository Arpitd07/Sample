import math

data = { 
    'Age': ['youth', 'youth', 'middle-aged', 'senior', 'senior', 'senior', 'middle-aged', 'youth', 'youth', 'senior', 'youth', 'middle-aged', 'middle-aged', 'senior'], 
    'Income': ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low', 'medium', 'medium', 'medium', 'high', 'medium'], 
    'Student': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no'], 
    'Credit_rating': ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'excellent'], 
    'Buys_Computer': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no'] 
}

features = ['Age','Income','Student','Credit_rating']

def info_D(data):
    c1 = data['Buys_Computer'].count('yes')
    c2 = data['Buys_Computer'].count('no')
    total = c1 + c2
    p1 = c1 / total
    p2 = c2 / total
    entropy = 0
    if p1 > 0 and p2 > 0:
        entropy = (-p1 * math.log2(p1)) + (-p2 * math.log2(p2))
    print("==== Info(D) ====")
    print(f"C1 (yes): {c1}")
    print(f"C2 (no): {c2}")
    print(f"Info(D): {entropy:}")
    return entropy

def ID3(data, attribute, target='Buys_Computer'):
    values = []
    for val in data[attribute]:
        if val not in values:
            values.append(val)
    total = len(data[target])
    entropy = 0
    for val in values:
        subset_yes = 0
        subset_no = 0
        subset_total = 0
        for i in range(total):
            if data[attribute][i] == val:
                subset_total += 1
                if data[target][i] == 'yes':
                    subset_yes += 1
                else:
                    subset_no += 1
        if subset_total == 0:
            continue
        p_yes = subset_yes / subset_total
        p_no = subset_no / subset_total
        ent = 0
        if p_yes > 0 and p_no > 0:
            ent = (-p_yes * math.log2(p_yes)) + (-p_no * math.log2(p_no))
        entropy += (subset_total / total) * ent
    return entropy

def info_gain(data, x, attribute):
    gain=x - ID3(data, attribute)
    print(f"Information gain {attribute}: {gain}")
    return gain

def get_best_feature(data, x, features):
    best_feature = None
    max_gain = -1
    for feature in features:
        gain = info_gain(data, x, feature)
        if gain > max_gain:
            max_gain = gain
            best_feature = feature
    return best_feature

def majority_class(labels):
    freq = {}
    for label in labels:
        if label not in freq:
            freq[label]=1
        else:
            freq[label]+=1
    majority = None
    max_count=-1
    for label in freq:
        if freq[label] >max_count:
            max_count=freq[label]
            majority=label
    return majority

def build_tree(data, features, target='Buys_Computer'):
    
    if data[target].count(data[target][0]) == len(data[target]):
        return data[target][0]

    
    if not features:
        return majority_class(data[target])
    
    x = info_D(data)
    best_feature = get_best_feature(data, x, features)
    tree = {best_feature: {}}

    # Unique values manually
    unique_values = []
    for val in data[best_feature]:
        if val not in unique_values:
            unique_values.append(val)

    for value in unique_values:
        # Subset
        subset = {}
        for key in data:
            subset[key] = []
        for i in range(len(data[best_feature])):
            if data[best_feature][i] == value:
                for key in data:
                    subset[key].append(data[key][i])

        sub_features = []
        for f in features:
            if f != best_feature:
                sub_features.append(f)

        tree[best_feature][value] = build_tree(subset, sub_features, target)

    return tree


final_tree = build_tree(data, features)
print("\nFinal Decision Tree:")
print(final_tree)