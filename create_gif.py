
from PIL import Image

# List of images to include in the GIF
image_files = [
    "image1.png",
    "image2.png",
    "image3.png"
]

# Create an empty list to store the images
frames = []

# Open each image and add it to the list
for file in image_files:
    image = Image.open(file)
    image = image.convert("RGB")
    image = image.resize((500, 500))
    frames.append(image)

# Create the animated GIF
frames[0].save(
    "my_animation.gif",
    format="GIF",
    save_all=True,
    append_images=frames[1:],
    duration=500,
    loop=0
)

print("GIF created successfully!")
