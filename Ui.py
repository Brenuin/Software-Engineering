import time
from PIL import Image

def clear_file(filename):
    with open(filename, "w") as file:
        file.write("")

while True:
    choice = input("Enter 1 to generate a new image or 2 to exit: ")

    if choice == "1":
        with open("prng-service.txt", "w") as prng_file:
            prng_file.write("run")

        time.sleep(5)

        with open("prng-service.txt", "r") as prng_file:
            number = prng_file.read()

        with open("image-service.txt", "w") as img_file:
            img_file.write(number)

        time.sleep(5)

        with open("image-service.txt", "r") as img_file:
            image_path = img_file.read().strip()
            print(f"Image path: {image_path}")


            img = Image.open(image_path)
            img.show()

    elif choice == "2":
        clear_file("prng-service.txt")
        clear_file("image-service.txt")
        break

    else:
        print("Unknown option")


