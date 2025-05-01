import csv

# Load data from CSV file
def load_data_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# The rest of your Naive Bayes implementation

def calculate_prior(data, target_value):
    count = sum(1 for item in data if item['play'] == target_value)
    return count / len(data)

def calculate_likelihood(data, feature_value, feature_name, target_value):
    count_feature_and_target = sum(1 for item in data if item[feature_name] == feature_value and item['play'] == target_value)
    count_target = sum(1 for item in data if item['play'] == target_value)
    unique_vals = len(set(item[feature_name] for item in data))
    return (count_feature_and_target + 1) / (count_target + unique_vals)

def predict(data, input_data):
    prior_yes = calculate_prior(data, 'yes')
    prior_no = calculate_prior(data, 'no')

    prob_yes = prior_yes
    prob_no = prior_no

    for feature, value in input_data.items():
        prob_yes *= calculate_likelihood(data, value, feature, 'yes')
        prob_no *= calculate_likelihood(data, value, feature, 'no')

    return 'yes' if prob_yes > prob_no else 'no'

# Read data from CSV
data = load_data_from_csv('data.csv')

# User input
print("Enter weather conditions:")
outlook = input("Outlook (sunny/overcast/rainy): ").strip().lower()
temperature = input("Temperature (hot/mild/cool): ").strip().lower()
humidity = input("Humidity (high/normal): ").strip().lower()
wind = input("Wind (weak/strong): ").strip().lower()

# Prepare input for prediction
input_data = {
    'outlook': outlook,
    'temperature': temperature,
    'humidity': humidity,
    'wind': wind
}

# Predict and print result
prediction = predict(data, input_data)
print(f"Prediction for {input_data}: Will play? {prediction}")
