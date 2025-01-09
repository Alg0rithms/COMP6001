import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import time

# Read data from CSV file
data = pd.read_csv('CICIDS2017_friday_dataset.csv')

df = pd.DataFrame(data)
 
# Select features and label
X = df[[' Bwd Packet Length Mean', ' Average Packet Size', ' Active Max', 'Idle Mean', ' Flow IAT Std', ' Flow IAT Max', ' Bwd Packet Length Std', 'Bwd Packet Length Max']]
y = df[' Label']
 
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
 
# Normalize the features using Z-Score normalization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
 
# Initialize classifiers
classifiers = {
    'Support Vector Machine': SVC(),
    'Random Forest': RandomForestClassifier(),
    'Logistic Regression': LogisticRegression()
}
 
# Dictionary to store results
results = {}
 
# Train and evaluate each classifier
for name, clf in classifiers.items():
    start_time = time.time()
    clf.fit(X_train_scaled, y_train)
    end_time = time.time()
    # Predict on the test set
    y_pred = clf.predict(X_test_scaled)
    # Calculate performance metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, pos_label='BENIGN')
    recall = recall_score(y_test, y_pred, pos_label='BENIGN')
    # Store results
    results[name] = {
        'Training Time': end_time - start_time,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'Confusion Matrix': confusion_matrix(y_test, y_pred).tolist()
    }

for name, result in results.items():
    print("***", name, "***")
    print(f"Training Time: {result['Training Time']:.4f} seconds\nAccuracy: {result['Accuracy']:.4f}\nPrecision: {result['Precision']:.4f}\nRecall: {result['Recall']:.4f}\nConfusion Matrix: {result['Confusion Matrix']}")
    print("-------------------------------------------")

#print(results)

print(f"{'Classifier':<25} {'Training Time':<15} {'Accuracy':<10} {'Precision':<10} {'Recall':<10}")
print("="*70)
for name, metrics in results.items():
    print(f"{name:<25} {metrics['Training Time']:<15.4f} {metrics['Accuracy']:<10.4f} {metrics['Precision']:<10.4f} {metrics['Recall']:<10.4f}")

print("\nConfusion Matrices:")
for name, metrics in results.items():
    print(f"*** {name} ***")
    print(f"Confusion Matrix: {metrics['Confusion Matrix']}")
    print("--------------------------------------")


