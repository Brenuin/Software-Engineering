import time
import os

image_directory = "./images"

while True:
    time.sleep(1)


    file = open("image-service.txt", "r")
    content = file.read()
    file.close()


    if content.isdigit():
        image_number = int(content)


        image_files = [f for f in os.listdir(image_directory)]


        index = image_number % len(image_files)


        filename = image_files[index]


        path = f"./images/{filename}"


        file = open("image-service.txt", "w")
        file.write(path)
        file.close()