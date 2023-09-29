import time
import random

while True:
    time.sleep(1)

    # Open and read from the file
    file = open("prng-service.txt", "r")
    content = file.read()
    file.close()

    if content == "run":
        # Generate random number
        rand_number = random.randint(0, 100)

        # Open the file in write mode to erase "run" and write the random number
        file = open("prng-service.txt", "w")
        file.write(str(rand_number))
        file.close()
