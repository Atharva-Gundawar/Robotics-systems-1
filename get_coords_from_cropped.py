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
    print(lines)
    # Create a black background image of the same size as the original image
    height, width = img.shape
    background = np.zeros((height, width), dtype=np.uint8)

    # Draw detected lines on the black background
    drawn_img = lsd.drawSegments(background, lines)

    # Show the resulting image with only line segments
    cv2.imshow("LSD", drawn_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
