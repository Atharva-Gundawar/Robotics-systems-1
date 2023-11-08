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

    # Create a black background image of the same size as the original image
    height, width = img.shape
    background = np.zeros((height, width), dtype=np.uint8)

    # Draw detected lines on the black background
    drawn_img = lsd.drawSegments(background, lines)

    # Add green dots at the starting points and yellow dots at the ending points
    for line in lines:
        x1, y1, x2, y2 = line.flatten()
        x1, y1, x2, y2 = round(x1), round(y1), round(x2), round(y2)
        print(f"Starting point: ({x1}, {y1}), Ending point: ({x2}, {y2}")

    # Show the resulting image with lines and dots
    cv2.imshow("LSD", drawn_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
