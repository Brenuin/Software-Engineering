import time
import os

# Define the directory where images are stored
image_directory = "/users/cs361-images"

while True:
    time.sleep(1)

    # Open and read from the file
    file = open("image-service.txt", "r")
    content = file.read().strip()
    file.close()

    # Check if content is a number
    if content.isdigit():
        image_number = int(content)

        # Get the list of all image files in the directory
        image_files = [f for f in os.listdir(image_directory) if f.endswith('.jpg')]

        # Use the Mod operator to mod the number with the number of actual images
        modded_number = image_number % len(image_files)

        # Construct the path with the modded_number
        path = os.path.join(image_directory, f"{modded_number}.jpg")

        # Write the path into the file
        file = open("image-service.txt", "w")
        file.write(path)
        file.close()
