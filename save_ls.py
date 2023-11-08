import cv2
import numpy as np

# Specify the list of capital letters
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Loop through each letter
for letter in capital_letters:
    # Load the image
    img = cv2.imread(f'cropped_letters/cropped{letter}.png', 0)

    # Create default parametrization LSD
    lsd = cv2.createLineSegmentDetector(0)

    # Detect lines in the image
    lines = lsd.detect(img)[0]  # Position 0 of the returned tuple are the detected lines

    # Create and open a file for saving line segment data
    with open(f'ls_{letter}.txt', 'w') as file:
        for line in lines:
            x1, y1, x2, y2 = line.flatten()
            x1, y1, x2, y2 = round(x1), round(y1), round(x2), round(y2)
            # Save the line segment data to the file
            file.write(f"{x1},{y1},{x2},{y2}\n")
