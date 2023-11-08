from PIL import Image, ImageDraw, ImageFont

# Set the dimensions of the image
width, height = 400, 200

# Create a new image with a white background
image = Image.new('RGB', (width, height), color = 'white')

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Load the desired font (provide the path to your own .ttf or .otf font file)
font = ImageFont.truetype("Roboto-Thin.ttf", 20)
# font = ImageFont.truetype('path_to_your_font_file.ttf', 30)

# Define the text to be written
text = "H"

# Calculate text size for centering the text
text_width, text_height = draw.textsize(text, font)

# Calculate the position to center the text
text_x = (width - text_width) // 2
text_y = (height - text_height) // 2

# Draw the text on the image
draw.text((text_x, text_y), text, fill='black', font=font)

# Save the image to a file
image.save('text_image.png')

