import tkinter as tk
from PIL import Image, ImageTk
import os
import random

image_files = [f for f in os.listdir("images")]
image_paths = [os.path.join("images", f) for f in image_files]

def prng_service():
    return random.randint(0, 100)

def get_image(i):
    return image_paths[i % len(image_files)]

def display_image():
    index = prng_service()
    image_path = get_image(index)

    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

root = tk.Tk()
root.title("Random Image Selector")

button = tk.Button(root, text="Get Random Image", command=display_image)
button.pack(pady=20)

image_label = tk.Label(root)
image_label.pack(pady=20)

root.mainloop()
