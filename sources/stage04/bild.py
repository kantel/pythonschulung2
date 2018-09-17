from PIL import Image
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

im = Image.open("me.jpg")
im.show()
