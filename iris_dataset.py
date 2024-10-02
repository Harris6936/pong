# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Convert it to a pandas DataFrame for better visualization
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

# Display the first 5 rows of the dataset
print(iris_df.head())

# Import necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data  # Features (sepal length, sepal width, etc.)
y = iris.target  # Labels (species)

# Split the dataset into training and test sets
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shape of the training and testing sets
print(f'Training set size: {X_train.shape}')
print(f'Testing set size: {X_test.shape}')

# Import necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC  # Import Support Vector Classifier
from sklearn.metrics import accuracy_score  # Import accuracy score to evaluate performance

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data  # Features
y = iris.target  # Labels

# Split the dataset into training and test sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the SVM classifier (linear kernel)
model = SVC(kernel='linear')  # You can also use 'rbf', 'poly', etc. for different kernels

# Train the model using the training set
model.fit(X_train, y_train)

# Predict the labels for the test set
y_pred = model.predict(X_test)

# Evaluate the model by checking the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Example of predicting a single sample
sample_data = [[5.1, 3.5, 1.4, 0.2]]  # Example sample point
prediction = model.predict(sample_data)
print(f"Predicted class for the sample data: {prediction}")