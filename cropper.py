import cv2
import numpy as np



# Specify the list of capital letters
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Loop through each letter
for letter in capital_letters:

    # Load the image
    image = cv2.imread(f'letters/{letter}.png')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find contours in the grayscale image
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour (assuming it's the boundary)
    largest_contour = max(contours, key=cv2.contourArea)

    # Get the bounding box of the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Crop the image to the bounding box
    cropped_image = image[y:y+h, x:x+w]

    # Save the cropped image
    cv2.imwrite(f'cropped_letters/cropped{letter}.png', cropped_image)

# Display the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
