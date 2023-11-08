import numpy as np
import matplotlib.pyplot as plt

# Function to generate 10 points around a given mean
def generate_points_around_mean(mean, num_points=10, std=0.05):
    return np.random.normal(mean, std, size=(num_points, 2))

# Generate 10 random blue points
blue_points = np.random.rand(10, 2)

# Generate 10 random red points
red_points = np.random.rand(10, 2)

# Generate 10 points around each blue point and their means
blue_data = np.vstack([generate_points_around_mean(point) for point in blue_points])
blue_labels = np.zeros(blue_data.shape[0])

# Generate 10 points around each red point and their means
red_data = np.vstack([generate_points_around_mean(point) for point in red_points])
red_labels = np.ones(red_data.shape[0])

# Combine the data and labels for both classes
data = np.vstack((blue_data, red_data))
labels = np.concatenate((blue_labels, red_labels))

# Plot the data with different colors for blue and red
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='bwr')
plt.title('Generated 2D Data')
plt.colorbar(ticks=[0, 1], label='Class')
plt.show()

import numpy as np

# Function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Function to perform K-nearest neighbors classification
def knn_classification(train_data, train_labels, new_point, k=3):
    distances = []
    
    # Calculate distances from the new_point to all points in the training data
    for i in range(len(train_data)):
        dist = euclidean_distance(train_data[i], new_point)
        distances.append((train_labels[i], dist))
    
    # Sort the distances and select the top k neighbors
    distances.sort(key=lambda x: x[1])
    neighbors = distances[:k]
    
    # Count the number of neighbors for each class
    class_counts = {}
    for neighbor in neighbors:
        class_label = neighbor[0]
        if class_label in class_counts:
            class_counts[class_label] += 1
        else:
            class_counts[class_label] = 1
    
    # Find the class with the most neighbors
    predicted_class = max(class_counts, key=class_counts.get)
    
    return predicted_class

# Sample data
data = np.vstack((blue_data, red_data))
labels = np.concatenate((blue_labels, red_labels))

# New unseen data point
unseen_point = np.array([0.6, 0.6])

# Perform K-nearest neighbors classification
k_value = 3  # You can choose any value for k
predicted_class = knn_classification(data, labels, unseen_point, k=k_value)

print(f"The predicted class for the unseen point {unseen_point} is: {'Blue' if predicted_class == 0 else 'Red'}")
