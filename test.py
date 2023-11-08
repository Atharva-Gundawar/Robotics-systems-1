import cv2
import numpy as np

# Create a black canvas
image_size = (500, 500, 3)
image = np.zeros(image_size, np.uint8)

# Choose a font
font = cv2.FONT_HERSHEY_SIMPLEX

# Specify the list of capital letters
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Loop through each letter
for letter in capital_letters:
    # Create a copy of the canvas for each letter
    letter_image = image.copy()

    # Calculate text position
    text_size = cv2.getTextSize(letter, font, 1, 2)[0]
    text_x = (letter_image.shape[1] - text_size[0]) // 2
    text_y = (letter_image.shape[0] + text_size[1]) // 2

    # Add the text to the image
    cv2.putText(letter_image, letter, (text_x, text_y), font, 10, (255, 255, 255), 1, cv2.LINE_AA)

    # Save the image with the letter as the filename
    image_filename = f"{letter}.png"
    cv2.imwrite(image_filename, letter_image)

# Cleanup OpenCV windows if they are open
cv2.destroyAllWindows()
