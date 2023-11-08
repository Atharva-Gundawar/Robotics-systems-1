import numpy as np
import matplotlib.pyplot as plt
import tqdm

# Hyper Parameters
n_points = 20
k = 15
st_dev = 0.1 

# Function to generate 10 points around a given mean
def generate_points_around_mean(mean, num_points=n_points, std=st_dev):
    return np.random.normal(mean, std, size=(num_points, 2))

# Generate 10 random blue points
blue_points = np.random.rand(n_points, 2)

# Generate 10 random red points
red_points = np.random.rand(n_points, 2)

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
    progress_bar.update(1)
    return predicted_class

# Create a grid of points to visualize the decision boundary
x_min, x_max = data[:, 0].min() - 0.1, data[:, 0].max() + 0.1
y_min, y_max = data[:, 1].min() - 0.1, data[:, 1].max() + 0.1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
grid_points = np.c_[xx.ravel(), yy.ravel()]

# Create a tqdm instance for tracking progress
progress_bar = tqdm.tqdm(total=len(grid_points), desc="Classifying Points", dynamic_ncols=True)

# Classify the grid points
predicted_classes = np.array([knn_classification(data, labels, point, k) for point in grid_points])

# Close the tqdm progress bar
progress_bar.close()

# Reshape the predictions to match the grid shape
predicted_classes = predicted_classes.reshape(xx.shape)

# Plot the decision boundary
plt.contourf(xx, yy, predicted_classes, cmap='bwr', alpha=0.4)
plt.title('K-Nearest Neighbors Decision Boundary')
plt.show()
