import cv2
import numpy as np


image = cv2.imread("Homepage1_resized.png")

# Window name in which image is displayed
# window_name = 'Image'
#
# # font
# font = cv2.FONT_HERSHEY_DUPLEX
#
# # org
# org = (int(image.shape[1]/2)-600, int(image.shape[0]/2) - 200)
#
# # fontScale
# fontScale = 3
#
# # Blue color in BGR
# color = (0, 0, 0)
#
# # Line thickness of 2 px
# thickness = 3
#
# # Using cv2.putText() method
# image = cv2.putText(image, 'Hallym Medical A.I. Center', org, font,
#                    fontScale, color, thickness, cv2.LINE_AA)
#
# # Displaying the image
# cv2.imshow(window_name, image)
# cv2.waitKey(0)

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

# in_file, out_file, text = sys.argv[1:]

img = Image.open("Homepage1_resized.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 20)
draw.text((0, 0), text, (255, 255, 255), font=font)
img.save(out_file)
