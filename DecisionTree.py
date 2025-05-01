import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv(r'C:\Users\samub\OneDrive\Desktop\DWM\data.csv')  # Replace with your actual CSV file path

# Encode labels
label_encoders = {}
for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Features and target
X = df.drop('Buys_Computer', axis=1)
y = df['Buys_Computer']

# Train the model
clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
clf.fit(X, y)

# Plot the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=label_encoders['Buys_Computer'].classes_, filled=True)
plt.show()
