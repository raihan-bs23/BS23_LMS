from PIL import Image
import os

directory = "/home/bs865/Documents/bs23-lms/media/images/"
size = (800, 600) # set the desired size here

# loop over all files in the directory
for filename in os.listdir(directory):
    # check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # open the image file using Pillow
        image = Image.open(os.path.join(directory, filename))
        # resize the image
        resized_image = image.resize(size)
        # save the resized image to the same directory
        resized_image.save(os.path.join(directory, filename))
